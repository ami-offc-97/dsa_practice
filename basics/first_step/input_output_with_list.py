# print("Enter the list elements ")
# List_num = list(map(int, input().split()))
# print("List elemnts are : ")
# print(List_num)

#alternative way
n = int(input("Enter the number of elements in list : "))
List = list()
print("enter the list elements")
for i in range(0,n):
    List.append(int(input()))
print(List)    