from itertools import count
import requests
import re
from bs4 import BeautifulSoup
from pynput import keyboard

user_url = input("[+] Enter target full URL: ")
count = 0
emails = []
urls = [user_url]
try:
    print("press q to exit")
    while len(urls):
        print(urls)
        if len(urls) > 100:
            break
        try:
            r = requests.get(urls[0])
            emails.append(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", r.text, re.I))
            soap = BeautifulSoup(r.text, features="html.parser")

            for every in soap.find_all("a"):
                link = every.attrs['href'] if 'href' in every.attrs else ''
                if link.startswith('/'):
                    full_link = user_url + link
                    urls.append(full_link)
                elif link.startswith('htt'):
                    urls.append(link)    
            
            urls.pop(0)
        except:
            print("[!!!] Incorrect URL. Please give full url for instance https://www.example.com")
            break
    for line in emails:
        for i in line:
            print(f'[+] {i}')
except KeyboardInterrupt:
    print("[-] Ending...")