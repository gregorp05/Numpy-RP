import numpy as np

def for_loop_range(rng, func, *args):
    np.vectorize(lambda idx: func(idx, *args), otypes=[int])(np.array(rng))
    return None

def for_loop(i, func, *args):
    np.vectorize(lambda idx: func(idx, *args), otypes=[int])(np.arange(i))
    return None

# za vse tistre k niste js :)

# tuki das svoje argumente k jih rabs, nujen je samo i

# primer z 0 dodatnimi argumenti:
def for_inside1(i, *args):
    #print(i)
    return 0

for_loop(10, for_inside1)


# primer z 1 dodatnim argumentom:
def for_inside(i, inp, *args):
    inp[i] += 9
    return 0

a = np.arange(10)
for_loop(10, for_inside, a)
print(a)


# primer z 2 dodatnima argumentoma:
def for_inside2(i, a1, a2, *args):
    #print(a1[i], a2[i])
    return 0

a = np.arange(10)
b = np.arange(10) * 2
for_loop(10, for_inside2, a, b)