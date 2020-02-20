#This program generates some random numbers and writes some data to a file
import random

do_input = True
#Accept user input for the quantity of random numbers to generate.
while(do_input):
    try:
        randomnum = int(input("How mant random numbers do you want? "))
        if(randomnum<0):
            print("Negative number is not allowed")
            continue
    except ValueError:
        print("The value you enter is invalid. Only positive value is valid")
    else:
        break
#Accept user input for the lower bound of the random numbers’ range.
while(do_input):
    try:
        lower_bound = int(input("What is the lowest the random number should be: "))
        if(lower_bound<0):
            print("Negative number is not allowed")
            continue
    except ValueError:
        print("The value you enter is invalid. Only positive value is valid")
    else:
        break
#Accept user input for the upper bound of the random numbers’ range.
while(do_input):
    try:
        upper_bound = int(input("What is the hightest the random number should be: "))
        if(upper_bound<0):
            print("Negative number is not allowed")
            continue
    except ValueError:
        print("The value you enter is invalid. Only positive value is valid")
    else:
        break


try:
    infile = open('/Users/chulehou/Desktop/randomnum.txt', 'w')
    for count in range(randomnum):
        randomnum_write = random.randint(lower_bound,upper_bound)
        infile.write(str(randomnum_write) + '\n')
    infile.close
    print("The random numbers were written to randomnum.txt")
except:
    print("An error were occurred.")
