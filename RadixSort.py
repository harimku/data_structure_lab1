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


def counting_sort(radix_arr, radix):
    temp_arr = []
    for _ in range(10):
        arr = []
        temp_arr.append(arr)

    for i in range(10):
        runner = radix_arr[i].head
        
        while(runner):
            # get the digit in question
            digit = runner.node % (radix * 10) // radix

            
            # if it's in the right place
            if (digit == i):
                runner = runner.next

            # else, move it 
            else:
                radix_arr[digit].Append(runner.node)
                radix_arr[i].Delete(runner.node)
                runner = runner.next
            
    return radix_arr



def radix_sort(arr):
    # create array of 10 doubly linked lists
    radix_arr = []
    for _ in range(10):
        new_dl = DList()
        radix_arr.append(new_dl)

    # get max element and its number of digits
    max_element = get_max(arr)
    max_radix = get_radix(max_element)
    print(max_element)
    print(max_radix)

    # Initial filling of array with Numbers.txt (radix 1)
    for num in arr:
        num = int(num)
        i = num % 10 
        radix_arr[i].Append(num)

    # sort array using counting sort
    radix = 10
    for _ in range(max_radix - 1):
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