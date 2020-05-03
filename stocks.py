def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

l= []
for i in range(600851475143):
    if(if(i % 600851475143 == 0) and (if(isPrime(i)))):
        l.append(i)
    
print(max(l))




def palin(num):
    if num == str(num)[::-1]:
        return 1

k = 999
s = 999
l =[]

for i in range(999  ,1):
    p = i * 999
    if(palin(p)):
        l.append(p)
print(l)







