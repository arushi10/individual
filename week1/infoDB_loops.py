ArushiDB = []
# List with dictionary records placed in a list  
ArushiDB.append({  
               "FirstName": "Arushi",  
               "LastName": "Bharadwaj",  
               "DOB": "August 9",  
               "Residence": "San Diego",  
               "Email": "arushi9b@gmail.com",  
               "Owns_Devices":       ["phone","TV","fitbit","laptop"]  
              }) 

# given an index this will print InfoDb content
def print_data(n):
    print(ArushiDB[n]["FirstName"], ArushiDB[n]["LastName"])  # using comma puts space between values
    print("\t", "Devices: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(ArushiDB[n]["Owns_Devices"]))  # join allows printing a string list with separator
    print()


def for_loop():
    for n in range(len(ArushiDB)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(ArushiDB):
        print_data(n)
        n += 1
    return

  # recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(ArushiDB):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def driver():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)  # requires initial index to start while
  print("Recursive loop")
  recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    driver()