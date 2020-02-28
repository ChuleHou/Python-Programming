# numstatWithLists.py

# Read integer numbers from a file and determine the
# sum, count, average, maximum, minimum, and range.
# Each number is an a separate line in the file.

# This solution uses lists.


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

        # Read the file's contents as a list of strings
        unconverted_numbers = number_file.readlines()

        # Create an empty list to store the converted numbers
        converted_numbers = []

        # Convert the strings to integers and store them in converted_numbers list
        for number in unconverted_numbers:
            converted_numbers.append(int(number))


        # Determine the sum
        number_sum = sum(converted_numbers)
        # Determine the count
        number_count = len(converted_numbers)
        # Determine the max
        number_maximum = max(converted_numbers)
        # Determine the minimum
        number_minimum = min(converted_numbers)
        
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


