import socket
from SymmetricEncryption import Symmetric
from AsymmetricEncryption import Asymmetric
import time
from threading import Thread


class MainServer:
    AES: Symmetric

    def __init__(self, host, port, buffer_size, clients_sessions, checkPeriod):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.checkPeriod = checkPeriod
        self.clients_sessions = clients_sessions
        clients = dict()
        self.clients = clients

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((self.host, self.port))
        sock.listen(len(self.clients_sessions))

        self.server = sock

        print("Starting The Server ..")
        print("Listening At {}".format(sock.getsockname()))

        # Creating Asymmetric Encryption
        self.RSA = Asymmetric()

        self.stopAcceptClients = False

    def AuthenticateClient(self, client, address):
        if str(address[0]).startswith('192.168.') or str(address[0]).startswith('10.0.') or str(address[0]).startswith(
                '172.16.') or str(address[0]).startswith('127.0.0.1'):
            publicKey = self.RSA.publicKey.export_key()
            # publicKey = publicKey.encode("utf-8")
            # publicKey = self.RSA.getPublicKey()
            # publicKey = base64.b64encode(publicKey)
            try:
                client.send(publicKey)
                AES_key_cipher = client.recv(self.buffer_size)
                # print("Received: {}".format(AES_key_cipher))
                AES_key = self.RSA.decryptionBase64data(AES_key_cipher)
                self.AES = Symmetric(AES_key, AES_key)  # change it if iv is different from the key

                identity = client.recv(self.buffer_size)
                identityDecrypted = self.AES.decrypt(identity, False)
                validUser = False
                for clientSession in self.clients_sessions:
                    clientKeys = clientSession.keys()
                    clientKey = ""
                    for x in clientKeys:
                        clientKey = x
                        break

                    if clientSession[clientKey] == identityDecrypted:
                        self.clients[clientKey] = client
                        self.send_data_encrypted(b"OK", clientKey)
                        validUser = True
                        print("Client At {}:{} connected to the server!".format(address[0], address[1]))
            except ConnectionResetError:
                print("Client At {}:{} reset the connection!".format(address[0], address[1]))
            except ConnectionRefusedError or ConnectionAbortedError or ConnectionError:
                print("Connection Error With Client {}:{}".format(address[0], address[1]))
            except Exception:
                print("Key Exchange Error With Client {}:{}".format(address[0], address[1]))

    def accept_client(self):
        while True:
            if self.stopAcceptClients:
                return
            try:
                client, address = self.server.accept()
                t = Thread(target=self.AuthenticateClient, args=(client, address))
                t.start()
            except OSError:
                print("Couldn't accept the connection as the server has been closed")

    def Connect_To_clients(self):
        print("Connecting to clients ..")
        self.stopAcceptClients = False

        t = Thread(target=self.accept_client)
        t.start()

        numOfClients = len(self.clients_sessions)

        while True:
            if len(self.clients) == numOfClients:
                print("Server has connected to all clients ..")
                self.stopAcceptClients = True
                break

            time.sleep(self.checkPeriod)   # change wait time before checking

    def ClientConnectionReset(self, clientKey):
        del self.clients[clientKey]
        print("Client {} disconnected".format(clientKey))
        time.sleep(1)
        self.Connect_To_clients()

    def setAES(self, AES):
        self.AES = AES

    def receive_data(self, clientKey):
        try:
            received_pi_data = self.clients[clientKey].recv(self.buffer_size)
        except ConnectionResetError:
            self.ClientConnectionReset(clientKey)
        except ConnectionAbortedError:
            self.ClientConnectionReset(clientKey)
        except ConnectionRefusedError:
            self.ClientConnectionReset(clientKey)
        else:
            return received_pi_data

        return b""

    def receive_data_encrypted(self, clientKey):
        data = self.receive_data(clientKey)
        if data == b"":
            return ""

        return self.AES.decrypt(data, False)

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

    def send_data_encrypted(self, text_to_send, clientKey):
        self.send_data(self.AES.encrypt(text_to_send), clientKey)

    def close_connection_with_client(self, client_name):
        print("Closing Connection With Client : {}".format(client_name))
        self.clients[client_name].close()

    def StopServer(self):
        self.stopAcceptClients = True
        # self.server.shutdown(socket.SHUT_WR)
        self.server.close()


