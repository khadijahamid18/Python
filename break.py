# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)


# for i in range(12):
#   if(i == 10):
#   break
#   print("5 X", i, "=", 5 * i)


for i in range(12):
  
  print("5 X", i, "=", 5 * i)  # 0 to 10
  if(i == 10):
     break



for i in range(12):
  
  print("5 X", i + 1, "=", 5 * (i+1))  # 1 to 10
  if(i == 10):
     break

  
# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i%100 == 0):
#     break