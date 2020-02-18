import math

wall_unit = 350
coast_perhour = 62.25
hour = 6
labor_unit = 1

print("This program is a Paint Job Estimator.\n")
do_calculation = True
while(do_calculation):
    while(do_calculation):
#get the square feet of wall space
        try:
            wall_space = float(input("Enter the square feet of wall space: "))
            if(wall_space < 0):
                print("The square feet of wall space must be positive values.")
                continue
        except ValueError:
            print("The value you enter is invalid. Only numerical values are valid.")
        else:
            break
#get the price of the paint per gallon
    while(do_calculation):
        try:
            price = float(input("Enter the price of the paint per gallon: "))
            if(price < 0):
                print("The price of the paint gallon must be positive values.")
                continue
        except ValueError:
            print("The value you enter is invalid. Only numerical values are valid.")
        else:
            break
    number_of_gallons = (wall_space/wall_unit) * labor_unit
    print("The number of gallons of paint required: ",  math.ceil(number_of_gallons))

    hours_of_labor = (wall_space/wall_unit) * hour
    print("The hours of labor required: ", '%.1f' % hours_of_labor)

    cost_of_paint = number_of_gallons * price
    print("The cost of the paint based on the round up whole gallons: ", round(cost_of_paint))

    labor_charges  = coast_perhour * hours_of_labor
    print("The labor charges: ", "$" + '%.2f' % labor_charges)

    total_coast = cost_of_paint + labor_charges
    print("The total cost of the paint job: ", "$" + '%.2f' % total_coast)

    another_calculation = input("Do you want to perform another calculation?(y/n)")
    if(another_calculation != "y"):
        do_calculation = False