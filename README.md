# >>Subxenum
Subdomain enumerate tool (Subxenum) using different techniques and scraping.
With Subxenum, you can brute-force subdomains using a wordlist files, scrap results from crt, ved and get information from whois using scraping with python.
With Subxenum, you can select from variety of techniques while enumerate subdomains.
<br>

<h3>Key Features</h3>
+ Easy to use, easy to get results.<br>
+ you can choose print the results on the screen, or save them into a file.<br>
+ with the flag '-t', you can timing easy requests you made while enumerating.<br>
+ using whois, crt or ved results include you'r own loaded file inside the code.<br>
<br>

![צילום מסך 2022-07-31 174131](https://user-images.githubusercontent.com/90532971/182031590-c70133d9-99a7-4cc1-b639-cac9dccaa32f.png)

# Install
<pre>
1 git clone https://github.com/Adkali/Subxenum.git
2 cd /Subxenum 
3 pip3 install -r requirements.txt
4 python3 [script.py] -domain [ domain http:// ] -word [ wordlist.txt ] 
</pre>
# Usage
<pre>
optional arguments:
  -h, --help         show this help message and exit
  -d D, -domain D    Domain URL, Example: http://example.com
  -w W, -word W      Wordlist Path.
  -v V, -version V   Subxanum, Version 1.0 Made By Adkali.
  -t [T], -time [T]  Time in each request for enumerate subdomains.
  -i I, -info I      Use 'whois' for more info about the target.
  -c C, -crt C       scrap subdomains from crt.sh data
  -x X, -xed X       scrap subdomains using Vedbex data
</pre>

# Examples:
* normal brute-subdomains from a file:<br>
// python3 Subxenum.py -d http://examplesite.com -w file.txt

![3](https://user-images.githubusercontent.com/90532971/182032263-d53eaf31-ce4c-4892-90be-234d3b769999.png)

* For using 'Whois' information, use the '-i' flag with 'whois' after it to grab information log from whois:<br>
// python3 Subxenum.py -d http:/examplesite.com -w file.txt -i whois

![2](https://user-images.githubusercontent.com/90532971/182032070-379dca31-52ca-4d1c-8528-a7dcc20c5698.png)
<br>

This tool tested only on kali linux, but you can test it on others platforms/distributions.
If you want to loads som Subdomains-List, you get download some of from github, there are planty of them for you to use.
With time, i hope to add the ability to perform dir search inside each subdomain, get information about running server, using Nmap to look
for open ports or vulnerability the dubdomain might have, just to help penetration testers while searching for vulnerabilities.
please, use this tool for education purpose only! if you seem to get into a problem while running this tool, see you are using the 'http://' protocol, and if from some reason it still doesn't work, please let me know.
