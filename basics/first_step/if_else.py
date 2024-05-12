# a = int(input("Enter a intger: ")) #mistake not converted data type into int before 05/05/2024
# b = int(input("Enter another intger: "))
# print (a)
# print(b)
# if a == b:
#     print('Equal')
# if a > b:           #this also gives result but it's not optimised way,.
#     print('greater')
# else:
#     print('lesser')

#alternative

a = int(input("Enter a intger: "))
b = int(input("Enter another intger: "))
if a == b:
    print('Equal')
elif a > b:           #this also gives result but it's  optimised way.
    print('greater')
else:
    print('lesser')