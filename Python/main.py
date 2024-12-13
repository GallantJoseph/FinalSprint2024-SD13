"""
Description: The Main program. Run this one when testing. This contains the main menu and calls the options from the MenuOptions file
Authors: 
Dates: Dec 1st, 2024 - 
"""
from SharedFunctions import clear
from MenuOptions import *
from time import sleep

while True:
    # Reads the values of the Defaults file every time the loop repeats
    f = open("Python/DataFiles/Defaults.dat", "r")

    defaults = []
    for line in f:
        defaults.append(line)

    f.close()

    # The Main Menu
    clear()
    print("        HAB Taxi Services")
    print("     Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues. [Implemented]")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing. [Implemented]")
    print("7. Print Driver Financial Listing. [Implemented]")
    print("8. Quit Program.")
    print()
    match input("      Enter choice (1-8): "):
        case "1":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            AshFunctions.placeholder()
        case "2":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            JoeyFunctions.CompanyRevenue(defaults)
        case "3":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            AshFunctions.placeholder()
        case "4":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            AshFunctions.placeholder()
        case "5":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            AshFunctions.placeholder()
        case "6":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            JosephFunctions.CompanyProfitListing()
        case "7":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            JakeFunctions.FinancialListing()
        case "8":
            clear()
            AshFunctions.end()
        case _:
            clear()
            print("Invalid Option...")
            sleep(2)

