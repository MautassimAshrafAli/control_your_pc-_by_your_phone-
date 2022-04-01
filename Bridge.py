from StreamServer import StreamServer
from Server import MainServer
from Sound import Sound
import os
import pygame
import ctypes
from pynput.keyboard import Key, Controller
from threading import Thread
import psutil
import argparse
import win32gui
import webbrowser

dir = os.path.dirname(__file__) #<-- absolute dir the script is in
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
ctypes.windll.kernel32.SetConsoleTitleA("Near Bridge")

pygame.mixer.init()

keyboard = Controller()

def shutdown():
    os.system("shutdown /s /t 1")


def restart():
    os.system("shutdown /r /t 1")


def sleep():

    os.system('powercfg -hibernate on & rundll32.exe powrprof.dll,SetSuspendState Hibernate')


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    
def main():

    #server_host = socket.gethostbyname(socket.gethostname())
    # server_host = "192.168.1.2"
    #server_host = "192.168.0.106"
    server_port = 4000
    server_buffer = 4096
    check_period = 5
    StreamSleepTime = 1
    ShutdownCommand = "Shutdown"
    StreamServerPort = 5000

    clientName = "NearApp"
    Clients = [{clientName: password}]

    print("Main Server")
    print(server_host)
    print(password)

    server = MainServer(server_host, server_port, server_buffer, Clients, check_period)
    server.Connect_To_clients()

    while True:
        try:
            inputData = server.receive_data_encrypted(clientName)
            if inputData == "Camera" and not StreamServer.StartedServer:

                # os.system("python {}".format(StreamServerPath))
                Thread(target=StartStreamServer, args=(Clients, server.AES, server_host, StreamServerPort, server_buffer, check_period, clientName, ShutdownCommand, StreamSleepTime,)).start()

            elif inputData == "Open Google Chrome":
                os.system("cd/ & cd Program Files & cd Google & cd Chrome & cd Application & start chrome.exe")
            elif inputData == "Close Google Chrome":
                PROCNAME = "chrome.exe"
                for proc in psutil.process_iter():
                    # check whether the process name matches
                    if proc.name() == PROCNAME:
                        proc.kill()
            elif inputData == "Open NEAR Browser":
                print("**NEAR Browser**")
                #Your code
                #OR
                #install NEAR Browser link :
                #https://github.com/MutassimAshraf123/Browser
                #os.system("path")
            elif inputData == "Compress NEAR Browser":
                   print("**Compress NEAR Browser**")
                   #Your code
                   #OR
                   #NEAR Browser code
                   #Window = gw.getWindowsWithTitle('Near browser')[0]
                   #Window.minimize()
            elif inputData == "show NEAR Browser":
                   print("**show NEAR Browser**")
                   #Your code
                   #OR
                   #NEAR Browser code
                   #Window = gw.getWindowsWithTitle('Near browser')[0]
                   #Window.activate()  
                   #Window = gw.getWindowsWithTitle('Near browser')[0]
                   #Window.restore()
            elif inputData == "Close NEAR Browser":
                print("**Close NEAR Browser**")
                #Your code
                #OR
                #NEAR Browser code
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open NEAR Wifi":
                print("**Open NEAR Wifi**")
            elif inputData == "Close NEAR Wifi":
                print("**Close NEAR Wifi**")
            elif inputData == "Open NEAR Sound":
                print("**Open NEAR Sound**")
            elif inputData == "Close NEAR Sound":
                print("**Close NEAR Sound**")
            elif inputData == "Open Keyboard":
                os.system("cd/ & start osk")
                #OR
                #install Near Keyboard link :
                #https://github.com/MutassimAshraf123/Near_Keyboard
                #os.system("path")
            elif inputData == "Compress Keyboard":
                print("**Compress Keyboard**")
                #Near Keyboard code
                #Window = gw.getWindowsWithTitle('keyboard_')[0]
                #Window.minimize()
            elif inputData == "Close Keyboard":
                print("**Close Keyboard**")
                #Near Keyboard code
                #PROCNAME = "keyboard_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Calculator":
              print("**Open Calculator**")
              #Near Keyboard code
            elif inputData == "Compress Calculator":
               print("**Compress Calculator**")
            elif inputData == "show Calculator":
                   print("**show Calculator**")
            elif inputData == "Close Calculator":
                print("**Close Calculator**")
            elif inputData == "Open Calendar":
              print("**Open Calendar**")
            elif inputData == "Compress Calendar":
               print("**Compress Calendar**")
            elif inputData == "show Calendar":
                print("**show Calendar**")
            elif inputData == "Close Calendar":
                print("**Close Calendar**")
            elif inputData == "Open Settings":
                print("**Open Settings**")
            elif inputData == "Compress Settings":
               print("**Compress Settings**")
            elif inputData == "show Settings":
                print("**show Settings**")
            elif inputData == "Close Settings":
                print("**Close Settings**")
            elif inputData == "Open Bluetooth":
                print("**Open Bluetooth**")
            elif inputData == "Close Bluetooth":
                print("**Close Bluetooth**")
            elif inputData == "Open Start":
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)
            elif inputData == "Close Start":
                keyboard.press(Key.cmd)
                keyboard.release(Key.cmd)
            elif inputData == "Camera Opened":
                #Your code windows camera
                os.system("start microsoft.windows.camera:")
                #OR
                #insetall NEAR Smart Camera link :
                #https://github.com/MutassimAshraf123/Smart_Camera
                #os.system("path")
            elif inputData == "Take Video":
                print("**Take Video**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("v")
                #keyboard.release("v")
                #keyboard.release(Key.ctrl)
            elif inputData == "Pause Video":
                print("**Pause Video**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("s")
                #keyboard.release("s")
                #keyboard.release(Key.ctrl)
            elif inputData == "Take Photo":
                print("**Take Photo**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("t")
                #keyboard.release("t")
                #keyboard.release(Key.ctrl)
            elif inputData == "Night mode":
                print("**Night mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("n")
                #keyboard.release("n")
                #keyboard.release(Key.ctrl)
            elif inputData == "Black mode":
                print("**Black mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("l")
                #keyboard.release("l")
                #keyboard.release(Key.ctrl)
            elif inputData == "Fire mode":
                print("**Fire mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("f")
                #keyboard.release("f")
                #keyboard.release(Key.ctrl)
            elif inputData == "Normal mode":
                print("**Normal mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("r")
                #keyboard.release("r")
                #keyboard.release(Key.ctrl)
            elif inputData == "text mode":
                print("**text mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("x")
                #keyboard.release("x")
                #keyboard.release(Key.ctrl)
            elif inputData == "Opject mode":
                print("**Opject mode**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("o")
                #keyboard.release("o")
                #keyboard.release(Key.ctrl)
            elif inputData == "Face detection":
                print("**Face detection**")
                #NEAR Smart Camera code
                #keyboard.press(Key.ctrl)
                #keyboard.press("d")
                #keyboard.release("d")
                #keyboard.release(Key.ctrl)
            elif inputData == "camera Close":
                PROCNAME = "WindowsCamera.exe"
                for proc in psutil.process_iter():
                    # check whether the process name matches
                    if proc.name() == PROCNAME:
                        proc.kill()
                #NEAR Smart Camera code
                #PROCNAME = "FaceDetectionAndRecognition.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "camera Compress":
                print("**camera Compress**")
                #NEAR Smart Camera code
                #Window = gw.getWindowsWithTitle('Near Camera')[0]
                #Window.minimize()
            elif inputData == "camera show":
                print("**camera show**")
                #NEAR Smart Camera code
                #Window = gw.getWindowsWithTitle('Near Camera')[0]
                #Window.activate()
                #Window = gw.getWindowsWithTitle('Near Camera')[0]
                #Window.restore()
            elif inputData =="Open My play list":
                 print("**Open My play list**")
                #Your code
                #like open your soundcloud play list
                #OR
                #or install youtube download manager link :
                #https://github.com/MutassimAshraf123/youtube_download_manager
                #then enter the path to open
                #os.system("path")
            elif inputData =="Compress My play list":
                print("**Compress My play list**")
                #Your code
                #OR
                #for compress youtube download manager
                #Window = gw.getWindowsWithTitle('myplaylist')[0]
                #Window.minimize()
            elif inputData =="show My play list":
                print("**show My play list**")
                #Your code
                #OR
                #for show youtube download manager music list
                #Window = gw.getWindowsWithTitle('myplaylist')[0]
                #Window.activate()  
                #Window = gw.getWindowsWithTitle('myplaylist')[0]
                #Window.restore()
            elif inputData == "Close My play list":
                print("**Close My play list**")
                #Your code
                #OR
                #for close youtube download manager
                #PROCNAME = "Youtube_Horn.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "musicPlayer Opened":
                print("**musicPlayer Opened**")
                #Your code

            #set desktop Background
            elif inputData == "Set Background ID: 1":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_1.jpg", 0)
            elif inputData == "Set Background ID: 2":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_2.jpg", 0)
            elif inputData == "Set Background ID: 3":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_27.jpg", 0)
            elif inputData == "Set Background ID: 4":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_7.jpg", 0)
            elif inputData == "Set Background ID: 5":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_9.jpg", 0)
            elif inputData == "Set Background ID: 6":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_10.jpg", 0)
            elif inputData == "Set Background ID: 7":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_11.jpg", 0)
            elif inputData == "Set Background ID: 8":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_12.jpg", 0)
            elif inputData == "Set Background ID: 9":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_13.jpg", 0)
            elif inputData == "Set Background ID: 10":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_15.jpg", 0)
            elif inputData == "Set Background ID: 11":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_16.jpg", 0)
            elif inputData == "Set Background ID: 12":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/m4.png", 0)
            elif inputData == "Set Background ID: 13":
                ctypes.windll.user32.SystemParametersInfoW(20, 0, dir+"/wallpaper/image_37.jpg", 0)

            elif inputData == "Shutdown":
                shutdown()
            elif inputData == "Sleep":
                sleep()
            elif inputData == "Restart":
                restart()

            elif inputData == "Open Whatsapp":
                webbrowser.open('https://web.whatsapp.com/')
                #OR
                #Code Near browser
                #os.system("path https://web.whatsapp.com/")
            elif inputData == "Compress Whatsapp":
              print("**Compress Whatsapp**")
              #Code Near browser
              #Window = gw.getWindowsWithTitle('Near browser')[0]
              #Window.minimize()   
            elif inputData == "Close Whatsapp":
                print("**Close Whatsapp**")
                #OR
                #Code Near browser
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Facebook":
                webbrowser.open('https://www.facebook.com/')
                #OR
                #Code Near browser
                #os.system("path https://www.facebook.com/")
            elif inputData == "Compress Facebook":
              print("**Compress Facebook**")
              #Window = gw.getWindowsWithTitle('Near browser')[0]
              #Window.minimize()
            elif inputData == "Close Facebook":
                print("**Close Facebook**")
                #Code Near browser
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Messenger":
                webbrowser.open('https://www.messenger.com/')
                #OR
                #Code Near browser
                #os.system("path https://www.messenger.com/")
            elif inputData == "Compress Messenger":
               print("**Compress Messenger**")
               #Window = gw.getWindowsWithTitle('Near browser')[0]
               #Window.minimize()
            elif inputData == "Close Messenger":
                print("**Close Messenger**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Instgram":
               webbrowser.open('https://www.instagram.com/?hl=en')
               #OR
               #Code Near browser
               #os.system("path https://www.instagram.com/?hl=en")
            elif inputData == "Compress Instgram":
               print("**Compress Instgram**")
               #Window = gw.getWindowsWithTitle('Near browser')[0]
               #Window.minimize()
            elif inputData == "Close Instgram":
                print("**Close Instgram**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Youtube":
                webbrowser.open('https://www.youtube.com/')
                #OR
                #Code Near browser
                #os.system("path https://www.youtube.com/")
            elif inputData == "Compress Youtube":
               print("**Compress Youtube**")
               #Window = gw.getWindowsWithTitle('Near browser')[0]
               #Window.minimize()
            elif inputData == "Close Youtube":
                print("**Close Youtube**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open SoundCloud":
                 webbrowser.open('https://soundcloud.com/')
                 #OR
                 #Code Near browser
                 #os.system("path https://soundcloud.com/")
            elif inputData == "Compress SoundCloud":
               print("**Compress SoundCloud**")
               #Window = gw.getWindowsWithTitle('Near browser')[0]
               #Window.minimize()
            elif inputData == "Close SoundCloud":
                print("**Close SoundCloud**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open G-mail":
                webbrowser.open('https://www.google.com/gmail/')
                #OR
                #Code Near browser
                #os.system("path https://www.google.com/gmail/")
            elif inputData == "Compress G-mail":
               print("**Compress G-mail**")
               #Window = gw.getWindowsWithTitle('Near browser')[0]
               #Window.minimize()
            elif inputData == "Close G-mail":
                print("**Close G-mail**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()
            elif inputData == "Open Twitter":
                webbrowser.open('https://twitter.com/')
                #OR
                #Code Near browser
                #os.system("path https://twitter.com/")
            elif inputData == "Compress Twitter":
              print("**Compress Twitter**")
              #Window = gw.getWindowsWithTitle('Near browser')[0]
              #Window.minimize()
            elif inputData == "Close Twitter":
                print("**Close Twitter**")
                #PROCNAME = "we_browser_.exe"
                #for proc in psutil.process_iter():
                #    # check whether the process name matches
                #    if proc.name() == PROCNAME:
                #        proc.kill()

            #set windows sound volume
            elif inputData == "Volume: 0":
                Sound.volume_set(0)
            elif inputData == "Volume: 1":
                Sound.volume_set(1)
            elif inputData == "Volume: 2":
                Sound.volume_set(2)
            elif inputData == "Volume: 3":
                Sound.volume_set(3)
            elif inputData == "Volume: 4":
                Sound.volume_set(4)
            elif inputData == "Volume: 5":
                Sound.volume_set(0)
                Sound.mute()
                Sound.volume_set(5)
            elif inputData == "Volume: 6":
                Sound.volume_set(6)
            elif inputData == "Volume: 7":
                Sound.volume_set(7)
            elif inputData == "Volume: 8":
                Sound.volume_set(8)
            elif inputData == "Volume: 9":
                Sound.volume_set(9)
            elif inputData == "Volume: 10":
                Sound.volume_set(10)
            elif inputData == "Volume: 11":
                Sound.volume_set(11)
            elif inputData == "Volume: 12":
                Sound.volume_set(12)
            elif inputData == "Volume: 13":
                Sound.volume_set(13)
            elif inputData == "Volume: 14":
                Sound.volume_set(14)
            elif inputData == "Volume: 15":
                Sound.volume_set(15)
            elif inputData == "Volume: 16":
                Sound.volume_set(16)
            elif inputData == "Volume: 17":
                Sound.volume_set(17)
            elif inputData == "Volume: 18":
                Sound.volume_set(81)
            elif inputData == "Volume: 19":
                Sound.volume_set(19)
            elif inputData == "Volume: 20":
                Sound.volume_set(20)
            elif inputData == "Volume: 21":
                Sound.volume_set(21)
            elif inputData == "Volume: 22":
                Sound.volume_set(22)
            elif inputData == "Volume: 23":
                Sound.volume_set(23)
            elif inputData == "Volume: 24":
                Sound.volume_set(24)
            elif inputData == "Volume: 25":
                Sound.volume_set(25)
            elif inputData == "Volume: 26":
                Sound.volume_set(26)
            elif inputData == "Volume: 27":
                Sound.volume_set(27)
            elif inputData == "Volume: 28":
                Sound.volume_set(28)
            elif inputData == "Volume: 29":
                Sound.volume_set(29)
            elif inputData == "Volume: 30":
                Sound.volume_set(30)
            elif inputData == "Volume: 31":
                Sound.volume_set(31)
            elif inputData == "Volume: 32":
                Sound.volume_set(32)
            elif inputData == "Volume: 33":
                Sound.volume_set(33)
            elif inputData == "Volume: 34":
                Sound.volume_set(34)
            elif inputData == "Volume: 35":
                Sound.volume_set(35)
            elif inputData == "Volume: 36":
                Sound.volume_set(36)
            elif inputData == "Volume: 37":
                Sound.volume_set(37)
            elif inputData == "Volume: 38":
                Sound.volume_set(38)
            elif inputData == "Volume: 39":
                Sound.volume_set(39)
            elif inputData == "Volume: 40":
                Sound.volume_set(40)
            elif inputData == "Volume: 41":
                Sound.volume_set(41)
            elif inputData == "Volume: 42":
                Sound.volume_set(42)
            elif inputData == "Volume: 43":
                Sound.volume_set(43)
            elif inputData == "Volume: 44":
                Sound.volume_set(44)
            elif inputData == "Volume: 45":
                Sound.volume_set(45)
            elif inputData == "Volume: 46":
                Sound.volume_set(46)
            elif inputData == "Volume: 47":
                Sound.volume_set(47)
            elif inputData == "Volume: 48":
                Sound.volume_set(48)
            elif inputData == "Volume: 49":
                Sound.volume_set(49)
            elif inputData == "Volume: 50":
                Sound.volume_set(50)
            elif inputData == "Volume: 51":
                Sound.volume_set(51)
            elif inputData == "Volume: 52":
                Sound.volume_set(52)
            elif inputData == "Volume: 53":
                Sound.volume_set(53)
            elif inputData == "Volume: 54":
                Sound.volume_set(54)
            elif inputData == "Volume: 55":
                Sound.volume_set(55)
            elif inputData == "Volume: 56":
                Sound.volume_set(56)
            elif inputData == "Volume: 57":
                Sound.volume_set(57)
            elif inputData == "Volume: 58":
                Sound.volume_set(58)
            elif inputData == "Volume: 59":
                Sound.volume_set(59)
            elif inputData == "Volume: 60":
                Sound.volume_set(60)
            elif inputData == "Volume: 61":
                Sound.volume_set(61)
            elif inputData == "Volume: 62":
                Sound.volume_set(62)
            elif inputData == "Volume: 63":
                Sound.volume_set(63)
            elif inputData == "Volume: 64":
                Sound.volume_set(64)
            elif inputData == "Volume: 65":
                Sound.volume_set(65)
            elif inputData == "Volume: 66":
                Sound.volume_set(66)
            elif inputData == "Volume: 67":
                Sound.volume_set(67)
            elif inputData == "Volume: 68":
                Sound.volume_set(68)
            elif inputData == "Volume: 69":
                Sound.volume_set(69)
            elif inputData == "Volume: 70":
                Sound.volume_set(70)
            elif inputData == "Volume: 71":
                Sound.volume_set(71)
            elif inputData == "Volume: 72":
                Sound.volume_set(72)
            elif inputData == "Volume: 73":
                Sound.volume_set(73)
            elif inputData == "Volume: 74":
                Sound.volume_set(74)
            elif inputData == "Volume: 75":
                Sound.volume_set(75)
            elif inputData == "Volume: 76":
                Sound.volume_set(76)
            elif inputData == "Volume: 77":
                Sound.volume_set(77)
            elif inputData == "Volume: 78":
                Sound.volume_set(78)
            elif inputData == "Volume: 79":
                Sound.volume_set(79)
            elif inputData == "Volume: 80":
                Sound.volume_set(80)
            elif inputData == "Volume: 81":
                Sound.volume_set(81)
            elif inputData == "Volume: 82":
                Sound.volume_set(82)
            elif inputData == "Volume: 83":
                Sound.volume_set(83)
            elif inputData == "Volume: 84":
                Sound.volume_set(84)
            elif inputData == "Volume: 85":
                Sound.volume_set(85)
            elif inputData == "Volume: 86":
                Sound.volume_set(86)
            elif inputData == "Volume: 87":
                Sound.volume_set(87)
            elif inputData == "Volume: 88":
                Sound.volume_set(88)
            elif inputData == "Volume: 89":
                Sound.volume_set(89)
            elif inputData == "Volume: 90":
                Sound.volume_set(90)
            elif inputData == "Volume: 91":
                Sound.volume_set(91)
            elif inputData == "Volume: 92":
                Sound.volume_set(92)
            elif inputData == "Volume: 93":
                Sound.volume_set(93)
            elif inputData == "Volume: 94":
                Sound.volume_set(94)
            elif inputData == "Volume: 95":
                Sound.volume_set(95)
            elif inputData == "Volume: 96":
                Sound.volume_set(96)
            elif inputData == "Volume: 97":
                Sound.volume_set(97)
            elif inputData == "Volume: 98":
                Sound.volume_set(98)
            elif inputData == "Volume: 99":
                Sound.volume_set(99)
            elif inputData == "Volume: 100":
                Sound.volume_max()

            #mobile keyboard
            elif inputData == "key_0":

                keyboard.press("0")
                keyboard.release("0")

            elif inputData == "key_1":

                keyboard.press("1")
                keyboard.release("1")

            elif inputData == "key_2":

                keyboard.press("2")
                keyboard.release("2")

            elif inputData == "key_3":

                keyboard.press("3")
                keyboard.release("3")   

            elif inputData == "key_4":

                keyboard.press("4")
                keyboard.release("4")

            elif inputData == "key_5":

                keyboard.press("5")
                keyboard.release("5")

            elif inputData == "key_6":

                keyboard.press("6")
                keyboard.release("6")

            elif inputData == "key_7":

                keyboard.press("7")
                keyboard.release("7")  

            elif inputData == "key_8":

                keyboard.press("8")
                keyboard.release("8")  

            elif inputData == "key_9":

                keyboard.press("9")
                keyboard.release("9")

            elif inputData == "key_q":
 
                keyboard.press("q")
                keyboard.release("q")

            elif inputData == "key_w":

                keyboard.press("w")
                keyboard.release("w")

            elif inputData == "key_e":

                keyboard.press("e")
                keyboard.release("e")

            elif inputData == "key_r":

                keyboard.press("r")
                keyboard.release("r")   

            elif inputData == "key_t":

                keyboard.press("t")
                keyboard.release("t")

            elif inputData == "key_y":

                keyboard.press("y")
                keyboard.release("y")

            elif inputData == "key_u":

                keyboard.press("u")
                keyboard.release("u")

            elif inputData == "key_i":

                keyboard.press("i")
                keyboard.release("i")  

            elif inputData == "key_o":

                keyboard.press("o")
                keyboard.release("o")  

            elif inputData == "key_p":

                keyboard.press("p")
                keyboard.release("p")

            elif inputData == "key_a":

                keyboard.press("a")
                keyboard.release("a")

            elif inputData == "key_s":

                keyboard.press("s")
                keyboard.release("s")

            elif inputData == "key_d":

                keyboard.press("d")
                keyboard.release("d")

            elif inputData == "key_f":

                keyboard.press("f")
                keyboard.release("f")   

            elif inputData == "key_g":

                keyboard.press("g")
                keyboard.release("g")

            elif inputData == "key_h":

                keyboard.press("h")
                keyboard.release("h")

            elif inputData == "key_j":

                keyboard.press("j")
                keyboard.release("j")

            elif inputData == "key_k":

                keyboard.press("k")
                keyboard.release("k")  

            elif inputData == "key_l":

                keyboard.press("l")
                keyboard.release("l")  

            elif inputData == "key_z":

                keyboard.press("z")
                keyboard.release("z") 

            elif inputData == "key_x":
            
                keyboard.press("x")
                keyboard.release("x")

            elif inputData == "key_c":

                keyboard.press("c")
                keyboard.release("c")

            elif inputData == "key_v":

                keyboard.press("v")
                keyboard.release("v")

            elif inputData == "key_b":

                keyboard.press("b")
                keyboard.release("b")   

            elif inputData == "key_n":

                keyboard.press("n")
                keyboard.release("n")

            elif inputData == "key_m":

                keyboard.press("m")
                keyboard.release("m")

      #===================================caps=======================================================

            elif inputData == "key_Q":
 
                keyboard.press("Q")
                keyboard.release("Q")

            elif inputData == "key_W":

                keyboard.press("W")
                keyboard.release("W")

            elif inputData == "key_E":

                keyboard.press("E")
                keyboard.release("E")

            elif inputData == "key_R":

                keyboard.press("R")
                keyboard.release("R")   

            elif inputData == "key_T":

                keyboard.press("T")
                keyboard.release("T")

            elif inputData == "key_Y":

                keyboard.press("Y")
                keyboard.release("Y")

            elif inputData == "key_U":

                keyboard.press("U")
                keyboard.release("U")

            elif inputData == "key_I":

                keyboard.press("I")
                keyboard.release("I")  

            elif inputData == "key_O":

                keyboard.press("O")
                keyboard.release("O")  

            elif inputData == "key_P":

                keyboard.press("P")
                keyboard.release("P")

            elif inputData == "key_A":

                keyboard.press("A")
                keyboard.release("A")

            elif inputData == "key_S":

                keyboard.press("S")
                keyboard.release("S")

            elif inputData == "key_D":

                keyboard.press("D")
                keyboard.release("D")

            elif inputData == "key_F":

                keyboard.press("F")
                keyboard.release("F")   

            elif inputData == "key_G":

                keyboard.press("G")
                keyboard.release("G")

            elif inputData == "key_H":

                keyboard.press("H")
                keyboard.release("H")

            elif inputData == "key_J":

                keyboard.press("J")
                keyboard.release("J")

            elif inputData == "key_K":

                keyboard.press("K")
                keyboard.release("K")  

            elif inputData == "key_L":

                keyboard.press("L")
                keyboard.release("L")  

            elif inputData == "key_Z":

                keyboard.press("Z")
                keyboard.release("Z") 

            elif inputData == "key_X":
                
                keyboard.press("X")
                keyboard.release("X")

            elif inputData == "key_C":

                keyboard.press("C")
                keyboard.release("C")

            elif inputData == "key_V":

                keyboard.press("V")
                keyboard.release("V")

            elif inputData == "key_B":

                keyboard.press("B")
                keyboard.release("B")   

            elif inputData == "key_N":

                keyboard.press("N")
                keyboard.release("N")

            elif inputData == "key_M":

                keyboard.press("M")
                keyboard.release("M")
                
   #===========================================SSSSSS============================================

            elif inputData == "key_!":

                keyboard.press("!")
                keyboard.release("!")

            elif inputData == "key_@":

                keyboard.press("@")
                keyboard.release("@")

            elif inputData == "key_#":

                keyboard.press("#")
                keyboard.release("#")

            elif inputData == "key_$":

                keyboard.press("$")
                keyboard.release("$")   

            elif inputData == "key_%":

                keyboard.press("%")
                keyboard.release("%")

            elif inputData == "key_^":

                keyboard.press("^")
                keyboard.release("^")

            elif inputData == "key_&":

                keyboard.press("&")
                keyboard.release("&")

            elif inputData == "key_*":

                keyboard.press("*")
                keyboard.release("*")  

            elif inputData == "key_(":

                keyboard.press("(")
                keyboard.release("(")  

            elif inputData == "key_)":

                keyboard.press(")")
                keyboard.release(")")

            elif inputData == "key_-":
 
                keyboard.press("-")
                keyboard.release("-")

            elif inputData == "key__":

                keyboard.press("_")
                keyboard.release("_")

            elif inputData == "key_=":

                keyboard.press("=")
                keyboard.release("=")

            elif inputData == "key_+":

                keyboard.press("+")
                keyboard.release("+")   

            elif inputData == "key_[":

                keyboard.press("[")
                keyboard.release("[")

            elif inputData == "key_]":

                keyboard.press("]")
                keyboard.release("]")

            elif inputData == "key_{":

                keyboard.press("{")
                keyboard.release("{")

            elif inputData == "key_}":

                keyboard.press("}")
                keyboard.release("}")  

            elif inputData == "key_":

                keyboard.press("\\")
                keyboard.release("\\")  

            elif inputData == "key_|":

                keyboard.press("|")
                keyboard.release("|")

            elif inputData == "key_;":

                keyboard.press(";")
                keyboard.release(";")

            elif inputData == "key_:":

                keyboard.press(":")
                keyboard.release(":")

            elif inputData == "char_s":

                keyboard.press("\'")
                keyboard.release("\'")

            elif inputData == "key_<":

                keyboard.press("<")
                keyboard.release("<")   

            elif inputData == "key_.":

                keyboard.press(".")
                keyboard.release(".")

            elif inputData == "key_>":

                keyboard.press(">")
                keyboard.release(">")

            elif inputData == "key_/":

                keyboard.press("/")
                keyboard.release("/")

            elif inputData == "key_?":

                keyboard.press("?")
                keyboard.release("?")  

            elif inputData == "key_\"":

                keyboard.press("\"")
                keyboard.release("\"")  

            elif inputData == "key_`":

                keyboard.press("`")
                keyboard.release("`") 

            elif inputData == "key_~":
                
                keyboard.press("~")
                keyboard.release("~")

   #==========================================del=============================================
            
            elif inputData == "key_del":
                
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)

   #=============================================space=============================================
            elif inputData == "key_space":
        
                keyboard.press(Key.space)
                keyboard.release(Key.space)
   #=============================================enter=============================================
            elif inputData == "key_enter":

                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

            print("Client {} sent: {}".format(clientName, inputData))
            if inputData == "":
                server.close_connection_with_client(clientName)
                server.ClientConnectionReset(clientName)

        except Exception:
            print("Failed to decrypt data received from client {}".format(clientName))
            print("Reset Connection With Client {}".format(clientName))
            server.close_connection_with_client(clientName)
            server.ClientConnectionReset(clientName)

def StartStreamServer(clients, aes, server_host, server_port, buffer, CheckPeriod, clientName, ShutdownCommand, sleeptime):

    streamServer = StreamServer(server_host, server_port, clients, buffer, aes, CheckPeriod, ShutdownCommand)
    streamServer.Connect_To_clients()
    try:
        streamServer.Stream(clientName, sleeptime)
    except Exception:
        print("Stream Server Reset Connection")
        streamServer.StopServer()

if __name__ == '__main__':
    
    parse = argparse.ArgumentParser()
    parse.add_argument("ip", help="ip")
    parse.add_argument("pass_")

    arg = parse.parse_args()
    server_host = arg.ip
    password = arg.pass_

    main()
