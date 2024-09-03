'''
Remove Adjacent Duplicates in String. 
You are given a string s and an integer k. Write a function to remove k adjacent duplicates from s where the "adjacent" characters are equal.

For instance, if k is 3 and the string is "daaabbbaa", since we have "aaa" and "bbb" as adjacent triples, the function should transform the string to "daa", removing the "bbb" first and then the remaining "aaa".
'''
# Runtime: Big O(N) by iterating through all chars in the string
# Memory: Big O(N) creating a result string of N length
def identify_adjacent(s, k):
    stack = []  # Initialize an empty stack to store <char, count> pairs

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1  # Increment the count of the top element if it's the same character
        else:
            stack.append([char, 1])  # Push a new character with count 1 onto the stack
        if stack[-1][1] == k:
            stack.pop()  # Remove the top element if its count reaches k

    # Reconstruct the result string from the stack
    return ''.join(char * count for char, count in stack)
    
# debug your code below
print(identify_adjacent("aaabbbacd", 3))