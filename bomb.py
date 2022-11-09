import pyautogui as gui
import time
import pyfiglet 
import colorama
import time
from colorama import*
text=pyfiglet.figlet_format("sms bomber ") 
print(Fore.GREEN+text)
print(Fore.GREEN+"                      BY SR12BD")
cont=input("press enter to continue:")
print("******************************************")
time.sleep(0.5)
print("connecting...........")
time.sleep(3)
print("open whatsapp, click on the contact you want to bomb")
time.sleep(2)
print("============================================")
print("")
cont=input("press enter to continue:")
print("connecting once more...........")
time.sleep(4)
print("=============================================")
num=input(Fore.BLUE+"[+] Number of messages")
mes=input(Fore.BLUE+"[+] Enter your message")
time.sleep(2)
for i in range (int(num)):
    gui.typewrite(mes)
    gui.press('enter')
