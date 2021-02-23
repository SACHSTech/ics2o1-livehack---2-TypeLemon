"""
----------------------------------------------------------
Name: problem1.py
Purpose: Program for NASA's Perserverance Rover that detects/classifies life forms using number of antenna and eyes.

Author: Yeh.A

Created: 23/02/2021
----------------------------------------------------------
"""
print("***** NASA's Martian Identifier *****")
print(" ")

#allows user to enter number of antenna and eyes
num_ant = int(input("How many antennas?: "))
num_eyes = int(input("How many eyes?: "))

#outputs name of aliens that match criteria
if num_ant >= 3 and num_eyes <= 4:
  print("Life form detected: AudreyMartian")
  
if num_ant <= 6 and num_eyes >= 2:
  print("Life form detected: MaxMartian")
  
if num_ant <= 2 and num_eyes <= 3:
  print("Life form detected: BrooklynMartian")
  
if num_ant == 0 and num_eyes == 2:
  print("Life form detected: MattDamonMartian")

else: 
  print("No life form detected.")