import binascii
s = "jonsnowisdragonbybirth"
key = binascii.unhexlify("3a2c3a35152538272c2d213e332e3c25383030373a15")
ans = ""
for i,j in zip(s, key):
    ans += chr(ord(i)^ord(j))
print(ans)