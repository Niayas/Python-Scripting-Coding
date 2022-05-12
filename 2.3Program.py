def setup(message):
    # Give user directions for using this program
    print(message)

def getInfo():
    number1=input("Please enter your first number: ")
    number2=input("Please enter your second number: ")
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
    else:
        answer=number1*number2
    return answer

def displayResult(number1,number2,operation,answer):
    print(f"The answer to {number1} {operation} {number2} = {answer}")

def detailLoop(keepGoing):

    while keepGoing=="T":
        number1,number2,operation= getInfo()
        result = calculate(number1,number2,operation)
        displayResult(number1,number2,operation,result)
        keepGoing=(input("Do you wish to perform another calculation"))

def finishUp(message):
    print(message)

def main():
    keepGoing="T"
    welcomeMessage= ''''' Thank you for using our calculator - it will ask you for two numbers, then prompt your for the operations (+,-,/,*).
The calculator will display teh result and ask you if you want to do another calculation. If not, the program will end.\n '''

    setup(welcomeMessage)
    detailLoop(keepGoing)
    finishUp("Thank you for using our calculator!")
# 2.x way
# if_name_= "_main_":
# main()
main ()
