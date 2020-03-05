# numstat2.py

# Load numbers from a file where each number is on a separate line.
# Calculate statistics about the numbers.

# Instead of having one continuos block of code, functions are
# used to implement the capabilities of this program.
# Functions make it easier to focus on solving smaller, individual
# problems.

# Determine the maximum values from the list of numbers.
def maximum_value(numbers):
    is_first = True
    maximum = None
    
    for number in numbers:
        if (is_first):
            maximum = number
            is_first = False
        else:
            if (number > maximum):
                maximum = number
    return maximum           

# Determine the minimum values from the list of numbers.
def minimum_value(numbers):
    is_first = True
    minimum = None

    for number in numbers:
        if (is_first):
            minimum = number
            is_first = False
        else:
            if (number < minimum):
                minimum = number
    return minimum

# Calculate the range from list of numbers.
# The functions to determine the maximum and minimum are
# called then the range is the difference between them.
def value_range(numbers):
    maximum = maximum_value(numbers)
    minimum = minimum_value(numbers)
    return (maximum - minimum)

# Calculate the sum of all the numbers in the list.
def sum_of(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Calculate the average of the numbers in the list.
# The function from above to calculate the sum is called in this function.
def average_of(numbers):
    total = sum_of(numbers)
    average = total/len(numbers)
    return average

# Determine the median of the numbers in the list.
def median_of(numbers):
    numbers.sort()
    count = len(numbers)
    midpoint = (count + 1) / 2          # get float of divide by 2
    left_of_midpoint = (count + 1) // 2 # get int of divide by 2 (rounded down division)

    # Midpoint calculations are based on first item being at position 1.
    # Python lists are based on the first value being at index position 0.
    # The caclulated midpoint(s) have to be reduced by 1 to use as list index.
    if (midpoint > left_of_midpoint):
        # average of above and below midpoint
        right_of_midpoint = left_of_midpoint + 1
        return ((numbers[left_of_midpoint - 1] + numbers[right_of_midpoint - 1])/2) 
    else:
        # use midpoint
        return (numbers[int(midpoint - 1)])

# Determine the mode(s) of the numbers in the list.
# The mode is the most frequently occurring number.
# It is possible for more than one number to occur at the highest frequency
# and therefore to have more than one mode.
def modes_of(numbers):
    modes = list()  # to hold the list of modes

    # Count how many of each number value is in list of numbers.
    # Keep the counts in a dictionary where key is the number and the value is the count.
    number_counts = {}
    for number in numbers:
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    # determine maximum count in dictionary of number_counts
    maximum_count = 0
    for number in number_counts:
        count = number_counts[number]
        if (count > maximum_count):
            maximum_count = count

    # find number(s) with the maximum count
    for number in number_counts:
        count = number_counts[number]
        if (count == maximum_count):
            modes.append(number)

    return modes

# The function that determines and presents the statistics.
def get_stats(filename):

    numbers = list()  # to hold the list of numbers

    try:
        number_file = open(filename, "r")
        for number in number_file:
            number = int(number)  # Convert the read string to an int.
            numbers.append(number)
    except Exception as err:
        print ("An error occurred loading", filename)
        print ("The error returned was", err)
        return

    if (len(numbers) < 1):
        print ("There are no numbers in", filename)
        return

    max_value = maximum_value(numbers)
    min_value = minimum_value(numbers)
    val_range = value_range(numbers)
    num_count = len(numbers)
    val_sum = sum_of(numbers)
    val_average = average_of(numbers)
    val_median = median_of(numbers)
    val_modes = modes_of(numbers)

    print ("File name:", filename)
    print ("Sum:", val_sum)
    print ("Count:", num_count)
    print ("Average:", val_average)
    print ("Maximum:", max_value)
    print ("Minimum:", min_value)
    print ("Range:", val_range)
    print ("Median:", val_median)
    print ("Mode:", val_modes)    

# The main function that contains what the program is to do!
def main():
    do_evaluate = True
    while(do_evaluate):
        filename = input('\nWhat is the file you would like to evaluate? ')
        get_stats(filename)
        check_evaluate = input('\nWould you like to evaluate another file? (y/n) ')
        if (check_evaluate != 'y'):
            do_evaluate = False


# Call the main() function to make the program do what it is defined to do.
main()
    
