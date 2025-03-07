classify_age = int(input("How old are you?"))
if classify_age >= 123:
	print("I don't think anyone reached this age yet.")
elif classify_age >= 65:
	print("You are a senior citizen.")
elif classify_age >= 20:
	print("You are an adult.")
elif classify_age >= 13:
	print("You are a teenager.")
elif classify_age >= 0:
	print("You are a child.")
else:
	print("This age doesn't exist.")


	