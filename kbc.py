# # Kon Banay ga Karoor pati   KBC

questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")










# Kon Banay ga Karoor pati   KBC

# print("**********KBC**********")
# print("There are going to be 4 total questions")
# print("If you answered 1 question correctly you'll get 5,000 Rs")
# print("If you answered 2 questions correctly you'll get 10,000 Rs")
# print("If you answered 3 questions correctly you'll get 15,000 Rs")
# print("If you answered 4 questions correctly you'll get 20,000 Rs") 
# print("\n")


# print("1st Question: What is the currency of USA?")
# one = input("Answere: ")
# if(one == "dollar"):
#     count = print("Correct answer, You won 5,000 Rs")
# else:
#     print("Sorry, wrong answer")    
# print("\n")

# print("2nd Question: What is the currency of Saudi Arabia?")
# two = input("Answere: ")
# if(two == "rayal"):
#     count = print("Correct answer, You won 5,000 Rs")
# else:
#     print("Sorry, wrong answer")
# print("\n")

# print("1st Question: What is the currency of UK?")
# three = input("Answere: ")
# if(three == "pound"):
#     count = print("Correct answer, You won 5,000 Rs")
# else:
#     print("Sorry, wrong answer")        
# print("\n")

# print("1st Question: What is the currency of Pakistan?")
# four = input("Answere: ")
# if(four == "rupees"):
#     count = print("Correct answer, You won 5,000 Rs")
# else:
#     print("Sorry, wrong answer")    
# print("\n")

# if(count == 1):
#     print("Congratulations, You won 5,000 Rs")
# elif(count == 2):
#     print("Congratulations, You won 10,000 Rs")
# elif(count == 2):
#     print("Congratulations, You won 15,000 Rs")
# elif(count == 2):
#     print("WINNER, Congratulations, You won 20,000 Rs")
# else:
#     print("Sorry, you failed, all answers were wrong")            



