# Subdomain enumerate tool, V1.0 *
# Made by Adkali with love *
# A tool for Penetration tester during there engagement.
# An OSINT tool with the use of enumerate site, using scraping and parsing.
# Use it for education purpose only.
# --------------------------------------------------------------

# MIT License
# Copyright (c) 2022 Adkali

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import argparse
import whois
import json
import os


# --Defined colors--
def Code_Colors():
    global Yellow, Red, Normal, BM, Green, Gray
    Yellow = "\033[1;33;40m"
    Red = "\033[1;31;40m"
    Normal = "\033[0;0m"
    BM = "\033[1;35;40m"
    Green = "\033[1;32;40m"
    Gray = "\033[1;30;40m"


Code_Colors()


# --Banner printing--
def BannerPrint():
    print(f'''
 _____       _                                    
/  ___|     | | [use '-h' for more help]                                  
\ `--. _   _| |____  _____ _ __  _   _ _ __ ___   
 `--. \ | | | '_ \ \/ / _ \ '_ \| | | | '_ ` _ \  
/\__/ / |_| | |_) >  <  __/ | | | |_| | | | | | | 
\____/ \__,_|_.__/_/\_\___|_| |_|\__,_|_| |_| |_| 

 {Yellow}A{Normal}d{Red}k{Normal}a{BM}l{Normal}i - SubDomain Enumerate T00l

    ''')


BannerPrint()


# --Manually error message for args--
def ParserErros(errmsg):
    print("[!] Syntax Error!")
    print(
        "Usage: python3 [ Script/Name ] -w [File] -d [http://Domain.com]\nFor more information about, use '-h' flag please.")
    exit()


# ---------- ARGS TO BE DEFINED AND GETTING INTERCATS WITH USING THE CODE'S FLAGS ----------

parser = argparse.ArgumentParser(description="Subdomain enumerate using 'whois'/TXT.list/crt/Ved")
parser.error = ParserErros
parser.add_argument('-d', '-domain', type=str, required=True, help='Domain URL, Example: http://example.com')
parser.add_argument('-w', '-word', type=str, required=True, help="Wordlist Path.")
parser.add_argument('-v', '-version', type=str, required=False, help="Subxanum, Version 1.0 Made By Adkali.")
parser.add_argument('-t', '-time', default=0, type=str, nargs='?', required=False,
                    help="Time in each request  for enumerate subdomains.")
parser.add_argument('-i', '-info', type=str, required=False, help="Use 'whois' for more info about the target.")
parser.add_argument('-c', '-crt', required=False, help="scrap subdomains from crt.sh data")
parser.add_argument('-x', '-xed', required=False, help="scarp subdomains using Vedbex data ")
args = parser.parse_args()


# ---------- INFO ABOUT FLAGS AND DEFINED THEM USING VAR ----------

def Operators_Use():
    global domain, wordlist, time_s, who_is, crtsh, ved
domain = args.d
wordlist = args.w
time_s = int(args.t)
who_is = args.i
crtsh = args.c
ved = args.x


Operators_Use()

# ---------- WHEN USING -C FLAG OPTION ('crt'), GET A LIST OF *. AND NONE ----------

sublist = []

# ---------- SPLIT DOMAIN, CUT OFF "http:// FOR THE SUBDOMAIN ----------

d = domain.split("http://")

# ---------- Open specified file using the --word for the specified file ----------

try:
    SubList = open(args.w)
except FileNotFoundError:
    print(f"[!] {Red}Error:{Normal} >> File Doesn't exist...\nUsage Example: '/home/user/Desktop/directory/file.txt'")
    exit()

# ---------- AFTER CHECK, CONTINUE THE CODE ----------

SubList2 = SubList.read()
res = requests.get(f"{domain}")
# ---------- Response 200 ----------
 # ---------- IF IT DOES, CONTINUE THE CODE ----------
