operator = input("select an operator(+,-,*,/)");
num1 = int(input("enter the first number"));
num2 = int(input("enter the second number"));
if operator=="+":
	result = num1+num2
	print("the sum is",result)
elif operator=="-":
	result = num1-num2
	print("the difference is",result)
elif operator=="*":
	result= num1 * num2
	print("the product is",result)
elif operator=="/":
	result= num1 / num2
	print("the value after divition is",result)
else:
	print("invalid operator")

	




