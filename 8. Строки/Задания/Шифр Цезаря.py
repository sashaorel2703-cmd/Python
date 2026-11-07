import string


def caesar_cipher_char(c,k):
    alp="abcdefghijklmnopqrstuvwxyz"
    if c.lower() not in alp :
        return c
    elif c.isupper() :
        return alp[(alp.find(c.lower())+k)%len(alp)].upper()
    return alp[(alp.find(c)+k)%len(alp)]

def caesar_cipher(s,k):
    x=""
    for i in s :
        x+=caesar_cipher_char(i,k)

    return x


print(caesar_cipher("abc,яЯ,,::X abc ",3))
