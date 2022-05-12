import os
from time import sleep
sleep(5)
os.system("cls")
sleep(5)
os.getcwd()
os.chdir(r"C:\Users\niasco6566\Desktop\week 3")
os.getcwd()
open("test.txt","w+")
myFile=open("testFile.txt","w+")
os.listdir()
type(os.listdir())
inputLines=[]
linesNumer=int(input("How many lines of text would you like"))
linesNumber=linesNumer
for counter in range(linesNumber):
    inputLines.append(input("Enter line 4:"))
    type(inputLines)
for word in inputLines:
	print(word,end=" ")
for word in inputLines:
	myFile.write(word+" ")
myFile.close()
