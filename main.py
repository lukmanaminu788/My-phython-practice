first_number = int(input("enter_1st_number:"))
second_number = int(input("enter_2nd_number:"))
sum  = first_number + second_number
difference =  first_number - second_number
product =  first_number * second_number
if second_number == 0:
	print("sum = ",sum)
	print("difference = ",difference)
	print("product = ",product)
	print("division = syntax error")
else:
	division = first_number / second_number
	print(f"sum = {sum}\ndifference = {difference}\nproduct = {product}\ndivision = {division}")