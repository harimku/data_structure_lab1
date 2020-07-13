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
            # move to temp array
            temp_arr[digit].append(runner.node)
            radix_arr[i].Delete(runner.node)
            runner = runner.next

    # re-assign in new order
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

    # get max element and its number of radix
    max_element = get_max(arr)
    max_radix = get_radix(max_element)
    #print(max_element)
    #print(max_radix)

    # Initial filling of array with Numbers.txt (for radix 1)
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
    numbers = np.loadtxt(fname = "./Numbers.txt")
    radix_sorted = radix_sort(numbers) # Radix sort output (an array of doubly linked lists)


    ## Print the radix sort output (array of doubly linked lists)
    print('========== Printing Radix Sort Output ===========')
    print('')
    for i in range(10):
        print("Printing radix_sorted[{}]".format(i))
        print(radix_sorted[i].output()) # call output function from Doubly Linked List class
        print('==============================')
    print('End of Array!')
    print('')


    ## Compare my output with python sorted output
    # Python Sorted (Correct Output)
    correct_sorted = map(int, sorted(numbers.tolist()))
    
    # Radix Sort  
    radix_output = [] # combine Radix sort output into a single list for comparison
    for i in radix_sorted:
        runner = i.head
        while(runner):
            if(runner.node is not None):
                radix_output.append(runner.node)
            runner = runner.next

    # Compare the two outputs
    print('===== Comparing Radix sort output with Correct ouput =====')
    print('[Radix Sort Output],[Correct Output]')
    for a,b in zip(radix_output,correct_sorted):
        print('{}, {}'.format(a,b)) 
    print('')
    print('Do the two outputs match? :')
    print('{}'.format(radix_output == correct_sorted))
    print('')


    
if __name__ == '__main__':
    main()