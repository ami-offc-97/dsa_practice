char = input("Enter a character: ")
if char>= "A" and char<= "Z":
    print(1)
elif char>= "a" and char<= "z":
    print(0)
else:
    print(-1) 
 
#alternative way
      
if char.isupper():
    print(1)
elif char.islower():
    print(0)
else:
    print(-1)       