def palindrome(s):
    return s == s[::-1]
s = input()
if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")