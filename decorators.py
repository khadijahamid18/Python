def greet(fx):
  # In case of arguments
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

# If there are no arguments
#     def mfx():
#     print("Good Morning")
#     fx()
#     print("Thanks for using this function")
#   return mfx

# *args: to pass arguments as a tupple in key value pairs
# ** kwargs: to pass arguments as a dictionary in key value pairs

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)




## LOGGING FUNCTION

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b


# In this example, the log_function_call decorator takes a function as an argument and returns 
# a new function that logs the function call before and after the original function is called.
