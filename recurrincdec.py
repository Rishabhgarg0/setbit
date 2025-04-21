def order(n,num):
    if (n < 1 or n > num):
        return
    
    print(n)
    order(n-1,n)
    print(n)
    
n = int(input("Enter a number: "))
order(n,n)