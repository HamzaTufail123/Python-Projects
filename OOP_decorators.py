class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def avg(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98,78, 89)
print(s1.avg)
s1.phy = 67
print(s1.phy)
print(s1.avg)

# @getter
# @setter

# ++++++++++++++++++++++++++++++++++++++++++++++
import time

def timer(func):
    def warpper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result

    return warpper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

# ++++++++++++++++++++++++++++++++++++++

def debug(func):
    def wrapper(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_val} and kwargs {kwargs_val}")
        return func(*args, **kwargs)

    return wrapper

@debug
def hello():
    print("Hello")

hello()

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}!, {name}")

greet("Hamza")

# +++++++++++++++++++++++++++++++++++++++++++++++++
import time
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
      if args in cache_value:
          return cache_value[args]
      result = func(*args)
      cache_value[args] = result
      return result
    return wrapper

@cache
def long_running_function(a, b):
   time.sleep(4)
   return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))

# ++++++++++++++++++++++++++++++++++++++
import time
def authenticate(func):
    def wrapper(*args):
        logged_in = False
        if args[0] == "1":
            logged_in = True
            print(f"Islogin: {logged_in}")
            return func(*args)
        else:
            logged_in = False
            print(f"Access denied.Response: {logged_in}")
            return

    return wrapper

@authenticate
def checker(n):
    time.sleep(4)
    print("Executed.")

val = input("Enter binary number(1/0) to check user Isloggedin? ").strip()
checker(val)

# ++++++++++++++++++++++++++++++++++++++

import time

def Logging(func):
    def wrapper(*args):
        print("Function Strated. ")

        return func(*args)

    return wrapper

@Logging
def simple():
    time.sleep(3)
    print("Function Ended. ")
simple()

# +++++++++++++++++++++++++++++++++++++++++
import time
import math

def Execution_Timer(func):
    def wrapper(*args):
        before = time.time()
        result = func(*args)
        after = time.time()
        total = math.floor(after - before)
        print(f"\nBefore execution time: {before}")
        print(f"After execution time: {after}")
        print(f"Total execution time: {total}")
        return result
    return wrapper

@Execution_Timer
def check():
    time.sleep(3)
    print("Function executed.")
check()


# ++++++++++++++++++++++++++++++++++++

def Repeat_Decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            print(f"Executed: ({i + 1})")
            func(*args, **kwargs)
    return wrapper

@Repeat_Decorator
def run_time():
    print("Function is own track.")
run_time()


# ++++++++++++++++++++++++++++++++++++++++++++
import time

def authentication(func):
    def wrapper(password):
        print("Password Checking...")
        time.sleep(4)
        if password == "taha2025":
            print("User login. ")
        else:
            print("Access denied. ")

    return wrapper

@authentication
def check(n):
    print("Password matched sucessfully. ")

user_input = input("Enter user password: ").strip().lower()
check(user_input)


# +++++++++++++++++++++++++++++++++++++
def authentication(func):
    def wrapper(*args):
        ## all check is iterated 
        ## isinstance check that all values are int 
        check_integer = all(isinstance(arg, int) for arg in args) 
        if check_integer == True:
            return func(*args)
        else:
            print("Error: Only integer are allowed. ")
    return wrapper
@authentication
def add(a,b, c):
    return a + b + c
print(add(1,2,3))
print(add(1,2,"hello"))


