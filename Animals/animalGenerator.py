from animal import Animal

print("Welcome to the animal generator!")
print("This program creates Animal objects. \n")
object_list = []

while(1):
    animal_type = input("What type of animal would you like to create?")
    animal_name = input("What is the animal's name?")
    object_list.append(Animal(animal_type,animal_name))

    if(input("Would you like to add more animals(y/n)?")=='y'):
        continue
    else:
        break
print("Animal List: \n")
for animals in object_list:
    print(animals.get_name() + " the " + animals.get_animal_type() + " is " + animals.check_mood())