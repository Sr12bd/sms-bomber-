import pyautogui as gui
import time
import pyfiglet 
import colorama
import time
import os
from colorama import*
text=pyfiglet.figlet_format("sms bomber ") 
print(Fore.GREEN+text)
print(Fore.GREEN+"                      BY SR12BD")
print("******************************************")
time.sleep(0.5)
print("connecting")
time.sleep(3)
print("open whatsapp, click on the contact you want to bomb")
time.sleep(2)
print("============================================")
print("")

num=input("Number of messages")
mes=input("Enter your message")
time.sleep(2)
for i in range (int(num)):
    gui.typewrite(mes)
    gui.press('enter')

emu=input("type X to update to latest verstion")
if emu!= "x":
    import pyautogui as gui
import time
import pyfiglet 
import colorama
import time
import os
from colorama import*
text=pyfiglet.figlet_format("sms bomber ") 
print(Fore.GREEN+text)
print(Fore.GREEN+"                      BY SR12BD")
print("******************************************")
time.sleep(0.5)
print("connecting")
time.sleep(3)
print("open whatsapp, click on the contact you want to bomb")
time.sleep(2)
print("============================================")
print("")

num=input("Number of messages")
mes=input("Enter your message")
time.sleep(2)
for i in range (int(num)):
    gui.typewrite(mes)
    gui.press('enter')
if emu == "X":
  print(Fore.GREEN + "Updating Ip Tracker")
os.system("""
    cd
    rm -f -r Ip-Tracker
    git clone https://github.com/Sr12bd/sms-bomber-.git
            
    """)
            
print(Fore.BLUE + """Now type the following command
            cd $HOME
            cd Ip-Tracker
            python3 tracker.py
            """)
exit()
