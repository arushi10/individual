# Function to find prime numbers in imperative

#test values
min = 1
max = 11

def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()


def primes():
  print("Imperative results:")  
  findprimes(min, max + 1)



# Function to find prime numbers in OOP

#test values
min = 1
max = 11

class Primes:
    def __init__(self):
        pass

    def __call__(self, min, max):
      print("OOP results:") 
      for Number in range(min, max + 1):
              count = 0
              for i in range(2, (Number // 2 + 1)):
                  if (Number % i == 0):
                      count = count + 1
                      break
              if (count == 0 and Number != 1):
                  print(" %d" % Number, end='  ')

def driver():
    primes()
    primes_of = Primes() # object instantiation and run __init__ method
    print(primes_of(min, max)) # object running __call__ method

if __name__ == "__main__":
    driver()