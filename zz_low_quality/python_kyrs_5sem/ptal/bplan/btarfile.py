import sys
from io import BytesIO
import tarfile

a = ''.join(sys.stdin.read().replace(' ', ''))
a.split('\n')
s = bytes.fromhex(a)
bts = BytesIO(s)
file = tarfile.open(fileobj=bts)
otvet = []

temp = file.getmembers()
for elem in temp:
    if elem.isfile():
        otvet.append(elem)

temp = map(lambda x: x.size, otvet)
temp = sum(temp)
print(temp, len(otvet))