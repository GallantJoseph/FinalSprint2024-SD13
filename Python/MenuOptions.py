'''
Names:
Dates: Dec 04, 2024 - 
Desc : Compination of all functions to be used in main.py
Note : The amount of J-names are very confusing o_o -Ashton
'''

from time import sleep
from SharedFunctions import BackToMenu
import SharedFunctions as SF
import datetime as DT


class AshFunctions:
    def placeholder():
        print("This is a placeholder!")
        sleep(1)
        print("It does nothing!")
        sleep(1)
        BackToMenu()
        return

    def end():
        exit(0) # temp until i make something funny

class JoeyFunctions:
    pass # Delete this line and paste your functions here

class JustinFunctions:
    pass # Delete this line and paste your functions here

class JakeFunctions:
    pass # Delete this line and paste your functions here

class JosephFunctions:
    def CompanyProfitListing():
        '''
        Desc.: Print a company profit listing, including revenues and expenses, and profit margin.
        Author: Joseph Gallant
        Dates: Dec. 5, 2024 - 
        '''

        # Read the informations from files

        # Initialize counters and accumulators
        revenuesCtr = 0
        revenuesSubtot = 0.0
        revenuesHst = 0.0
        revenuesTot = 0.0

        expensesCtr = 0
        expensesSubtot = 0.0
        expensesHst = 0.0
        expensesTot = 0.0

        # Print the headings


        strAddr = "123 Main Street"
        city = "St. John's"
        prov = "NL"
        postalCode = "A2C4E6"
        phone = "7095554227" # HABS
        email = ""

        startDate = DT.datetime.strptime("2024-10-10", "%Y-%m-%d")
        endDate = DT.datetime.strptime("2024-11-10", "%Y-%m-%d")

        print(startDate)
        print(endDate)

        # Trans.ID, Trans. Date, Desc., SubTotal, HST, Total
        revenuesLst = []

        # Build a temporary list for testing purposes
        for listIndex in range(1,6):
            revenuesLst.append(["12345", "2024-10-11", f"Description Trans. {listIndex:2d}", 1234.33, 185.15, 1419.48])

        print()
        print(f"HAB Taxi Services")
        print(f"     {strAddr:<30s}")
        print(f"     {city}, {prov:<2s}")
        print(f"     {strAddr:<30s}")
        print(f"     {SF.FormatValues.FormatPostalCode(postalCode):<7s}")
        print()
        print(f"     Phone: {SF.FormatValues.FormatPhone(phone):<14s}")
        print()
        print(f"Financial Report")
        print(f"----------------")
        print()
        print(f"REVENUES")
        print(f"Listing from {SF.FormatValues.FormatDateShort(startDate):<10s} to {SF.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Transaction    Transaction           Description            Subtotal         HST           Total")
        print(f"    ID            Date")
        print(f"---------------------------------------------------------------------------------------------------")

        # Print each revenue transaction
        # Transaction ID, Transaction Date, Description, Subtotal, HST, Total
        for listItem in revenuesLst:
            revenuesCtr += 1

            transactDate = DT.datetime.strptime(listItem[1], "%Y-%m-%d")

            print(f"  {listItem[0]:<5s}        {SF.FormatValues.FormatDateShort(transactDate):<10s}   {listItem[2]:<30s}  {SF.FormatValues.FormatDollar2(listItem[3]):>9s}      {SF.FormatValues.FormatDollar2(listItem[4]):>7s}      {SF.FormatValues.FormatDollar2(listItem[5]):>10s}")
            pass

        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                          {SF.FormatValues.FormatDollar2(revenuesSubtot):>11s}   {SF.FormatValues.FormatDollar2(revenuesHst):>10s}   {SF.FormatValues.FormatDollar2(revenuesTot):>13s}")
        print(f"Number of transactions: {revenuesCtr:>3d}")


        print(f"EXPENSES")
        print(f"Listing from {SF.FormatValues.FormatDateShort(startDate):<10s} to {SF.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Expense   Invoice   Item              Item                Item        Qty    HST          Total")
        print(f"  ID      Number    Number         Description            Cost                            Cost")
        print(f"---------------------------------------------------------------------------------------------------")



class MichaelFunctions:
    pass # Delete this line and paste your functions here