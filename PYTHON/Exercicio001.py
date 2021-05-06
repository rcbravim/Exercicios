j = 0

for i in range(1,1000):
    if (i%3 == 0) or (i%5 == 0):
        j = j+i
    
print(j)

'''
def zarib3or5(n):
    if n % 3 ==0 or n% 5 ==0 :
        return True
    else:
        return False

sum = 0
for i in range (1,1000):
 
    if zarib3or5(i):

        sum = sum + i
    

print (sum)
'''