class Solution:
    def __init__(self):
      pass

    def __call__(self, test):
      var = "".join(reversed(test))
      print (var)
      if (var == test): 
          return True
      return False
      print(test)

def driver():
    palindrome_of = Solution() # object instantiation and run __init__ method

    # Test Cases
    #true
    test = "racecar"
    print(palindrome_of(test))

    #true
    test = "amanaplanacanalpanama"
    print(palindrome_of(test))

    #false
    test = "APCSP"
    print(palindrome_of(test))


if __name__ == "__main__":
    driver()