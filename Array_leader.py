def current_leader(a,a_size):
    current_max = a[a_size-1]
    print(current_max)
    
    for i in range(a_size - 2, -1, -1):
        if current_max < a[i]:
            current_max = a[i]
            print(a[i])

a = [5,8,4,7,10,3,14,2,5,7,8,9]

current_leader(a, len(a))