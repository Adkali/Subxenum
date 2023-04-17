![צילום מסך 2022-10-20 181413](https://user-images.githubusercontent.com/90532971/196989261-49182e3d-b45a-4b17-80db-3699ac67274f.png)

# >>Subxenum
Subxenum is a Python tool designed for subdomain enumeration that uses advanced techniques such as grabbing and parsing. It can retrieve subdomains from sources such as crt.sh data, sublist3r, and whois. It is a powerful tool for penetration testers and security researchers, and is intended for educational purposes only. Subxenum is an open-source project available on GitHub, and can help when conduct a research on a target when gathering information.
<br>

<h3>Key Features</h3>
• Subxenum is designed to be easy to use and delivers results quickly.<br>
• Results can be printed on the screen or saved to a file.<br>
• The '-t' flag allows users to time requests and optimize enumeration.<br>
• Subxenum supports various techniques including whois, crt, and user-defined wordlists to generate comprehensive results.<br>
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
  -w W, -word W      Wordlist path.
  -v V, -version V   Subxenum, version 1.2 made by adkali.
  -t [T], -time [T]  Time in each request.
  -i I, -info I      Use 'whois' for more info about the target.
  -c C, -crt C       Grab subdomains from crt.sh data
  -s S, -sub S       Get subdomains using sublist3r data
</pre>

# Examples:

* For using 'Whois' information, use the '-i' flag with 'whois' after it to grab information log from whois:<br>
// python3 Subxenum.py -d http:/examplesite.com -w file.txt -i whois

![2](https://user-images.githubusercontent.com/90532971/182032070-379dca31-52ca-4d1c-8528-a7dcc20c5698.png)
<br>

Subxenum is a penetration testing tool designed for domain enumeration. It has been tested on Kali Linux but can be used on other platforms. The tool allows users to load subdomains from a file, and with the '-t' flag, timing requests can be specified. It also supports Whois, crt, and sublist3r data to provide more information about the target. In the future, features such as directory search, server information, and Nmap integration will be added. Subxenum is intended for educational purposes only, and any issues should be reported. Ensure that the 'http://' protocol is used when running the tool.

# Updates
1. Fix bug outputs while using 'c' flag & other functionalities.<br> Soon i wil add the option of using brute-force for looking for hidden directories inside of the script on subdomains you found using the code.
2. 14/12 - if "whois" results in nothing, use "pip install python-whois".
3. 18/04 - Subxenum 1.2
