from termcolor import colored
import subprocess
import pyautogui
import pyperclip
import requests
import time
import sys
import os

sys.path.insert(0, './Modules')
from WebhookSpammer import mainWS
#from VencordInstaller import mainVencord

def title():
    os.system("")

def clear():
    os.system("cls")


hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def printSlow2(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.05)


def main():
    title()
    clear()
    Color()
    main2()



def main2():
    title()
    clear()
    print("""
          
          
                         ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
                         ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                         ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
                         ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
                         ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
                         ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                           
                                                                      
              """)






    print(colored("                     Computer Info                       Discord                         Other                                                          ", "red"))
    print("""             ┌──────────────────────────────┬───────────────────────────────┬──────────────────────────────┐
             │                              │                               │                              │   
             │                              │                               │                              │
             │    1. What's my IP           │    4. Webhook Spammer         │    7. Spicetify installer    │
             │    2. What's my HWID         │                               │    8. Color                  │    
             │    3. What's my Hostname     │                               │    9. Exit                   │
             │                              │                               │                              │
             │                              │                               │                              │
             └──────────────────────────────┴───────────────────────────────┴──────────────────────────────┘""")
    sel2 = input("                                                         Select: ")

    iplist = ["1", "IP", "Ip", "ip", "What's my IP"]
    hwidlist = ["2", "HWID", "Hwid", "hwid", "What's my HWID"]
    hostnamelist = ["3", "Hostname", "hostname", "What's my Hostname", "What's my hostname"]
    spicetifylist = ["Spicetify", "spicetify", "7", "Spicetify installer", "spicetify installer"]
    webhookspammerlist = ["4", "Webhook spammer", "webhook spammer", "Webhook Spammer", "webhook Spammer"]
    #vencordlist = ["5", "Vencord", "Vencord Installer", "vencord", "Vencord installer", "vencord installer"]


    colorlist = ["Color", "color", "8"]


    exit2 = ["Exit", "exit", "9"]



    if sel2 in iplist:
        ip()
    elif sel2 in hwidlist:
        hwid()
    elif sel2 in hostnamelist:
        hostname()
    elif sel2 in spicetifylist:
        spicetify()
    elif sel2 in webhookspammerlist:
        webhookspammer()
    #elif sel2 in vencordlist:
    #    mainVencord()



    elif sel2 in colorlist:
        main()





    elif sel2 == " " or "":
        printSlow2("You can't leave it blank. Sending you back...")
        time.sleep(0.75)
        print("\nPress any key to countinue...")
        os.system('pause >NUL')
        main()







    elif sel2 in exit2:
        clear()
        printSlow("Exiting...")
        time.sleep(0.5)
        clear()
        exit()
    else:
        printSlow2("\nYou have to select something from the list above...")
        time.sleep(0.75)
        print("\nPress any key to countinue...")
        os.system('pause >NUL')
        main2()
    



    if sel2 == "exit" or "Exit":
        exit()
    



def ip():
    ip = requests.get('https://api.ipify.org').text
    clear()
    print("────────────────────────────────────")
    print("This is your IP: ")
    print(ip)
    print("────────────────────────────────────")
    print("\nPress any key to countinue...")
    os.system('pause >NUL')
    main2()


def hwid2():
    os.system("wmic csproduct get uuid")

def hwid():
    clear()
    print("────────────────────────────────────")
    print("This is your HWID: " )
    hwid2()
    print("────────────────────────────────────")
    print("\nPress any key to countinue...")
    os.system('pause >NUL')
    main2()


def hostname():
    clear()
    print("────────────────────────────────────")
    print("This is your Hostname: ")
    os.system("hostname")
    print("────────────────────────────────────")
    print("\nPress any key to countinue...")
    os.system('pause >NUL')
    main2()


def spicetify():
    clear()
    spicetifycmd = "iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1"
    spicetifycomment = "#Right click on the powershell terminal when it is finish typing and then click enter."
    pyperclip.copy(" | iex")
    printSlow("Spicetify installing...")
    os.system("Start powershell")
    time.sleep(1)
    pyautogui.click(500, 500)
    time.sleep(0.5)
    pyautogui.typewrite(spicetifycomment)
    time.sleep(1)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(2.5)
    pyautogui.typewrite(spicetifycmd)
    time.sleep(5)
    main2()


def webhookspammer():
    mainWS()    


def Color():
    clear()
    print("""
          
          
                         ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
                         ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                         ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
                         ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
                         ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
                         ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                           
                                                                      
              """)
    print("""
                                                                  Color
                                        ┌────────────────────────────────────────────────────────┐
                                        │                       1. White                         │
                                        │                       2. Grey                          │
                                        │                       3. Black                         │
                                        │                       4. Yellow                        │
                                        │                       5. Orange                        │
                                        │                       6. Red                           │
                                        │                                                 (Exit) │
                                        └────────────────────────────────────────────────────────┘""")
    colorsel = input("                                                                Select: ")
    colors = ["White", "white", "Grey", "grey", "Black", "black", "Yellow", "yellow", "Orange", "orange", "Red", "red"]
    colornumbers = ["1", "2", "3", "4", "5", "6"]

    if colorsel in colornumbers:
        if colorsel == "1":
            colorsel = "white"
        if colorsel == "2":
            colorsel = "grey"
        if colorsel == "3":
            colorsel = "black"
        if colorsel == "4":
            colorsel = "yellow"
        if colorsel == "5":
            colorsel = "orange"
        if colorsel == "6":
            colorsel = "red"
        clear()
        printSlow("Instalizing color.")
        time.sleep(0.5)
        clear()
        print("Instalizing color..")
        time.sleep(0.5)
        clear()
        print("Instalizing color...")
        time.sleep(1)
        clear()
        main2()

    if colorsel in colors:
        print("Instalizing color.")
        time.sleep(0.2)
        printSlow("Instalizing color..")
        time.sleep(0.2)
        printSlow("Instalizing color...")
        time.sleep(1)
        main2()

    clear()
    if colorsel == "exit" or "Exit":
        exit()













if __name__ == "__main__":
    main2()