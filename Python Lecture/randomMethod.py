import random 
#  this function generates 20 random number 
#  end = " space " means next mn space
#  0.4 means decimal k bas 4 no
#  0 means start with 0
#  5 means total digits including decimal must be 5
# for i in range(20):
#     print("%05.4f" %random.random(), end=' ' )  
#     print() 



#  random.uniform method
#  1 to 10 range

# for i in range(20):
#     print("%05.4f" %random.uniform(1, 100), end=' ' )    # 1 to 100 k darmayan 20 random no generate hon gy
#     print()



# #  random.seed method
# for i in range(20):
#     random.seed(1)   
#     print("%05.4f" %random.random(), end=' ' )   
#     print()

# # random.randint
# for i in range(20):
#     print("%05.4f" %random.randint(-20, 40), end=' ' )   
#     print()    

# # random.randrange
# for i in range(20):
#     #  0 to 100 and multiple of 5
#     print("%05.4f" %random.randrange(0, 100, 5), end=' ' )   
#     print()    

# for i in range(20):
#     #  0 to 20 and multiple of 4
#     print("%05.4f" %random.randrange(0, 20, 4), end=' ' )   
#     print()    


# # Multiple of 10 ( 10 ka table)
# range(10, 100, 10)

# # random.choice
# #  a-z characters mn randomly 3 choose krny hain 
# #  or cities choose and name repeat ho sakty hain
# cityList = ['lahore', 'islamabad', 'karachi', 'naran', 'murree', 'multan']
# for i in range(10):
#     cityItem = random.choice(cityList)
#     print("Randomly selected item from city list is - ", cityItem)



# #  random.sample method
# dataList = range(10, 100, 10)
# print("Initial data list - ", dataList)
# dataSample = random.sample(dataList, k=5)
# print("Sample data list = ", dataSample)


# #  random.shuffle
# import string
# charSet = list(string.ascii_letters + string.digits + "()+-$%^&&")
# print(charSet)
# random.shuffle(charSet)
# passwordLength = int(input("How long your password should be? : "))
# password = []
# for i in range(passwordLength):
#     password.append(random.choice(charSet))
# random.shuffle(password)
# print(password)
# print("". join(password)) 


# # 
# # encode = byte code mn convert deta hy title ko
# # fernet = extension
# # install cryptography
# # google : pypi install cryptography 
# # pip install cryptography , run in cmd
# from cryptography.fernet import Fernet
# title = "Simulation and Modelling with Python"
# title = title.encode()
# print(title)
# secretKey = Fernet.generateKey()
# fernetObj = Fernet(secretKey)
# encTitle = fernetObj.encrypt(title)
# print("My last book title= ", title)
# print("Title encrypted= ", encTitle)

# decTitle = fernetObj.decrypt(encTitle)
# decTitle = decTitle.decode('utf-8')
# print("Title decrypted= ", decTitle)




# uniform distribution
import numpy as np
import matplotlib.pyplot as plt
# a =1 
# b =100
# N = 1000

# x1 = np.random.uniform(a, b, n)
# plt.plot(x1)
# plt.show()

# plt.figure()
# plt.hist(x1, density= True, histtype='stepfilled', alpha= 0.2)
# plt.show()



# # binomial distribution
# # 2 parameters hoty binomial k liye 
# # 1: probability of success : 0.5
# # 2: probability of failure : 0.5
# N = 10000
# n = 10
# p = 0.5
# p1 = np.random.binomial(n, p, N)
# plt.plot(p1)
# plt.show()
# plt.figure()
# plt.hist(p1, density= True, alpha = 0.8, histtype="bar", color="green", ec="black")
# plt.show()



# Normal Distribution
# bell shaped
import seaborn as sns

mu = 10
sigma = 2
p1 = np.random.normal(mu, sigma, 1000)

mu = 5
sigma = 2
p2 = np.random.normal(mu, sigma, 1000)

mu = 15
sigma = 2
p3 = np.random.normal(mu, sigma, 1000)

plt.plot(p1)
plt.show()

plt.figure()
plt.hist(p1, density= True, alpha = 0.8, histtype="bar", color="green", ec="black")
plt.show()
