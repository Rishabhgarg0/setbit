def paren(l,r,p,n,s):
    if (p==2*n):
        for ss in s:
             print(ss, end='')
        return
    
    if (l > r):
        s[p] = "}"
        paren(l,r+1,p+1,n,s)
        
    if (l < n):
        s[p] = "{"
        paren(l+1,r,s,p+1,n)
        
n = int(input("Enter the number of parenthesis: "))
s = [""] * 2 * n
paren(0,0,0,n,s)
