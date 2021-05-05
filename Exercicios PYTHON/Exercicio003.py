from abc import abstractproperty


#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

n = 633
m = 0
l = list()

for i in range(n,1,-1):
    if n%i==0:
#        print(i)
        l.append(i)
        m += 1

print(max(l, key=int))

if m==0:
    print("é primo")
else:
    print("qnt", m)
