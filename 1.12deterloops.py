total=0
for counter in range (5):
	grade=int(input("Please enter a grade:"))
	total=total + grade

average = total/5
print(f'The average for the 5 grades entered is : {average}')
