# def calculateSum(num1, num2):
#     sum = num1 + num2
#     print('The sum is: ' ,sum)    

# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))

# calculateSum(number1, number2)



# Lambda Function       

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

sum = lambda x, y: x + y

result = sum(number1, number2)

print("The sum of", number1, "and", number2, "is: ", result)
