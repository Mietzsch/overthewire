#!/bin/python
import requests

url = "http://natas22.natas.labs.overthewire.org/?revelio"
auth = ("natas22", "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s")


r = requests.get(url, auth=auth)

for redirect in r.history:
    print(redirect.text)
