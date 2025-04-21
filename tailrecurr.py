def tailrecurr(n,num):
    if (n > num):
        return
    
    print(n)
        
    tailrecurr(n+1,num)
    
n = int(input("Enter a number: "))

tailrecurr(1,n)