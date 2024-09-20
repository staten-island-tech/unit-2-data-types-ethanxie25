num = int(input('Choose the number you would like to factor'))

def num_factor():
    for z in range(1, num + 1): 
        if num % z == 0:
            print(z)
num_factor()
