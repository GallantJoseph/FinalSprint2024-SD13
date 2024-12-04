"""
Description:
Authors:
Dates:
"""
from SharedFunctions import clear, placeholder
from time import sleep

while True:
    clear()
    print("        HAB Taxi Services")
    print("     Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Quit Program.")
    print()
    match input("      Enter choice (1-8): "):
        case "1":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "2":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "3":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "4":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "5":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "6":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "7":
            clear()
            print("Opening...")
            sleep(1.5)
            clear()
            placeholder()
        case "8":
            exit(0) #temp until i make something funny
        case _:
            clear()
            print("Invalid Option...")
            sleep(2)

