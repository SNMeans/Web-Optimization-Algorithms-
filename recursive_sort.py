# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Recursive Sort < O(n^2)
#
# NAME:         Sumi Nia Means    April 02 2024
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a less than O(n^2) sort function `recursive_sort`
# that takes an unordered array of numbers as a parameter
# and returns a sorted array using merge sort or quick
# sort using recursion, rather than loops.
def recursive_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less=[i for i in array[1:] if i<= pivot]
        greater[i for i in array[1:] if i > pivot]

        return recursive_sort(less) + [pivot] + recursive_sort(greater)


def main():
    arrays = [[45, 67, -2, 33, 0, -44, 134, -67], \
              [i for i in range(10)], \
              [i for i in range(10, -1, -1)]]

    for a in arrays:
        print("Unordered:", a)
        print("Sorted:   ", recursive_sort(a))


main()
