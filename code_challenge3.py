name = input("What is your name? --> ")
fare = float(input("Fare fee --> "))
isStudent = input("Are you currently a student? (Yes / No) ")

if isStudent.lower() == 'yes' :
	discount = fare * .20
	#fare -= discount
	new_fare = fare - discount
	print("Hi", name)
	print("Your Discount is", discount)
	print("Your new fare is", new_fare)
else:
	print("Sorry", name, "You are not eligible for a student discount.")