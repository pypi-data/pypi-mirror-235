import re
import urllib.parse
import TheSilent.kitten_crawler as kitten
import TheSilent.puppy_requests as puppy
from TheSilent.clear import clear

CYAN = "\033[1;36m"

def pumpkin(host,delay=0):
    word_list = []
    links = kitten.kitten_crawler(host,delay)
    clear()
    for link in links:
        word_list = list(set(word_list[:]))
        word_list.sort()
        print(CYAN + f"checking: {link}")
        try:
            data = puppy.text(link)
            data = data.replace("\n","")
        except:
            continue

        words = re.findall("[a-z]+",data)
        for word in words:
            word_list.append(word.lower())

    word_list = list(set(word_list[:]))
    word_list.sort()

    clear()
    print(CYAN + f"found {len(word_list)} unique words")

    with open(f"{urllib.parse.urlparse(host).netloc}.txt","a") as file:
        for word in word_list:
            file.write(f"{word}\n")
