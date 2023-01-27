s=input("Enter string to be checked: ")
a=""
for i in s:
    a=i+a
if a==s:
    print("the given string is a palindrome")
else:
      print("the given string is not  a palindrome")