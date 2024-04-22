# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Iterative Linear Search
#
# NAME:        Sumi Nia Means
# DATE:        April 2 2024
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a function `linear_search` that takes an
# unordered array of numbers as a parameter and
# a number to search for and returns the index of
# the number in the array, or -1 otherwise. Your
# search should be performed using a loop, rather
# than recursion.
def linear_search(array, num):
    for index, element in enumerate(array):
        if element == num:
            return index
    return -1

def main():
    a = [45, 67, -2, 33, -44, 134, -67]
    print(a)
    for n in [1, 0, -1, 2, -2, 134, 67, -67]:
        print("%5d index? %d" % (n, linear_search(a, n)) )

main()
