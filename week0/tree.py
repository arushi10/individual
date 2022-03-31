#christmastree
def christmastree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*',end='*')
        print(' ')
def trunk(n):
  for i in range(n):
    for j in range(n-1):
      print(' ', end =' ')
    print('* *')
  # Input and Function Call

def driver():
    row = int(input('Enter number of rows: '))
    christmastree(row)
    trunk (row)

if __name__ == "__main__":
    driver()