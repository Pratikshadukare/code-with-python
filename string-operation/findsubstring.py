"""
Task:
Write a function to find the first occurrence of a substring (needle) inside another string (haystack) without using built-in methods like .find() or .index().

If the substring exists, return the starting index of the first match.
If it doesn't exist, return -1.
"""

def custom_strstr(haystack: str, needle: str) -> int:
    if not needle:
        return 0  # Empty needle always matches at index 0

    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1  # If not found


# Test cases
if __name__ == "__main__":
    haystack = input("Enter the main string (haystack): ")
    needle = input("Enter the substring to search (needle): ")
    result = custom_strstr(haystack, needle)
    if result != -1:
        print(f"Substring found at index: {result}")
    else:
        print("Substring not found.")
