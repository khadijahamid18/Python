# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):  # tupple 
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name)) # dictionary
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")



def name(fname, lname, age):
  print("Hellow", fname, lname, age)

name("Khadija", "Hamid", 19)  
  


def name(fname, lname, age):
  pass # if you dont want to write the func body at that time 


