import math
from math import factorial







def displayMessage(message):
    # Give the user directions for using this program
    THANK_YOU_MESSAGE=''' Thank you for using our calculator'''

WELCOME_MESSAGE= ''''' Thank you for using our calculator -
You will be prompted to enter an equation to solve: it should be entered on a
single line in the format "a + b" - please be sure you leave at least one space between
the operands and the operators. We have also added additional functionality to the calculator.
You now have the following operation availble:\n
"+" addition
"-" subtraction
"/" real division
"//" interger division - also call floor division in python
"%" modulo
"a ** b (take the first operand to the power of the second operand)'''
print(WELCOME_MESSAGE)

def getInfo():
    number1=input("Please enter your equation: ")
    try:
        if number.count(" ") == 2:
           number1,operation,number2 = number.split(" ")
           number1 = int(number1)
           number2 = int(number2)
        else:
            number1,operation = number.split(" ")
            number1 = int(number1)
            number2 = ""
        return number1,number2,operation
    except:
            return 0,0,None
    operation = input("Please enter the operation you wish to perform")


    number1=int(number1)
    number2=int(number2)
    return number1,number2,operation

def calculate(number1,number2,operation):
    if(operation=='+'):
        answer=number1+number2
    elif(operation=='-'):
        answer=number1-number2
    elif(operation=='/'):
        answer=number1/number2
    elif(operation=="*"):
        answer=number1*number2
    elif(operation=="//"):
        answer=number1//number2
    elif(operation=="%"):
        answer=number1%number2
    elif(operation=="**"):
        answer=pow(number1,number2)
    elif(operation=="!"):
        answer=factorial(number1)
    else:
        answer=None
    return answer

def displayResult(number1,number2,operation,answer):
    print(f"The answer to {number1} {operation} {number2} = {answer}")

def detailLoop(keepGoing):

    while keepGoing=="T":
        number1,number2,operation= getInfo()
        if operation is None:
           print ("This equation was not in the correct format.")
        else:
           result = calculate(number1,number2operation)
        if (not result is None):
               displayResult(number1,number2,operation,result)
        else:
             print("We did not recognize the operation you requested")
               
        keepGoing=(input("Do you wish to perform another calculation? (T or F)"))

def finishUp(message):
    print(message)

def main():
    keepGoing="T"
    welcomeMessage= ''''' Thank you for using our calculator -
You will be prompted to enter an equation to solve: it should be entered on a
single line in the format "a + b" - please be sure you leave at least one space between
the operands and the operators. We have also added additional functionality to the calculator.
You now have the following operation availble:\n
"+" addition
"-" subtraction
"/" real division
"//" interger division - also call floor division in python
"%" modulo
"a ** b (take the first operand to the power of the second operand)'''

 # 2.x way
# if_name_= "_main_":
# main()
main()
