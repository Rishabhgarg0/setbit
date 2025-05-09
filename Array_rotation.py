def rotation(n, A, A_size):
    for i in range(n):
        rotate(A, A_size)
        
def rotate(A, A_size):
    temp = A[0]
    for i in range(A_size - 1):
        A[i] = A[i + 1]
    A[A_size - 1] = temp
    
def print_array(A, A_size):
    for i in range(A_size):
        print(A[i])
        
A = [5,8,6]
print_array(A, len(A))

rotation(2, A, len(A))
print_array(A, len(A))