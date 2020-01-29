import traceback as tc
import sorting as s
import numpy as np

s.test = True


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def test(sorting_function):
    arr = s.Array(np.random.randint(low=-2000, high=2000, size=1000))
    sorting_function(arr)
    try:
        assert is_sorted(arr.values), sorting_function.__name__ + ' Failed.'
    except AssertionError as msg:  
        print(msg) 
    return 'Passed'


functions = [s.cycle_sort, s.shell_sort, s.comb_sort, s.pigeonhole_sort]
for function in functions:
    print('Testing:   ', function.__name__.ljust(17), test(function))
