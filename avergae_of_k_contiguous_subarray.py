# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

def func(k, arr):
    average_list = []
    average = 0
    start = 0
    for i in range(len(arr)):
        average += arr[i]
        if i>=k-1:
            average_list.append(average/k)
            average = average - arr[start]
            start += 1
    return average_list
print(func(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))

#
# time complexity = O(N) # for loop
# space complexity = O(1) #O(1) means that it takes a constant time, like 14 nanoseconds, or three minutes no mat