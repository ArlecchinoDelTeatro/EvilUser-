import requests
import bs4
import os
import time

green = '\033[92m'
end = '\033[0m'
grey = '\033[37m'
red = '\033[91m'

os.system("clear")
print("")
print(red+"  ╔"+red+"["+green+"Arlecchino"+red+"]"+red+"══❥"+" Type server and port")

def admin():
    admin = input("  ╚════❥ ")
    url = requests.get("http://monitor.sacnr.com/checker.html?" + admin)
    soup = bs4.BeautifulSoup(url.text,"lxml")
    hi = soup.select("tr")
    for i,o in hi:
        print(red +"   [" + green + "✥"+ red + "]" + " EvilUser : " + i.text + green + " " + o.text)
admin()
print("")
print(red+"  ╔"+red+"["+green+"Arlecchino"+red+"]"+red+"══❥"+" Wait ")
print(red+"  ╚"+red+"["+green+"Icey"+red+"]"+red+"══❥"+" I will redirect you")
print("")
time.sleep(7)

os.system("python3.6 EvilUser.py")
