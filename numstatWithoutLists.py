# numstat.py

# Read integer numbers from a file and determine the
# sum, count, average, maximum, minimum, and range.
# Each number is an a separate line in the file.

# This solution does not use lists.


# Loop the program
while (True):
    
    # Initialize variables
    number_sum = 0
    number_count = 0
    number_average = 0
    number_maximum = 0
    number_minimum = 0
    number_range = 0

    try:
        # Ask the user for a file of random numbers
        number_file_name = input("Enter the name of the file you would like to process: ")

        # Open the file
        number_file = open(number_file_name, "r")

        # Use a variable to indicate when the first line of the file is being read
        is_first_number = True

        # For each line in the file
        for number in number_file:
            # Convert the line to an integer
            number = int(number)

            # If this is the first number in the file...
            if (is_first_number):
                # We'll say it is both the max and the min
                number_maximum = number
                number_minimum = number
                # Turn is_first_number flag to False so this doesn't happen again
                is_first_number = False


            # Add the number to the running sum
            number_sum += number

            # Count the number
            number_count += 1

            # Determine if it is greater than the max
            if (number > number_maximum):
                number_maximum = number
            # Determine if it is lesser than the min
            if (number < number_minimum):
                number_minimum = number


        # Calculate the average
        number_average = number_sum / number_count
        # Calculate the range
        number_range = number_maximum - number_minimum

        # Close the file
        number_file.close()

    # If there's a problem reading the file, print an error
    except Exception as err:
        print ('An error occurred reading', number_file_name)
        print ('The error is', err)

    # If the file was read successfully...
    else:
        # Print the calculated statistics
        print("File name:", number_file_name)
        print("Sum:", number_sum)
        print("Count:", number_count)
        print("Average:", number_average)
        print("Maximum:", number_maximum)
        print("Minimum:", number_minimum)
        print("Range:", number_range)

        # Ask to try again
        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break


