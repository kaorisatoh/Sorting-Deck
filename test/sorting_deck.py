#!/usr/bin/env python3
import argparse


def list_to_sort():
    """
    Return a list with 3 elements:
    0. the algorithm required to sort
    1. the list of intergers need to be sorted
    2. true if gui is specified, else return false
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO', choices=['bubble', 'insert', 'quick', 'merge'], default='bubble', help='specify which algorithm to use for sorting among [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true', help='visualise the algorithm in GUI mode')
    args = parser.parse_args()
    list = [args.algo, args.integers, args.gui]
    return list


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                # print (list)
    return list


def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i-1, -1, -1):
            if list[j] > list [j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                # print(list)
    return list


def partition(list, left, right):
    """
    Choose the last number as pivot and divine list into smaller and larger
    Return the right position of that pivot to continue divine sublists
    """
    pivot = list[right]
    print(pivot)
    i = left - 1
    for j in range(left, right):
        if list[j] < pivot:
            i += 1
            list[j],list[i] = list[i],list[j]
    list[right], list[i+1] = list[i+1], list[right]
    return (i+1)


def quick_sort(list, left, right):
    if left < right:
        piv = partition(list, left, right)
        print ('1: ', end='')
        print (list)
        quick_sort(list, left, piv-1)
        print ('2: ', end='')
        print(list)
        quick_sort(list, piv+1, right)
        print ('3: ', end='')
        print(list)
    return list


def merge_sort(list):



list = list_to_sort()
# print(bubble_sort(list[1]))
# print(insertion_sort(list[1]))
print(quick_sort(list[1],0,len(list[1])-1))
