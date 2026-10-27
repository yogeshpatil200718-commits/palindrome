import sys

word = sys.argv[1]

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")