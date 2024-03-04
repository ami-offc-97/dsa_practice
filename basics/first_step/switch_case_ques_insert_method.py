ch = int(input('Enter value of ch as 1 or 2: '))
a = []

if ch == 1:
    r = float(input('Enter radius of circle: '))
    a.insert(0, r)  # Insert the radius at index 0
    area = 3.14 * a[0]**2  # Calculate area of circle
    print(f"Area of circle: {area}")
elif ch == 2:
    l = int(input('Enter length of rectangle: '))
    w = int(input('Enter width of rectangle: '))
    a.insert(0, l)  # Insert the length at index 0
    a.insert(1, w)  # Insert the width at index 1
    area = a[0] * a[1]  # Calculate area of rectangle
    print(f"Area of rectangle: {area}")
else:
    print("Invalid choice")

"""In my other script I was not able to correctly use insert method so created this script and it works
     perfectlty fine.
"""   