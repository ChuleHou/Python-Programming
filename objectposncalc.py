#!/usr/bin/env python
# coding: utf-8
# Object Position Calculation
print("This program calculates an object's final position.\n")

x_initial = float(input ("The initial position is: "))
v_initial = float(input ("The initial velocity is: "))
acceleration = float(input ("The acceleration is: "))
time = float(input ("The time is: "))

final = x_initial + v_initial*time + (1/2)*acceleration*time*time

print ("The final position is ", final)
