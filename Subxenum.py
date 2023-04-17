import requests
import time
from datetime import datetime
import argparse
import whois
import json
import os
import sublist3r

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

# ---------- Defined colors ----------
Yellow = "\033[1;33;40m"
Red = "\033[1;31;40m"
Normal = "\033[0;0m"
BM = "\033[1;35;40m"
Green = "\033[1;32;40m"
Gray = "\033[1;30;40m"

# ---------- Banner printing ----------
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

# -------------------- Manually error message for args --------------------
def ParserErros(errmsg):
    print("[!] Syntax Error!")
    print("Usage: python3 [ Script/Name ] -w [File] -d [http://Domain.com]\nFor more information about, use '-h' flag please.")
    exit()

# -------------------- ARGS TO BE DEFINED WITH USING THE CODE'S FLAGS --------------------

parser = argparse.ArgumentParser(description="Subdomain enumerate using 'whois'/word.list/crt/sublist3r")
parser.error = ParserErros
parser.add_argument('-d', '-domain', type=str, required=True, help='Domain URL, Example: http://example.com')
parser.add_argument('-w', '-word', type=str, required=True, help="Wordlist path.")
parser.add_argument('-v', '-version', type=str, required=False, help="Subxenum, version 1.2 made by adkali.")
parser.add_argument('-t', '-time', default=0, type=int, nargs='?', required=False,help="Time in each request.")
parser.add_argument('-i', '-info', type=str, required=False, help="Use 'whois' for more info about the target.")
parser.add_argument('-c', '-crt', type=str, required=False, help="Grab subdomains from crt.sh data")
parser.add_argument('-s', '-sub', type=str, required=False, help="Get subdomains using sublist3r data ")
args = parser.parse_args()

# ---------- INFO ABOUT FLAGS AND DEFINED THEM USING VAR ----------

domain = args.d
wordlist = args.w
time_s = args.t
who_is = args.i
crtsh = args.c
sub = args.s

# ---------- WHEN USING -C FLAG OPTION ('crt'), GET A LIST OF *. AND NONE ----------
sublist = []

# ---------- SPLIT DOMAIN, CUT OFF "http:// FOR THE SUBDOMAIN ----------
d = domain.split("http://")

# ----------  OPEN SPECIFIED FILE USING -WORD  FOR THE SPECIFIED FILE  ----------
try:
    SubList = open(args.w)
    SubList2 = SubList.read()
except FileNotFoundError:
    print(f"[!] {Red}Error:{Normal} >> File Doesn't exist...\nUsage Example: '/home/user/Desktop/directory/file.txt'")
    exit(0)

# ---------- AFTER CHECK, CONTINUE THE CODE ----------
 # ---------- Response 200 ----------
  # ---------- IF IT DOES, CONTINUE THE CODE ----------
try:
    res = requests.get(f"{domain}")
    if res.status_code != 200:
        pass
    else:
        if who_is == "whois":
            select = ["yes", "y"]
            who = input("Do you want to use 'Whois' for more information? Y/N: ").lower()
            if who in select:
                web = whois.whois(f"{domain}")
                file = open("Whois_Info.txt", "w")
                file.write(str(web))
                print(f"\n[+] >> {Green}'Whois_Info'{Normal} file has been created, continue...")
                print(f"{Red}---{Normal}" * 9)
                time.sleep(3)
            else:
                print(f"{Red}Note:{Normal} >> Continue without 'Whois' information about {args.d}.")
                print("For more information and help, Use '-h' flag.\n")
                pass
                time.sleep(3)
        else:
            print(f"{Red}Note:{Normal} >> Continue without  -i('Whois') flag")
            time.sleep(1)

        if crtsh == "crt":
            print(f"[+] Grabs subdomains from crt using json with splits.\n")
            print(f"{Red}Note:{Normal}'crt_list.txt' file will be add to current directory.")
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
                os.system(f"echo {i} >> crt_list.txt")
            print(f"{Red}---{Normal}" * 9)
            time.sleep(3)

        else:
            print(f"{Red}Note:{Normal} >> Continue without  -c('crt') flag")
            pass
            time.sleep(1)

        if sub == "sublist3r":
            def find_subdomains(domain):
                subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=False, verbose=True, enable_bruteforce=False, engines=None)
                return subdomains

            def print_subdomains(subdomains):
                for subdomain in subdomains:
                    print(subdomain)

            def save_subdomains(subdomains, file_path):
                with open(file_path, "w") as sub_file:
                    for subdomain in subdomains:
                        sub_file.write(subdomain + '\n')
                print(f"Subdomains written to {file_path}\n")
            if __name__ == '__main__':
                domain = d[1]
                subdomains = find_subdomains(domain)
                print_subdomains(subdomains)
                save_subdomains(subdomains, "sublist3r_results.txt")
        else:
            print(f"{Red}Note:{Normal} >> Continue without  -s('sublist3r') flag")
            time.sleep(1)

