a = input("Enter a intger: ")
b = input("Enter another intger: ")
if a == b:
    print('Equal')
if a > b:           #this also gives result but it's not optimised way,.
    print('greater')
else:
    print('lesser')

#alternative

a = input("Enter a intger: ")
b = input("Enter another intger: ")
if a == b:
    print('Equal')
elif a > b:           #this also gives result but it's  optimised way.
    print('greater')
else:
    print('lesser')