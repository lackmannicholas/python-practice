'''
Remove Adjacent Duplicates in String. 
You are given a string s and an integer k. Write a function to remove k adjacent duplicates from s where the "adjacent" characters are equal.

For instance, if k is 3 and the string is "daaabbbaa", since we have "aaa" and "bbb" as adjacent triples, the function should transform the string to "daa", removing the "bbb" first and then the remaining "aaa".
'''
# Runtime: Big O(N^2) by iterating through all chars in the string potentially N/2 times
# Memory: Big O(N) creating a result string of N length
def identify_adjacent(s: str, k: int) -> str:
    if len(s) < k or k < 2:
        return s
    
    result = s
    while True:
        prev = result
        for i in range(len(result)):
            if has_adjacent_duplicates(i, k, result):
                result = result.replace(result[i]*k, '')
                break

        if prev != result:
            continue
        break

    return result

# Runtime: Big O(N) by iterating through all chars in the string
# Memory: Big O(k) creating a substring of k chars
def has_adjacent_duplicates(i: int, k: int, s: str) -> bool:
    substring = s[i]*k
    if s.find(substring) > -1:
        return True
    return False
    
# debug your code below
print(identify_adjacent("aaabbbacd", 3))