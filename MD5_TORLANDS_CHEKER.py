#-*- coding: utf-8 -*-
import hashlib
import sys
try:
    print ("""
 ███▄ ▄███▓▓█████▄   ██████       ▄▄▄█████▓ ▒█████   ██▀███   ██▓    ▄▄▄       ███▄    █ ▓█████▄   ██████     ▄████▄   ██░ ██  ██ ▄█▀
▓██▒▀█▀ ██▒▒██▀ ██▌▒██    ▒       ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██▒   ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██    ▒    ▒██▀ ▀█  ▓██░ ██▒ ██▄█▒ 
▓██    ▓██░░██   █▌░ ▓██▄         ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌░ ▓██▄      ▒▓█    ▄ ▒██▀▀██░▓███▄░ 
▒██    ▒██ ░▓█▄   ▌  ▒   ██▒      ░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒   ▒▓▓▄ ▄██▒░▓█ ░██ ▓██ █▄ 
▒██▒   ░██▒░▒████▓ ▒██████▒▒        ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒░██████▒▓█   ▓██▒▒██░   ▓██░░▒████▓ ▒██████▒▒   ▒ ▓███▀ ░░▓█▒░██▓▒██▒ █▄
░ ▒░   ░  ░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░        ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▒ ▓▒
░  ░      ░ ░ ▒  ▒ ░ ░▒  ░ ░          ░      ░ ▒ ▒░   ░▒ ░ ▒░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░     ░  ▒    ▒ ░▒░ ░░ ░▒ ▒░
░      ░    ░ ░  ░ ░  ░  ░          ░      ░ ░ ░ ▒    ░░   ░   ░ ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░  ░  ░     ░         ░  ░░ ░░ ░░ ░ 
       ░      ░          ░                     ░ ░     ░         ░  ░     ░  ░         ░    ░          ░     ░ ░       ░  ░  ░░  ░   
            ░                                                                             ░                  ░                       
                                                                                                        
                            [+] Dev : TorlandsArmy
                            [+] Torlands.EmilioM
                            [+] Torlands.AxelVA
                            [+] Torlands.LeonelG
-> Modo de uso : 
$ python torland_bruter.py wordilist.txt hashmd5sdfoihw4tuhtuithwituhwthrtnhturt
    """)
except (KeyboardInterrupt, SystemExit):
	print "\n\t[!] Sesion cancelada"	

c = open(sys.argv[1], 'r+')
l = 0
for i in c:
	l = l + 1
	d = i.split('\n')
	if hashlib.md5(d[0]).hexdigest() == sys.argv[2]:
		print "se encontro la palabra: ", i
		print "se hicieron ", l, "intentos"
		break
	print "se hicieron", l," intentos"
c.close()


