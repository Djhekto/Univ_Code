import sys
import base64

h = []
ii = 0
a = sys.stdin.buffer.read().strip()
a = base64.b85decode(a)

while (el := int.from_bytes(a[ii:ii + 1], byteorder='big', signed=True)):	
    h.append(el)
    ii += 1
#    print(ii)

ii += 1
otvet = []
aaaa = int((len(a) - ii) / sum(map(abs, h)))
for j in range(aaaa):
    for i in h:
        if i > 0:
            otvet.append(int.from_bytes(a[ii:ii + abs(i)], byteorder='big', signed=False))
        elif i<=0:
            otvet.append(int.from_bytes(a[ii:ii + abs(i)], byteorder='big', signed=True))
        ii += abs(i)
finotvet = sum(otvet)
print(finotvet)