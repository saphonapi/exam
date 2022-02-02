def isPalindrome(s):
    return s == s[::-1]
 
print("Please enter a string to check  palindrome:") 
x = input()
ans = isPalindrome(x)
 
if ans:
    print("Yes")
else:
    print("No")