#ch = int(input('Enter value of ch as 1 or 2 as numbers: '))
#a = []
#if ch == 1:
    #r= float(input('Enter radius of circle: '))
    #a = [r]
#elif ch == 2:
    #l = int(input('enter length of rec: '))
    #w = int(input('enter width of rec: '))
    #a = [l, w]   
#print(a)
#if len(a) == 1:
   # area = (22/7) * (a[0]**2)
    #print(area)
#elif len(a) == 2:
    #area = a[0] * a[1]
    #print(area)

#I was trying to use this:
#if ch == 1:
    #r = float(input('Enter radius of circle: '))
    #a.insert(0, r)  # Insert the radius at index 0
#elif ch == 2:
    #l = int(input('Enter length of rectangle: '))
    #w = int(input('Enter width of rectangle: '))
    #a.insert(0, l)  # Insert the length at index 0
    #a.insert(1, w)  # Insert the width at index 1

""" I was trying to insert 1 as ch value and getting error because a was taking 
    none value type instead of list .
"""

ch = int(input('Enter value of ch as 1 or 2 as numbers: '))
a = []

if ch == 1:
    r = float(input('Enter radius of circle: '))
    a.append(r)
    area = 3.14 * r ** 2
    print(f'The area of the circle is: {area}')
elif ch == 2:
    l = int(input('Enter length of rectangle: '))
    w = int(input('Enter width of rectangle: '))
    a.extend([l, w])
    area = l * w
    print(f'The area of the rectangle is: {area}')
else:
    print('Invalid choice. Enter 1 or 2.')

print(a)