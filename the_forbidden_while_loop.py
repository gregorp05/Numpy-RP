import numpy as np

def while_loop(func, *args):
    ind = np.array([0]) # must be length 1
    ect = np.array([0])
    
    while_helper(func, ind, ect, *args)
    return None
    
def while_helper(func, ind, ect, *args):
    try:
        np.vectorize(lambda idx: while_break_helper(func, ind, ect, *args), otypes=[int])(np.arange(100000)) # bigger num in arange less recursion calls
        if ect[0] == 0:
            while_helper(func, ind, ect, *args)
    except IndexError:
        if ect[0] == 1:
            return None
    return None

def while_break_helper(func, break_arr, ext, *args):
    if not func(*args):
        ext[0] = 1
        break_arr[1] # call outside bound so that while_loop errors-out
    return 0
    
    
# demonstration with two extra variables
# even more programming warcrimes were committed here

# in while loop there must be a exit case: if you want while True just set it to sth really big
# 'variables' that you pass must be numpy arrays since they ac like pointers / addresses, could be achieved with classes I think?

# exit is triggered when while_inside func returns False 
def while_inside(i, ff, *args):
    if i[0] > 5000:
        return False # this is necessary so that the recursion limit error is not triggered, also you want an exist case you p*****
        
    ff[0] = not ff[0] # flip flop just for demo

    print(i[0], ff[0])

    i[0]+= 1 # just add 1 to 'index' variable, 
    return True

index = np.array([0])
fliflop = np.array([0])

while_loop(while_inside, index, fliflop)

