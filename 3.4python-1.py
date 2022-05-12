import os
import csv
import subprocess as s

print (os.getcwd())
os.chdir(r"C:\Users\niasco6566\Desktop\week 3")
print(os.getcwd())
os.listdir()
csvFile=open("example.csv","r")
fileContent=csv.reader(csvFile)
fcList=list(fileContent)
for element in fcList:
    print(element)

myFile=open("myfile.csv","w",newline="")
os.listdir()
breakfast=["oatmeal","bacon","eggs","ham"]
write=csv.writer(myFile)
write.writerow(breakfast)
write.writerow([4,2,1])
myFile.close()
myFile=open("myFile2.csv","w",newline="")
write=csv.writer(myFile,delimiter="\t",lineterminator="\n\n")
write.writerow(["breakfast1","breakfast2","breakfast3"])
write.writerow(["oatmeal","waffles","bacon & eggs","custom"])
write.writerow(["3$","5$","7$","price varies"])
wordPad=s.Popen([r"C:\Program Files\Windows NT\Accessories\wordpad.exe","myFile.csv"])
