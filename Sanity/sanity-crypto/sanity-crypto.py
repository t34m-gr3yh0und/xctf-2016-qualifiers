#!/usr/bin/python

import base64

s = "GgEWBDkaDRAdc3cdMXIdIS5zISpxPw=="
m = base64.b64decode(s)
flag = ""
for i in range(len(m)):
        v = ord(m[i]) ^ 0x42
        flag = flag + chr(v)


print flag

