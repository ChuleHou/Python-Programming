import Animals

# Create a list for Animal objects
object_list = []

# Print a welcome message
print("Welcome to the animal generator!")
print("This program creates Animal objects")

while True:
    # Ask the user for the animal's type
    print("\nWould you like to create a mammal or bird? \n1. Mammal \n2. Bird")
    type = input("Which would you like to create? ")
    if type == "1":
        animal_type = input("\nWhat type of mammal would you like to create? ")
        animal_name = input("What is the mammal’s name? ")
        hair_color = input("What color is the mammal’s hair? ")
        object_list.append(Animals.Mammal(animal_type,animal_name,hair_color))

    else:
        animal_type = input("\nWhat type of bird would you like to create?")
        animal_name = input("What is the bird's name?")
        can_fly = input("Can the bird fly?")
        object_list.append(Animals.Bird(animal_type,animal_name,can_fly))

    choice = input("\nWould you like to add more animals (y/n)? ")
    if choice != "y":
        break

# Print a header
print("\nAnimal List:")

# Loop through the list
for animals in object_list:
    print(animals.get_name() + " the " + animals.get_animal_type() + " is " + animals.check_mood())