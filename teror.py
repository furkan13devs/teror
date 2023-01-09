
import os
import sys
import requests
from googlesearch import search


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white

version = '1.4'

def banner():
	os.system('clear')
	banner = r'''
_____   _____   ____     ___    ____  
|_   _| | ____| |  _ \   / _ \  |  _ \ 
  | |   |  _|   | |_) | | | | | | |_) |
  | |   | |___  |  _ <  | |_| | |  _ < 
  |_|   |_____| |_| \_\  \___/  |_| \_\
                                       
'''
	print(G + banner + W + '\n')
	print(G + '[>] ' + R + 'BY CODED : ' + W + 'SWANTEX')
	print(G + '[>] ' + R + 'Version : ' + W + version)

def cardpwn():
	urls = []
	qlist = []
	total_url = []
	paste_sites = ['cl1p.net', 'dpaste', 'dumpz.org', 'hastebin', 'ideone', 'pastebin', 'pw.fabian-fingerle.de','gist.github.com','https://www.heypasteit.com/','ivpaste.com','mysticpaste.com','paste.org.ru','paste2.org','sebsauvage.net/paste/','slexy.org','squadedit.com','wklej.se','textsnip.com']
	card = input(G + '[+] ' + R +'kart mumarası girin. -> ' + W)
	try:
		val = int(card)
		if len(str(val)) >= 12 and len(str(val)) <= 19:
			for site in paste_sites:
				query = '{} {}'.format(site, card)
				qlist.append(query)
			for entry in qlist:
				for url in search(entry, pause=2.0, stop=20, user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'):
					urls.append(url)

			print('\n' + G + '[>]' + R + ' DÖKÜMLER TOPLANIYOR...' + W + '\n')
			for item in urls:
				for site in paste_sites:
					if '{}'.format(site) in item:
						print(G + '[+] ' + C + item + W)
						total_url.append(item)

		else:
			print('\n' + R + '[!] ' + G + 'HATALI KART NUMARASI' + W + '\n')
			return cardpwn()
		total = len(total_url)
		if total == 0:
			print (R + '[-] BU KART NUMARASI İÇİN AÇIK SIZINTI BULUNAMADI.' + W + '\n')
		else:
			print('\n' + G + '[+]' + R + ' TOPLAM DÖKÜM BULUNTULARI : ' + W + str(total) + '\n')

	except ValueError:
		print('\n' + R + '[!] HATALI KART NUMARASI GİRİLDİ...' + W + '\n')


def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print ('\n' + G + '[+]' + R + ' İNTERNET BAĞLANTISI KONTROL EDİLİYOR...' + W, end = '')
		print (G + ' ÇALIŞIYOR' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + R + ' İNTERNET BAĞLANTISI KURULAMADI... ÇIKIŞ YAPILIYOR...' + W)
		sys.exit()

try:
	banner()
	network()
	cardpwn()
except KeyboardInterrupt:
	print ('\n' + R + '[!]' + R + ' KLAVYE KESİNTİSİ.' + W)
	exit()
