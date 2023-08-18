import requests
import socket
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def gethip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(hostname)
    print(IPAddr)

id_tele = '735055104'
token_bot = '2002443519:AAGdrLRtknB_H0kCG5kaFUco9G8rWTMasSA'

def uch():
    ld = '\033[1;32m'
    f = '\033[1;35m'
    headers = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)',
        'X-CSRFToken': 'TNZhAQCH80aoK8F5oK8F5oZNHJ5ZrKAlSmcMM',
        'X-instagram-AJAX': 'cec4fe0d7efe',
        'X-IG-App-ID': '936619743392459'
    }
    a7rf = "ggeerrttyyuuiiooppllkkjjhhggffdssaazzxxccvvbbnn11223344556677889900....____"
    while True:
        user = str("".join(random.choice(a7rf) for i in range(5)))
        url = f'https://www.instagram.com/{user}/'
        rq = requests.get(url, headers=headers)
        if rq.status_code == 200:
            tlg = f'https://api.telegram.org/bot{token_bot}/sendMessage?chat_id={id_tele}&text=user found: {user}'
            req = requests.post(tlg)
            print('\033[1;36m' " user found :" + user)
        elif rq.status_code == 404:
            print('\x1b[2;31m' + " user not found : " + user)

print(''' \033[31m

          
                                      $$\                         $$\ 
                                      $$ |                        $$ |
$$$$$$$\   $$$$$$\  $$\   $$\       $$$$$$\    $$$$$$\   $$$$$$\  $$ |
$$  __$$\ $$  __$$\ \$$\ $$  |      \_$$  _|  $$  __$$\ $$  __$$\ $$ |
$$ |  $$ |$$ /  $$ | \$$$$  /         $$ |    $$ /  $$ |$$ /  $$ |$$ |
$$ |  $$ |$$ |  $$ | $$  $$<          $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |
$$ |  $$ |\$$$$$$  |$$  /\$$\         \$$$$  |\$$$$$$  |\$$$$$$  |$$ |
\__|  \__| \______/ \__/  \__|         \____/  \______/  \______/ \__|
                                                                      
                                                                      
                                                                      

tool by Nox \033[39m ''')

print('''
       \033[32m [01]\033[39m show my ip & hostname

       \033[32m [02]\033[39m uch

       \033[32m [00]\033[39m about
        ''')

chinput = input('select number:')
if chinput == '1':
    gethip()

elif chinput == '2':
    uch()

elif chinput  == '00' :
    print('''
by Nox 
my telegram : @Noxform
thanks for try my first tool
''')

elif chinput  == '0' :
    print('''
by Nox
my telegram : @Noxform
thanks for try my first tool
''')
