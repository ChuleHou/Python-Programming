#Create a program called numstat2.py that reads a series of integer numbers from a file and determines and displays the following:
#Name of the file.
#Sum of the numbers.
#Count of how many numbers are in the file.
#Average of the numbers. The average is the sum of the numbers divided by how many there are.
#Maximum value.
#Minimum value.
#Range of the values. The range is the maximum value minus the minimum value.
#Median of the numbers.
#Mode of the numbers.

while (True):
    
    # Initialize variables
    number_sum = 0
    number_count = 0
    number_average = 0
    number_maximum = 0
    number_minimum = 0
    number_range = 0
    number_median = 0
    number_key = 0
    number_mode = 0

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

        #Check the file whether is empty
        if len(converted_numbers) == 0:
            print ('No numbers could be find in the file:', number_file_name)
            continue
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
        #Calculate the median
        sorted_numbers = converted_numbers.sort()
        index = (number_count-1)//2
        if(number_count%2):
            number_median = converted_numbers[index]
        else:
            number_median = (converted_numbers[index] + converted_numbers[index + 1])/2.0
        
        #Calculate the mode
        number_dictionary = {}
        for number in converted_numbers:
            if number in number_dictionary:
                number_dictionary[number] +=1
            else:
                number_dictionary[number] = 1   
           
        count = number_dictionary[number] 
        modeList = []
        for number in number_dictionary:
            if number_dictionary[number] >= count:
                count = number_dictionary[number]
        for number in number_dictionary:
            if number_dictionary[number] == count:           
                modeList.append(int(number))


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
        print ("Meidan:", number_median)
        print("Mode:", modeList)

    # Ask to try again
    calculate_again = input("Would you like to evaluate another file? (y/n) ")
    if (calculate_again != "y"):
        break
