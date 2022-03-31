#age1 = int(input('Enter your age: '))
#age2 = int(input('Enter another age: '))

# swaps numbers regardless of value
def swap1(age1,age2):
    temp = age1
    age1 = age2
    age2 = temp
    print("Swap 1 Result:{}, {}".format(age1, age2))
    return age1,age2

#returns numbers lowest to highest
def swap2(a, b):
    if a > b:
        b, a = a, b
    print("Swap 2 Result:")
    return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
    if age1 > age2:
        print ("Swap 3 Result:")
        return(age2, age1)
    else:
        print ("Swap 3 Result:")
        return(age1, age2)

def driver():

    swap1(16, 20)
    swap1(9.134, 4)
    swap2(16,20)
    swap2(9.134, 4)
    swap3(16,20)
    swap3(9.134, 4)



if __name__ == "__main__":
    driver()