except TimeoutError:
    print("Timeout...Exit!")
except KeyboardInterrupt:
    print("User stopped process, abort....")
    exit(0)
except requests.exceptions.ConnectionError:
    print("Please, check the url again please.\nMake sure you wrote it has 'http://'.")
    exit(0)

# -------------------- CONTINUE THE CODE --------------------
options = ["yes", "y"]
progress = input(f"Continue run by {args.w}? type y/n: ")
if progress not in options:
    print(f"{Red}[!]Continue...{Normal}")
else:
    print("\n")
    for _ in range(2):
        for x in range(4):
            string = "[!]Please wait" + ">" * x + ""
            print(string, end="\r")
            time.sleep(0.5)
    print("\n")

# -------------------- Continue --------------------
    print("#################################################################")
    print(f"\n[+] >> Status: (INFO) {Yellow}Successful HTTP requests!{Normal}")
    time.sleep(1)
    print(f"[+] >> Date and time: {datetime.now()}")
    time.sleep(1)
    print(f"[+] >> {BM}File loaded: (INFO) {args.w}{Normal}")
    time.sleep(1)
    sub_split = SubList2.splitlines()
    print(f"[!] >> {Red}Warning:{Normal} (INFO) File {args.w} contains {len(sub_split)} Subdomains words.")
    time.sleep(1)
    res = requests.get(f"{domain}")
    if res.status_code == 200:
        print(f"[?] >> {Green}Mode:{Normal} (INFO) Starting enumerate subdomains on {domain}, Please Wait...\n")
        print(f"{Red}---{Normal}" * 9)
        time.sleep(2)
        for j in sub_split:
            url = f"http://{j}.{d[1]}"
            try:
                if time_s > 0:
                    time.sleep(time_s)
                    requests.get(url, timeout=2)
                    print("[!] Note: (time) flag specified.")

                if time_s <= 0:
                    requests.get(url, timeout=2)
                    print("[!] Note: no -t(time) flag specified.")

            except requests.ConnectionError:
                pass
            except TimeoutError:
                print("Timeout Error...")
                pass
            except RuntimeError:
                print("Please, try again!")
            except KeyboardInterrupt:
                print("User stopped process, EXIT....")
                exit(0)
            except TypeError as e:
                print(print("Use -h for more information..."))

            else:
                print(f"[+] {Gray}{args.d}{Normal} : {Yellow}Possible Subdomains{Normal}: {url}")

# ------------------------- CONTINUE TO BRUTE-FORCE --------------------------------
YES_OPTIONS = ["y", "yes"]
def BruteForce():
    subdomain_url_brute = input("Subdomain URL please: ")
    wordlists_path = input("Path to wordlists: ")

    with open(wordlists_path, "r") as directories:
        try:
            response = requests.get(subdomain_url_brute)
            if response.status_code == 200:
                print("Please wait... [ FOUND PATH WILL MARK IN BLUE ]")
                for word in directories:
                    word_stripped = word.strip()
                    response = requests.get(f"{subdomain_url_brute}/{word_stripped}")
                    if response.status_code == 200:
                        print(f"\n[!] PATH FOUND --- >> {subdomain_url_brute}/{word_stripped}")
                    else:
                        print(f"\n{subdomain_url_brute}/{word_stripped} ---- >>> [-] Bad request (HTTP/{response.status_code} - {datetime.now()}")
        except requests.exceptions.RequestException as e:
            print(f"\nError: {e}")

def ByeBye():
    for ix2 in range(4):
        ex = f"Exit{'.' * ix2}"
        print(ex, end="\r")
        time.sleep(0.5)

user_input = input("Brute force hidden domains? Type y/n: ").strip().lower()
if user_input in YES_OPTIONS:
    BruteForce()
else:
    ByeBye()
