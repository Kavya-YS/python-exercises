'''
1.If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20 , print Weird
If  is even and greater than , print Not Weird

2.The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

3.The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
4. check the leap year
5.Print the list of integers from  through  as a string, without spaces

'''



import math
import os
import random
import re
import sys

def check_input(n):
    "check the input"
    if n%2 == 0:
        if n>20:
            print(" Not Weird")
        elif n>6 and n<20:
            print("Weird")
        else:
            print("Not weird")
    else:
        print("Weird odd")


if __name__ == '__main__':
    n = int(input().strip())
    check_input(n)