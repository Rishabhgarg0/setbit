def headrecurr(n, num):
    if (n > num):
        return
    
    headrecurr(n+1, num)
    
    print(n)
    
num = int(input("Enter a number: "))

headrecurr(1,num)