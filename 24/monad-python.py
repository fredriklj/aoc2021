import random

# If all modulo operations results in 0 remainer, Z will be zero in the end

start = 94992961162998 

def f1(a,b,c):
    return 26*a+b+c

def f2(a,b,c,d):
    x = a % 26 + c
    a = int(a/26)
    if b == x:
        x = 0
    else:
        x = 1
    a = a * (25 * x + 1)
    a = a + (b + d) * x
    return a


while True:
    #start = random.randrange(11111111111111, 99999999999999)
    #start = 29467817373577     
    #start = 13492999573778
    monad = list(map(int,list(str(start))))
    
    if 0 not in monad:
    
        z = monad[0]
        z = f1(z,monad[1],6)
        z = f1(z,monad[2],4)
        z = f1(z,monad[3],2)
        z = f1(z,monad[4],9)
        z = f2(z,monad[5],-2,1)
        z = f1(z,monad[6],10)        
        z = f2(z,monad[7],-15,6)
        z = f2(z,monad[8],-10,4)
        z = f1(z,monad[9],6)        
        z = f2(z,monad[10],-10,3)
        z = f2(z,monad[11],-4,9)
        z = f2(z,monad[12],-1,15)
        z = f2(z,monad[13],-1,5)
        
        if z == 0:
            print(start,z)
    
    start += 1
