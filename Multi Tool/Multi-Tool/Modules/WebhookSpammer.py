from termcolor import colored
import keyboard
import requests
import subprocess
from dhooks import Webhook
import os
import time
import sys


def start():
    os.system("py Multi-Tool.py")

def clear():
    os.system("cls")

def title():
    os.system("title Made by Bulle212")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


list2 = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]
exitlist = ["Exit", "exit", "close", "Close"]


def mainWS():
    title()
    clear()
    print(colored("""
            
                              ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                              ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                              ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                              ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                              ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                               ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                              ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                              ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                              ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                              ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                              ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                              ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

                                                                                                                  (exit)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""", "light_grey"))

    webhook2 = input("Webhook: ")
    if webhook2 in exitlist:
        start()
    clear()
    print(colored("""
            
                              ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                              ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                              ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                              ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                              ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                               ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                              ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                              ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                              ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                              ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                              ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                              ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

                                                                                                                  (exit)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""", "light_grey"))
    message = input("Message: ")
    if message in exitlist:
        start()
    clear()
    print(colored("""
            
                              ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
                              ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
                              ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
                              ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
                              ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
                               ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

                              ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                              ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                              ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                              ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                              ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                              ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

                                                                                                                  (exit)
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""", "light_grey"))
    delay = input("Delay in second(s): ")

    if delay in exitlist:
        start()



    hook = Webhook(webhook2)

    while True:
                    clear() 

                    
                    print("Hold S to stop spamming...")
                    if keyboard.is_pressed("s"):
                        clear()
                        print("Stopped... Press any key to countinue.\n")
                        time.sleep(2)
                        os.system('pause >NUL')
                        mainWS()
                    hook.send(message)
                    if delay in list2:
                        time.sleep(float(delay))
                    else:
                        time.sleep(int(delay))
    return


if __name__ == "__main__":
    title()
    mainWS()