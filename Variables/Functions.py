#def main():
#    printMessage()
#    return

#def printMessage():
#    print("Hello World!")
#    return

##printMessage()
#main()

#def main():
#    printNames()
#    return

#def printNames():
#    names = ['Christopher', 'Susan', 'Danny']
#    for name in names:
#        print(name)
#    return

def main():
    #names = getNames()
    printNames(getNames())
    return

def getNames():
    names = ['Christopher', 'Susan', 'Danny']
    newName = input('Enter a new guest: ')
    names.append(newName)
    return names

def printNames(names):
    for name in names:
        print(name)
    return

main()