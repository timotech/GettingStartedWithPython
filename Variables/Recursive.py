import turtle
#turtle.forward(100)
#turtle.right(90)
#turtle.color('red')
#turtle.forward(100)

#Draw a square
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)

#Use for loop instead
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)
#turtle.color('red')
#turtle.forward(200)

#nbrsides = 4
#for steps in range(nbrsides):
#    turtle.forward(100)
#    turtle.right(360/nbrsides)
#    for x in range(nbrsides) :
#        turtle.forward(50)
#        turtle.right(360/nbrsides)

#Polygons(5)
#nbrsides = 20
#for steps in range(nbrsides):
#    turtle.forward(100)
#    turtle.right(360/nbrsides)
#    for x in range(nbrsides) :
#        turtle.forward(50)
#        turtle.right(360/nbrsides)

#Specify different index instead of 0
#for x in range(1, 4):
#    print(x)

#specify step value
#for x in range(1,10,2):
#    print(x)

#do a foreach
#for x in [1,2,3,4,5]:
#    print(x)

#for colour in ['red', 'blue', 'green', 'yellow']:
#    turtle.color(colour)
#    turtle.forward(100)
#    turtle.left(90)

###########
#Using the while loop
###########
#answer = '0'

#while answer != '4':
#    answer = input('What is 2 + 2' )
#print("You are write!")

counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter = counter + 1