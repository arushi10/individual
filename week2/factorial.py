

class Factorial:
    def __init__(self):
      pass

    def __call__(self, number):
        if number == 0:
            return 1
        else:
          for i in range(1, number):
            number = number * i
          return number

def driver():
    number = int(input("What number?"))
    factorial_of = Factorial() # object instantiation and run __init__ method
    print(factorial_of(number)) # object running __call__ method

if __name__ == "__main__":
    driver()