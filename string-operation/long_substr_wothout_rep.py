'''
### 7. Longest Substring Without Repeating Characters
- **Input:** `"abcabcbb"`  
- **Output:** `3` (`"abc"`)  
- 💡 *Common in interviews — sliding window technique.*

---
'''

def longest_unique_substring(s):
    longest = 0
    current = ""

    for ch in s: #abcabcdd
        if ch in current:
            # Cut the string from the ch
            # aracter after the first occurrence
            print("current in ",current)
            current = current[current.index(ch) + 1:]
            print("current",current)
                  
        current += ch
        print("current if ",current)

        longest = max(longest, len(current))

    return longest

# Example usage:
input_str = input("Enter a string: ")
print("Length of longest substring without repeating characters:", longest_unique_substring(input_str))
