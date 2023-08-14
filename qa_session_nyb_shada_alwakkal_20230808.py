""""
QA-session Beginner (Nyb) 2023-08-08
@author Shada Al-Wakkal, GitHub: Shada12354
"""

"""
The following code is from course book: Python Programming: An Introduction to Computer Science - John Zelle
"""

#13.3.2
"""
split nums into two halves
sort the first half
sort the second half
merge the two sorted halves back into nums
"""
def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 + 1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2, nums)


nums1 = [3, 7, 1, 9, 5]
mergeSort(nums1)
print("Sorted nums1:", nums1)

nums2 = [42, 8, 16, 23, 4, 15]
mergeSort(nums2)
print("Sorted nums2:", nums2)

# Test merge
list1 = [1, 4, 6]
list2 = [2, 5, 8]
merged_list = [0] * (len(list1) + len(list2))
merge(list1, list2, merged_list)
print("Merged list:", merged_list)

#13.4.1
"""
1. Only one disk may be moved at a time.
2. A disk may not be "set aside." It may only be stacked on one of the three
posts.
3. A larger disk may never be placed on top of a smaller one
"""

def moveTower(n, source, dest, temp):
    if n == 1:
        print("Move disk from", source, "to", dest + ".")
    else:
        moveTower(n - 1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n - 1, temp, dest, source)

def hanoi(n):
    moveTower(n, "A", "C", "B")

hanoi(3)

#13.6 - Programming exercises: 1)
def fib(n):
    print(f"Computing fib({n})")
    if n <= 1:
        print(f"Leaving fib({n}) returning {n}")
        return n
    else:
        f = fib(n - 1) + fib(n - 2)
        print(f"Leaving fib({n}) returning {f}")
        return f
result = fib(10)
print("\nResult of fib(10):", result)


#13.6 _ Multiple choice

"""
1. Which algorithm requires time directly proportional to the size of the input?
a) linear search b) binary search
c) merge sort d) selection sort 
"""
#Svar: a): for explanation, see appurtenant PDF

"""
3. Recursions on sequences often use this as a base case:
a) 0 b) 1 c) an empty sequence d) None
"""
#Svar: c): for explanation, see appurtenant PDF
