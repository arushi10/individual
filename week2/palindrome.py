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


# true
# print("A man, a plan, a canal -- Panama!")
# print(num.palindrome_of())

# #false
# list_2 = Solution([6 , 3 , 4, 6])
# print("6 , 3 , 4, 6")
# print(list_2.palindrome_of())

# #true
# list_3 = Solution(["racecar"])
# print("racecar")
# print(list_3.palindrome_of())

# #true
# list_4 = Solution([1])
# print("1")
# print(list_4.palindrome_of())