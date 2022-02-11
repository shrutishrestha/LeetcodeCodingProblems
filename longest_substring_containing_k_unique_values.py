def longest_substring_with_k_distinct(str1, k):

    start = 0
    substring = []
    longest_length = 0
    for i in range(len(str1)):
        substring.append(str1[i])
        if len(set(substring))>k :
            substring.pop(0)

            start += 1
        longest_length = max(len(substring), longest_length)
    return longest_length