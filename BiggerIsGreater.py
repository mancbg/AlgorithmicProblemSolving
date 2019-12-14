"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""
import math
import os
import random
import re
import sys


def bigger_is_greater(word):
    # Create a list of chars from the word
    word_list = list(word)

    wrod = 'no answer'

    # Find the rightmost index such that
    # a[k] < a[k+1]
    k = None
    for i in range(len(word_list) - 2, -1, -1):
        if word_list[i] < word_list[i + 1]:
            k = i
            break

    # If such index doesn't exist, return
    if k is None:
        return wrod

    # Find index l > k such that
    # a[k] < a[l]
    l = None
    for i in range(len(word_list) - 1, k, -1):
        if word_list[k] < word_list[i]:
            l = i
            break

    # Swap k and l letter
    word_list[k], word_list[l] = word_list[l], word_list[k]

    # Reverse the list after k to get the smaller string
    wrod = "".join(word_list[:k + 1] + word_list[k + 1:][::-1])
    return wrod


def main():
    T = int(input())

    for T_itr in range(T):
        w = input()

        result = bigger_is_greater(w)
        print(result)


if __name__ == '__main__':
    main()
