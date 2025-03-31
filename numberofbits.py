def numberofbits(n):
    ones = 0
    zeros = 0
    
    while(n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeros += 1
            
        n >>= 1
    print("ones: ",ones,"\nzeros: ",zeros)
        
number = int(input("Enter a number: "))
numberofbits(number)

def setbit(x, num):
    if x & (1 << (num-1))==1:
        print("It's a set bit.")
        
    else:
        print("It's not a set bit.")
        
num = int(input("Enter a number: "))
z = int(input("enter the position of the number: "))
setbit(num, z)
