# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

# Program to display the Fibonacci sequence up to n-th term

# Python program to display the Fibonacci sequence

# recurring function
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def driver():
    # take user input to determine number of terms to print
    nterms = int(input("How many terms? "))

    # check if the number of terms is valid (try-except)
    if nterms <= 0:
       print("Plese enter a positive integer")
    else:
       print("Fibonacci sequence:")
       for i in range(nterms):
           print(recur_fibo(i))

if __name__ == "__main__":
    driver()