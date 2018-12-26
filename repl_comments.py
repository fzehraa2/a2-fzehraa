#https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
#I borrowed the codes in the lines from 4th to 8th from this link

from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

pas = "hidden"
hsh1 = create_hash(pas)
list = []
while True:
    print("enter a comment")
    com = input()
    print("enter the password")
    psw=input()
    hsh2 = create_hash(psw)

    if hsh1==hsh2:
        print("those were the same passwords")
        print("previously entered comments")
        list.append(com)

        for com in list:
         i = 1 + list.index(com)
         print(str(i) + "." + com)

    else:
        print("those were different passwords")
