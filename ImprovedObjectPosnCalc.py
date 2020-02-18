#!/usr/bin/env python
# coding: utf-8

print("This program calculates an object's final position.\n")
do_calculation = True
while(do_calculation):
  while(do_calculation):
# get the initial position
    try:
      x_initial = float(input("Enter the object's initial position: "))
    except ValueError:
      print("The value you enter is invalid. Only numerical values are valid.")
    else:
      break
#get the initial velocity
  while(do_calculation):
    try:
      v_initial = float(input("Enter the object's initial velocity: "))
    except ValueError:
      print("The value you enter is invalid. Only numerical values are valid.")
    else:
      break
#get the elapsed time
  while(do_calculation):
    try:
      time = float(input("Enter the elapsed time: "))
      if(time<0):
        print("Negative elapsed time are not allowed")
        continue
    except ValueError:
      print("The value you enter is invalid. Only positive values are valid.")
    else:
      break
#get the acceleration
  while(do_calculation):
    try:
      acceleration = float(input("Enter the acceleration: "))
    except ValueError:
      print("The value you enter is invalid. Only numerical values are valid.")
    else:
      break

  final = x_initial + v_initial * time + (1/2) * acceleration * time * time

  print("The final position is ", final)

  another_calculation = input("Do you want to perform another calculation?(y/n):")
  if(another_calculation != "y"):
    do_calculation = False