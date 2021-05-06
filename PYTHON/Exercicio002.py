
qnt = 4*1000000

pri = 0
seg = 1
ult = 0
sum = 0

while ult <= qnt:
    ult = pri + seg
    pri = seg
    seg = ult
    if (ult%2 == 0):
        sum = sum + ult
print(qnt)
print(sum)


