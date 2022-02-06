def smallest_subarray_sum(s, arr):
  shortest_length = 10000
  sum = 0
  start = 0
  for i in range(len(arr)):
    sum += arr[i]

    while sum >= s:
      shortest_length = min(shortest_length,i - start + 1)
      sum -= arr[start]
      start += 1

  return shortest_length

print(smallest_subarray_sum(8, [3, 4, 1, 1, 6]))