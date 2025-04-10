def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return str2 in (str1 + str1)

# Input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Output
if is_rotation(s1, s2):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")
