"""
----------------------------------------------------------
Name: problem2.py
Purpose: Allows user to enter 3 side lengths and determines if it forms a triangle or not.

Author: Yeh.A

Created: 23/02/21
----------------------------------------------------------
"""
print("***** Welcome to the Triangle Checker *****")
print(" ")

#get side lengths
side_1 = int(input("Enter the length of the first side: "))
side_2 = int(input("Enter the length of the second side: "))
side_3 = int(input("Enter the length of the third side: "))

#computes sum of any 2 side lengths to see if it is greater than the 3rd side, outputs whether it forms a triangle or not
if side_3 < side_1 + side_2 and side_2 < side_1 + side_3 and side_1 < side_2 + side_3:
  print("The figure is a triangle.")
else:
  print("The figure is NOT a triangle.")