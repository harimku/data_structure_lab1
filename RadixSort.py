from array import *
from DLinkedList import DList
import numpy as np


def get_max(arr):
    max_element = 0
    for n in arr:
        if max_element < n:
            max_element = n
    return max_element

def get_radix(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i

'''
def counting_sort(radix_arr, place):
    # Place the elements in sorted order
    i = len(arr) - 1

    while i >= 0:
        digit = int(arr[i] % (place * 10) // place)
        radix_arr[digit].Append(arr[i])
        i -= 1
    
    return radix_arr
'''



def radix_sort(arr):
    # create array of 10 doubly linked lists
    radix_arr = []
    for _ in range(10):
        new_dl = DList()
        radix_arr.append(new_dl)

    # get max element and its number of digits
    max_element = get_max(arr)
    num_radix = get_radix(max_element)
    print(max_element)
    print(num_radix)

    # Initial filling of radix_arr with Numbers.txt
    for num in arr:
        num = int(num)
        i = num % 10 
        radix_arr[i].Append(num)

    # sort using counting sort
    radix = 10
    for _ in range(num_radix):
        counting_sort(radix_arr, radix)
        radix *= 10

    return radix_arr




def main():   
    numbers = np.loadtxt(fname = "/Users/felons/Downloads/Numbers.txt")

    x = radix_sort(numbers)

    for i in x:
        print()
        print(i.output())


if __name__ == '__main__':
    main()