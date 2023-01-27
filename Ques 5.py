print("Enter hyphen separated words: ")
list=[n for n in input().split('-')]
list.sort()
print("Sorted: ")
print("-".join(list))