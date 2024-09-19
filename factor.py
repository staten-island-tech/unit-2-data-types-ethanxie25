x = int(input('Choose the number you would factor'))

def x_factor():
    for z in range(x): 
        if x % z == 0:
            print(x)
x_factor()