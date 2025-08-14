something = eval(input("Enter amount to deposit --> ")) 

print("Here is a breakdown of the deposit amount:")
print(something // 1000, "- 1000")
something = something % 1000
print(something // 500, "- 500")
something = something % 500
print(something // 200, "- 200")
something = something % 200
print(something // 100, "- 100")
something = something % 100
print(something // 50, "- 50")
something = something % 50
print(something // 20, "- 20")
something = something % 20
print(something // 10, "- 10")
something = something % 10
print(something // 5, "- 5")
something = something % 5
print(something // 1, "- 1")
something = something % 1 