# string ko upper case mn kr k reverse krna 

# str1 = 'khadija hamid'

# str1 = input("Enter any string: ")

# # lambda returns function object
# rev_upper = lambda string: string.upper() [::-1]

# print(rev_upper(str1)) 



format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num: .2f}" 

print("Int Formatting: ", format_numeric(10000000))
print("Float Formatting: ", format_numeric(999999.365698))  