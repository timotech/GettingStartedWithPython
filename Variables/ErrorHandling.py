#firstNumber = float(input("enter a number "))
#secondNumber = float(input("enter second number "))
#try:
#    result = firstNumber/secondNumber
#    print(result)
#except:
#    print("Something went wrong")

import sys

#firstNumber = float(input("enter a number "))
#secondNumber = float(input("enter second number "))
#try:
#    result = firstNumber/secondNumber
#    print(result)
#except:
#    error = sys.exc_info()[0]
#    print(error)
#finally:
#    print("I will always run")

firstNumber = float(input("enter a number "))
secondNumber = float(input("enter second number "))
try:
    result = firstNumber/secondNumber
    print(result)
except ZeroDivisionError:
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]
    print("Something went wrong: " + error)
finally:
    print("I will always run")