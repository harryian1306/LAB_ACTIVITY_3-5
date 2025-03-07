assign_grade = int(input("What is your grade?"))
if assign_grade >= 101:
	print("Invalid score! Please enter a value between 0 and 100.")
elif assign_grade >= 90:
	print("Wow!!! You got an A. Congratulations!")
elif assign_grade >= 80:
	print("You got a B. Not Bad.")
elif assign_grade >= 70:
	print("Uhhh, you got a C. Better luck next time.")
elif assign_grade >= 60:
	print("Oh no, you got a D.")
elif assign_grade >= 59:
	print("I'm sorry, but you got an F, which means you failed.")
else:
	print("Invalid score! Please enter a value between 0 and 100.")