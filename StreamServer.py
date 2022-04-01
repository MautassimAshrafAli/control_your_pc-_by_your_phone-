import cv2
import base64
import time
from threading import Thread
from Server import MainServer as Server


class StreamServer(Server):

    StartedServer = False
    def __init__(self, host, port, clients_sessions, buffer_size, AES, checkPeriod, shutdownCommand):

        super().__init__(host, port, buffer_size, clients_sessions, checkPeriod)
        self.AES = AES
        super().setAES(AES)
        # self.host = host
        # self.port = port
        # self.buffer_size = buffer_size
        # self.clients_sessions = clients_sessions
        # self.checkPeriod = checkPeriod
        self.ShutdownCommand = shutdownCommand
        self.stopServer = False
        # clients = dict()
        # self.clients = clients
        #
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.bind((self.host, self.port))
        # sock.listen(len(self.clients_sessions))
        #
        # self.sock = sock

        print("Stream Server Has Been Started ..")
        StreamServer.StartedServer = True
        self.cam = cv2.VideoCapture(0)

    def AuthenticateClient(self, client, address):
        if str(address[0]).startswith('192.168.') or str(address[0]).startswith('10.0.') or str(address[0]).startswith(
                '172.16.') or str(address[0]).startswith('127.0.0.1'):
            try:
                identity_data = client.recv(self.buffer_size)
                # identity_text = identity_data.decode("utf-8")
                identity_text = self.AES.decrypt(identity_data, False)

                for clientSession in self.clients_sessions:
                    clientKeys = clientSession.keys()
                    clientKey = ""
                    for x in clientKeys:
                        clientKey = x
                        break

                    if clientSession[clientKey] == identity_text:
                        self.clients[clientKey] = client
                        print("Client At {}:{} connected to the server!".format(address[0], address[1]))
            except ConnectionResetError:
                print("Client At {}:{} reset the connection!".format(address[0], address[1]))
            except ConnectionRefusedError or ConnectionAbortedError or ConnectionError:
                print("Connection Error With Client {}:{}".format(address[0], address[1]))
            except Exception:
                print("Key Exchange Error With Client {}:{}".format(address[0], address[1]))

    def Connect_To_clients(self):

        print("Connecting to clients ..")
        self.stopAcceptClients = False
        self.cam.release()

        t = Thread(target=self.accept_client)
        t.start()

        numOfClients = len(self.clients_sessions)

        while True:
            if len(self.clients) == numOfClients:
                print("Server has connected to all clients ..")
                self.stopAcceptClients = True
                self.cam = cv2.VideoCapture(0)
                break

            time.sleep(self.checkPeriod)   # change wait time before checking

    def ClientConnectionReset(self, clientKey):
        # del self.clients[clientKey]
        print("Client {} disconnected".format(clientKey))
        time.sleep(1)
        self.StopServer()
        self.stopServer = True

    def receive_frame(self, clientKey):
        length = self.receive_data(clientKey)
        length = int(length.decode("utf-8"))
        data = b""
        while length > 0:
            data += self.receive_data(clientKey)
            length -= self.buffer_size
        return base64.b64decode(data)

    def receive_frame_encrypted(self, clientKey):
        length = self.receive_data_encrypted(clientKey)
        # length = base64.b64decode(length)
        length = int(length)
        data = b""
        while length > 0:
            data += self.receive_data(clientKey)
            length -= self.buffer_size

        data = self.AES.decrypt(data, True)
        data = base64.b64decode(data)
        return data

    def send_frame(self, frame_buffer, clientKey):
        data = base64.b64encode(frame_buffer)
        # the following code commented in the case of Java Client Socket
        # length = str(len(data))
        # self.send_data(length.encode("utf-8"), clientKey)
        self.send_data(data, clientKey)

    def send_frame_encrypted(self, frame_buffer, clientKey):
        data = base64.b64encode(frame_buffer)
        data = self.AES.encrypt(data)
        # the following code commented in the case of Java Client Socket
        length = str(len(data))
        length = length.encode("utf-8")

        self.send_data(length, clientKey)
        self.send_data(b"\n", clientKey)

        # self.send_data_encrypted(length, clientKey)
        # self.send_data("\r\n", clientKey)
        self.send_data(data, clientKey)
        # self.send_data(b"\r\n", clientKey)

    def send_data(self, text_to_send, clientKey):

        # print("Sending [{}], length:{} to {}".format(text_to_send, len(text_to_send), client_name))
        try:
            self.clients[clientKey].send(text_to_send)
        except ConnectionResetError:
            self.ClientConnectionReset(clientKey)
        except ConnectionAbortedError:
            self.ClientConnectionReset(clientKey)
        except ConnectionRefusedError:
            self.ClientConnectionReset(clientKey)
        except KeyError:
            self.ClientConnectionReset(clientKey)

    def send_data_encrypted(self, text_to_send, clientKey):
        self.send_data(self.AES.encrypt(text_to_send), clientKey)

    def ReceiveStopCommand(self, clientKey):
        try:
            data = self.receive_data_encrypted(clientKey)
            if data == self.ShutdownCommand:
                self.StopServer()
                self.stopServer = True
            else:
                print("Client {} sent: {}".format(clientKey, data))
        except Exception:
            print("Failed to decrypt data received from client {}".format(clientKey))

    def Stream(self, clientKey, sleeptime):
        t = Thread(target=self.ReceiveStopCommand, args=(clientKey,))
        t.start()

        while True:
            if self.stopServer:
                # self.close_connection_with_client(clientKey)
                self.cam.release()
                StreamServer.StartedServer = False
                print("end")
                break

            result, frame = self.cam.read()
            result, buffer_data = cv2.imencode('.jpg', frame)
            # print(buffer_data)
            self.send_frame_encrypted(buffer_data, clientKey)
            time.sleep(sleeptime)
            # cam.release()
        exit(0)






