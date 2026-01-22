from pwn import xor
KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY11= bytes.fromhex(KEY1)
KEY12='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY122= bytes.fromhex(KEY12)
KEY2=xor(KEY11,KEY122)
KEY13='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
KEY133 = bytes.fromhex(KEY13)
KEY3 =xor(KEY2,KEY133)
KEYL='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
KEYP= bytes.fromhex(KEYL)
flag=xor(KEYP,xor(KEY3,xor(KEY2,KEY11)))
print(flag.decode('ascii'))
