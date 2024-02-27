# Before was not convinient

# letter = "Hey my name is {} and I am from {}" yahan name mn country a jae ga or country name according to call

letter = "Hey my name is {1} and I am from {0}" # difficult for lengthy strings
country = "India"
name = "Harry"

print(letter.format(country, name))

# F-strings
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!" # 49.10 (round off kr deta.2 mens 2 values tak)
print(txt)
# print(txt.format())

print(f"{2 * 30}") # returns 60 as string 
print(type(f"{2 * 30}")) # returns sting