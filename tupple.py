tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup)) # 7
print(tup[0])
print(tup[-1]) # print(tup[len(tup) - 1]) = 7 -1 = 6
print(tup[2])
# print(tup[34])

# in keyword
if  3421 in tup:
  print("Yes 342 is present in this tuple") # ye ni chalay ga bcz condition is false

if "re" in "green":
  print("Yes re exists in green")  

# slicing returns new tupple  
tup2 = tup[1:4] # 1 to 3 tak chalay ga means 2, 76, 342 will print
print(tup2)

tup3 = tup2[1:3] # tup2 = [2, 76, 342] 
print(tup3) # 76, 342


tup = [i for i in range(10)] # 0 - 9
print(tup)


tup = [i%2==0 for i in range(10)] # returns true if num is even false otherwise
print(tup)





###                                         OPERATIONS ON TUPPLE


tuple1 = (0, 1, 3, 2, 2, 31, 1, 3, 2, 3, 3)
res = print((tuple1.count(3))) # 4
res = print(tuple1.index(3)) # 2
# res = print(tuple1.index(311)) # error
res = print(tuple1.index(3, 4, 8)) # 7
res = len(tuple1)
print('Count of 3 in tuple1 is:', res) # 11