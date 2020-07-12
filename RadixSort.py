from array import *
from DLinkedList import DList
import numpy as np


def get_radix(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i

def radix_sort(arr):
    # create array of 10 doubly linked lists
    radix_arr = []
    for _ in range(10):
        new_dl = DList()
        radix_arr.append(new_dl)
    exit()
    
    # get max element and its number of digits
    max_element = np.amax(arr1)
    num_radix = get_radix(max_element)
    print(max_element)

    for d in range(num_radix):
        arr = counting_sort(arr, max_element, )
    return arr1


def main():    
    fileref = open("Numbers.txt", "r")
    numbers = fileref.read()
    print(numbers)
    fileref.close()

    #radix_sort(numbers)


if __name__ == '__main__':
    main()