import os, time
import requests, random
from bs4 import BeautifulSoup
os.system('clear')
lgo = '''

            ;               ,
         ,;                 '.
        ;:                   :;
       ::                     ::
       ::                     ::
       ':                     :
        :.                    :
     ;' ::                   ::  '
    .'  ';                   ;'  '.                                ::    :;                 ;:    ::                               ;      :;.             ,;:     ::
   :;      :;:           ,;"      ::
   ::.      ':;  ..,.;  ;:'     ,.;:
    "'"...   '::,::::: ;:   .;.;""'
        '"""....;:::::;,;.;"""
    .:::.....'"':::::::'",...;::::;.                               ;:' '""'"";.,;:::::;.'""""""  ':;
  ::'         ;::;:::;::..         :;                            ::         ,;:::::::::::;:..       ::
 ;'     ,;;:;::::IP-DOM::::;";..    ':.
::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ;
  ;    ::   :::::::  :::::::   :    ;
   '   ::   ::::::....:::::'  ,:   '
    '  ::    :::::::::::::"   ::
       ::     ':::::::::"'    ::
       ':       """""""'      ::
        ::      F.N.W.H      ;:
        ':;                 ;:"
          ';              ,;'
            "'           '"

            '''
class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKGREEN,lgo,bcolors.ENDC)
time.sleep(2)
header = {
     'User-Agent': random.choice(['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    ]),
    'Accept-Encoding': random.choice(['gzip', 'deflate', 'sdch', 'br']),
    'Accept-Language': random.choice(['en-US', 'en;q=0.8', 'zh-CN;q=0.6', 'zh;q=0.4']),
    'Cache-Control': 'no-cache',
    'Connection': random.choice(['keep-alive', 'close']),
    'Pragma': 'no-cache'
} 
url = 'https://networksdb.io/domains-on-ip/'

domains_file = 'Domains.txt'
data = [] # to store ip and its domains
if not os.path.exists('IP.txt'):
    os.mknod('IP.txt')
with open('IP.txt', 'r') as infile, open(domains_file, 'a') as outfile:
    if os.stat('IP.txt').st_size == 0:
        print(bcolors.FAIL,'ERROR',bcolors.ENDC)
        time.sleep(1)
        print(bcolors.WARNING,'No IP found in IP file',bcolors.ENDC)
        exit()
    else:
        print(bcolors.OKCYAN,'reversing domains in each IP',bcolors.ENDC)
    save_all_results = input("\n\n|### Save ALL results without confirmation?###| y/n  ")
    for line in infile:
        # I am assuming that file has no header and that each line correspond to an ip so no extra effort is needed
        ip = line.strip()
        api = url + ip
        try:
            print(bcolors.OKGREEN,'\ncrawling...',bcolors.ENDC)
            html = requests.get(api, headers=header)
            soup = BeautifulSoup(html.text, 'html.parser' )
            ati = soup.find('div', class_='main-container block')
            dom = ati.find('pre').get_text(strip=True, separator=' ')
            print(ip)
            print(dom)

            if save_all_results.lower() == 'y':
                ch = 'y'
            else:
                ch = input("\n\n|### SAVE RESULT?###| y/n  ")

            if ch.lower() == 'y':
                outfile.write(dom)
                pass

                # You also can save the ip and its domains for later save to a spreadsheet file using pandas lib
                for domain in dom.split():
                    data.append([ip, domain])
            else:
                continue
        except AttributeError:
            print(bcolors.FAIL,'IP Not Found', bcolors.ENDC)
            continue # continue to the next one
            # exit()
        except KeyboardInterrupt:
            print(bcolors.FAIL,'EXIT',bcolors.ENDC)
            exit()
        except requests.ConnectionError:
            print("Can't connect to internet")
            exit()
