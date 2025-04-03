def swap(A, B):
    A = A ^ B
    B = A ^ B
    A = A ^ B
    print("After swapping: ",A, B)

A = int(input("Enter a number: "))
B = int(input("Enter a number: "))

print("Before swapping", A, B)
swap(A, B)


def swap2(a , b):
    a = (a & b) + (a | b)
    b = a + (~ b) + 1
    a = a + (~ b) + 1
    print("After swapping: ", a, b)
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("Before swapping, ", a, b)
swap2(a,b)