# Created by:   Patrick Archer
# Date:         20 December 2018
# Copyright to the above author. All rights reserved.

"""
Directions - COMPLETE:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
(Hint) how does an even / odd number react differently when divided by 2?

Extras - COMPLETE:
(1 - DONE) If the number is a multiple of 4, print out a different message.
(2 - DONE) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

# ################################################# start_funcs

def runCalcs(num, mod1, mod2):

    print("\n#####################")
    print("\nNow running calculations of the values you entered.\nThe results are as follows:")
    print(str(num) + " mod(" + str(mod1) + ") = " + str(int(num) % int(mod1)))
    print(str(num) + " mod(" + str(mod2) + ") = " + str(int(num) % int(mod2)))
    print("\n#####################\n")

    # if IS multiple of 2 and IS multiple of 4, do...
    if (num %mod1 == 0 and num %mod2 == 0):
        print("Thus, the number " + str(num) + " IS a multiple of 2 AND ALSO a multiple of 4.\n")
    # if IS multiple of 2 and NOT multiple of 4, do...
    elif (num %mod1 == 0 and num %mod2 != 0):
        print("Thus, the number " + str(num) + " IS a multiple of 2 BUT NOT a multiple of 4.\n")
    # if NOT multiple of 2 and IS multiple of 4, do...
    elif (num %mod1 != 0 and num %mod2 == 0):
        print("Thus, the number " + str(num) + " IS NOT a multiple of 2 BUT IS a multiple of 4.\n")
    # if NOT multiple of 2 and NOT multiple of 4, do...
    elif (num %mod1 != 0 and num %mod2 != 0):
        print("Thus, the number " + str(num) + " IS NOT a multiple of 2 AND IS NOT a multiple of 4.\n")
    else:
        print("ERROR: Mark @ runCalcs() else statement.\n")

# ################################################# end_funcs/start_main

# prompt user for desired number, 1st modulus to use, and 2nd modulus to use
userNum = input("\nPlease enter any whole number.\n")
userMod1 = input("Please enter the first whole number modulus you wish to use in calculations.\n")
userMod2 = input("Please enter the second whole number modulus you wish to use in calculations.\n")

try:
    userNum = int(userNum)  # convert from str to int
    userMod1 = int(userMod1)  # convert from str to int
    userMod2 = int(userMod2)  # convert from str to int
    runCalcs(userNum, userMod1, userMod2)   # call runCalcs func with user-entered values
except (ValueError):
    print("ERROR: Invalid number entered. Ending program to prevent further catastrophe.\n")





