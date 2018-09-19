area = 0 #Initialize a variable to determine which datatype it is
width = 15
height = 20

area = width * height
print("The area of height and width are %.2f" % area)
print()
#Using a different way using .format syntax to print a float (f), d for decimal i.e int
print('The area of height and width is {0:.2f}'.format(area))
print()
#Formatting multiple numbers
print("Here are 3 numbers ! The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))
print()
print("""There once was a movie star icon
who preferred to sleep with the light on.
They learned how to code
a device that sure glowed
and lit up the night using python!""")

#l = (1, 2, 5, 6, 4, 3)
#print(l[int(-1/2):int(7/2)])

#numbers = [1,2,3,4,5,1,2,3,4,5,0,1]
#print(len(set(numbers))/2)

#name = input("What is your name? ")
#print(name)

#x = sum(n/2 for n in range(2,6,2))
#print(x)

#i = 0
#while i<3:
#    print(++i)
#    i += 1
#    print(i+1)

#print(list("hello"))

#bool1 = True
#bool2 = False
#bool3 = False

#if bool1 or bool2 and bool3:
#    print(bool1)
#else:
#    print(bool2)