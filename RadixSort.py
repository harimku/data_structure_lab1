from array import *
from DLinkedList import DList
import numpy as np
from collections import Counter


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
    # temporary array to store values for moving
    temp_arr = []
    for _ in range(10):
        arr = []
        temp_arr.append(arr)

    # counting sort
    for i in range(10):
        runner = radix_arr[i].head
        
        while(runner):
            # get the digit in question
            digit = runner.node % (radix * 10) // radix

            temp_arr[digit].append(runner.node)
            radix_arr[i].Delete(runner.node)
            runner = runner.next

    for i in range(10):
        for d in temp_arr[i]:
            radix_arr[i].Append(d)



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
    for _ in range(max_radix):
        counting_sort(radix_arr, radix)
        radix *= 10

    return radix_arr




def main():   
    numbers = np.loadtxt(fname = "./Numbers.txt")

    correct_sorted = map(int, sorted(numbers.tolist()))
    radix_sorted = radix_sort(numbers)
    out_arr = []
    for i in radix_sorted:
        runner = i.head
        while(runner):
            if(runner.node is not None):
                out_arr.append(runner.node)
            runner = runner.next
    
    #print(correct_sorted[:10])
    #print(out_arr[:10])

    bool_compare = []
    for a,b in zip(out_arr,correct_sorted):
        print('{}, {}'.format(a,b))

    #for i,v in enumerate(bool_compare):
    #    print('Mismatch at index {}'.format(str(i)))
    

    print('{}'.format(out_arr == correct_sorted))


if __name__ == '__main__':
    main()