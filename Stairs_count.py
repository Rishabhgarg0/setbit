def steps(stairs):
    if (stairs < 0):
        return 0
    if (stairs == 0):
        return 1
    
    two_steps = 0
    one_step = 0
    
    if (stairs >= 2):
        two_steps = steps(stairs - 2)
               
    one_step = steps(stairs - 1)
    
    return two_steps + one_step

stairs = int(input("Enter the number of stairs."))

print("The ways by which we can climb is: ", steps(stairs))