i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break # if break then else will not execute

else:
  print("Sorry no i")



for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

#output
# iteration no 1 in for loop
# iteration no 2 in for loop
# iteration no 3 in for loop
# iteration no 4 in for loop
# iteration no 5 in for loop
# else block in loop
# Out of loop