if res.status_code == 200:
    try:
        if who_is == "whois":
            who = input("Do you want to use 'Whois' for more information? Y/N: ").lower()
            if who == "y" or who == "yes":
                file = open("Whois_Info", "w")
                file.write(str(whois.whois(domain)))
                file.close()
                print(f"\n[+] >> {Green}'Whois_Info'{Normal} file has been created, continue...")
                print(f"{Red}---{Normal}" * 9)
                time.sleep(3)
            else:
                print(
                    f"{Red}Note:{Normal} >> Continue without 'Whois' information about {args.d}.\nFor more information and help, Use '-h' flag.\n")
                pass
                time.sleep(3)
        else:
            print(f"{Red}Note:{Normal} >> Continue without  -i('Whois') flag")
            time.sleep(1)

        if crtsh == "crt":
            print("[+] scrap subdomains from crt using json with splits...")
            print(f"{Red}---{Normal}" * 9)
            url = f"https://crt.sh/?q={d[1]}&output=json"
            r = requests.get(url)
            c = r.content.decode("UTF-8")
            J_data = json.loads(c)
            for i in range(len(J_data)):
                N_value = J_data[i]["name_value"]
                if N_value.find("\n"):
                    Subdomains = N_value.split("\n")
                    for Subdomains in Subdomains:
                        if Subdomains.find("*"):
                            if Subdomains not in sublist:
                                sublist.append(Subdomains)
            for i in sublist:
                print(f"Possible results from crt: {i}")
                time.sleep(0.1)
                os.system(f"echo {i} >> crtlist.txt")
            print(f"{Red}---{Normal}" * 9)
            time.sleep(3)
                    
        else:
            print(f"{Red}Note:{Normal} >> Continue without  -c('crt') flag")
            pass
            time.sleep(1)

        if ved == "ved":
            headers = {
                
                "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582",
                "Method": "GET"
            }


            def VedEnum():
                r = requests.get(f"https://www.vedbex.com/subdomain-finder/{d[1]}", headers=headers)
                soup = BeautifulSoup(r.content, 'html.parser').find_all('td')
                for link in soup:
                    split_1 = str(link).split("<td>")[1]
                    if f'{d[1]}' in split_1:
                        split_2 = split_1.split("</td>")[0]
                        print(f"Possible results from Ved: {split_2}")
                        time.sleep(0.1)
                        os.system(f"echo {split_2} >> Vedlist.txt")
                print(f"{Red}---{Normal}" * 9)


            VedEnum()

        else:
            print(f"{Red}Note:{Normal} >> Continue without  -x('ved') flag")
            pass
            time.sleep(1)

    except TimeoutError:
        print("Timeout...Exit!")

    except KeyboardInterrupt:
        print("User stopped process, abort....")
        exit(0)

    except ConnectionError as e:
        print(e)

    except:
        pass

# ---------- SHOULD THE CODE CONTINUE? ( Ask user ) ----------

progress = input(f"Continue run by {args.w}? type Y/N: ")
if progress == "N" or progress == "n" or progress == "no":
    print("Exit...")
    exit()
else:
    # -- Make nice dots for continue code--
    print("\n")
    for _ in range(2):
        for x in range(4):
            string = "Please wait" + ">" * x + ""
            print(string, end="\r")
            time.sleep(0.8)
    print("\n")
    # ---------- Continue ----------
    print(f"\n[+] >> Status: () {Yellow}Successful HTTP requests!{Normal}")
    time.sleep(2)
    print(f"[+] >> Date and time: {datetime.now()}\n")
    time.sleep(2)
    print(f"[+] >> {BM}File loaded: () {args.w}{Normal}\n")
    time.sleep(2)
    sub_split = SubList2.splitlines()
    print(f"[!] >> {Red}Warning:{Normal} () File {args.w} contains {len(sub_split)} Subdomains words.\n")
    time.sleep(2)
    res = requests.get(f"{domain}")
    if res.status_code == 200:
        print(f"[?] >> {Green}Mode:{Normal} () Starting enumerate subdomains on {domain}, Please Wait...")
        print(f"{Red}---{Normal}" * 9)
        time.sleep(2)
        for j in sub_split:
            url = f"http://{j}.{d[1]}"
            try:
                if time_s > 0:
                    time.sleep(time_s)
                    requests.get(url, timeout=3)
                else:
                    requests.get(url, timeout=3)
                    print("[!] Note: no -t(time) flag specified.")

            except requests.ConnectionError:

                pass

            except TimeoutError:

                print("Trying connect to the target...")
                pass

            except RuntimeError:

                pass

            except KeyboardInterrupt:
                print("User stopped process, EXIT....")
                exit(0)

            except TypeError as e:
                print(print("Use -h for more information..."))


            else:
                print(f"[+] {Gray}{args.d}{Normal} : {Yellow}Possible Subdomains{Normal}: {url}")
