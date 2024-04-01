def my_decorator(func):
    def wrapper():
        print("Before calling the func")
        func()
        print("After calling the func")
    return wrapper()

@my_decorator
def my_function():
  print("Inside the function")
my_function