import random
import socket
import time
from TheSilent.clear import clear

CYAN = "\033[1;36m"

def kiwi(host,delay=0):
    clear()
    hits = []
    init_hosts = []
    hosts = []

    subdomains = ["aams","accent","accounts","acs-xs","acsamid01","acsnas","adams","adfs","adm","admin","aes","aesdvr1","aggies","ahs","airwatch","akpk","alt","alumni","ams","angel","aovpn","api","aplus","apple","apps","apps2","apps3","aps","arabamid","asas","asg","atriuum","attalla","auth","auth2","autodiscover","av","barracuda","bbb","bcbeiboss2","bcboefilewave","bcrobotics","bcsipmonitor","bes","beverlye","bibbcompass","bibbdestiny","bibbdocumentserver","bigboy","blackboard","block","blocker","blogs","bms-audioe","bsl","butlerco","carver","casarry","cassidy","ccctc","cchs","ccs","ciscoasa","citrix","cl","classlink","classweb","cloverdale","cms","cnp","cobalt","collab-edge","compass","compasslearning","conecuh","cov","cpi","cs-voip","csg","ctcsec","d2l","daleville","dare","datsrv055","dcsamid01","dcsfws","dcsnamidcl","dcsxserve","ddi","decisioned","dell-learn","des","designthefuture","destination","destiny","dialin","discovervideo","dn","docefill","documentservices","donehoo","dothan","dothanhigh","dothantech","dsviewer","e2010","ebes","ecsinow","ecspowerschool","edulog","ees","eforms","email","employeeportal","es","esmoodle","esms","ess","et","etcentral","etcontent","etsecurity","etsts","eurabrown","evans","exchange","expressway","faine","fairview","falcon1","fce","fes","filewave","filter","finance","floyd","forms","fortis","franklin","fs","ftp","gadsdencity-hs","gchs","girard","girardms","gmail","gms","grandview","greene","guac","guac-test","happytimes","hcs-ess","hct","hd","hdcsmtp1","hdctab","heard","helpdesk","henryclay","henryconnects","heritagehigh","hes","hhs","highlands","hms","homewood","honeysuckle","hs","iboss","ibossreporter","icreports","imail","info","infonowweb","inow","inowapi","inowhome","intranet","jasper","jds","jsj-cam","kb","kc","kellysprings","kronmobile","lessonplans","lib","library","links","lms","mail","mail2","mail4","maps","matterhorn","mdm","mdm2","mealapps","media","meet","mes","mitchell","montage","montagebeta","montana","moodle","mta-sts","my","mydocs","myfiles","mypay","mytime","nagios","netview","newmail","nextgen","ngweb","nms","northview","ns","ns1","ns2","nutrition","oaes","oldmail","onlinemealapp","packetview","pandora","parent","parentportal","passwordreset","passwordresetregistration","payday","payroll","pcmon","pdexpress","pinpoint","pop","portal","powerschool","pres","preschool","proxy","proxy2","pssb","pwchange","radius","rds","readydesk","relay","remotesupport","renlearn","reporter","res","rocket","rollcall","router","rp","rsapi","s","safariaves","searchsoft","secure","securityportal","selmast","ses","sets","setsti","setsweb","shssec","sis","slingluff","smtp","smtp-1","smtp1","smtp2","spc","sso","sspr","staffportal","status","stisets","striplin","sts","studentportal","support","swinstall","teacherportal","technology","techweb","techwiki","tes","test","test5","thompson","tickets","tm","tools","transportation","trend","ugms","updates","vpn","walnutpark","webmail","websets","wes","wessec","wiki","williamblount","workorders","wpes","www","www1","www2"]
    subdomains = random.sample(subdomains,len(subdomains))
    for _ in subdomains:
        # check reverse dns
        print(CYAN + f"checking for reverse dns on {_}.{host}")
        dns_host = f"{_}.{host}"
        time.sleep(delay)
        try:
            hits.append(f"reverse dns {_}.{host}: {socket.gethostbyaddr(dns_host)}")
        except:
            pass
        # check if host is up
        print(CYAN + f"checking {_}.{host}")
        try:
            my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            my_socket.settimeout(1.25)
            my_socket.connect((f"{_}.{host}",80))
            my_socket.close()
            hits.append(f"found {_}.{host}")
        except ConnectionRefusedError:
            hits.append(f"found {_}.{host}")
        except socket.timeout:
            hits.append(f"found {_}.{host}")
        except:
            pass

    clear()
    hits.sort()
    for hit in hits:
        print(CYAN + hit)

    print(CYAN + f"{len(hits)} results")
