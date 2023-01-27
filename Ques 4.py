str=input("Enter the string to be checked: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
flag=0
for char in alphabet:
    if char not in str.lower():
        flag=1
if flag==0:
    print("It is a pangram")
else:
    print("It is not a pangram")

#Question 5
print("Enter hyphen separated words: ")
list=[n for n in input().split('-')]
list.sort()
print("Sorted: ")
print("-".join(list))