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
        revenuesSubTot = 0.0
        revenuesHst = 0.0
        revenuesTot = 0.0

        expensesCtr = 0
        expensesSubTot = 0.0
        expensesHst = 0.0
        expensesTot = 0.0

        # Print the headings


        strAddr = "123 Main Street"
        city = "St. John's"
        prov = "NL"
        postalCode = "A2C4E6"
        phone = "7095554227" # HABS
        email = "service@habstaxi.com"

        # TODO Remove testing variables and use input instead
        startDate = DT.datetime.strptime("2024-10-10", "%Y-%m-%d")
        endDate = DT.datetime.strptime("2024-11-10", "%Y-%m-%d")

        # Trans.ID, Trans. Date, Desc., SubTotal, HST, Total
        revenuesLst = []

        # Build a temporary list for testing purposes
        for listIndex in range(1,6):
            revenuesLst.append(["12345", "2024-10-11", f"Description Trans. {listIndex:2d}", 1234.33, 185.15, 1419.48])

        print()
        print(f"HAB Taxi Services")
        print(f"     {strAddr:<30s}")
        print(f"     {city}, {prov:<2s}")
        print(f"     {SF.FormatValues.FormatPostalCode(postalCode):<7s}")
        print()
        print(f"     Phone: {SF.FormatValues.FormatPhone(phone):<14s}")
        print(f"     Email: {email:<23s}")
        print()
        print(f"Financial Report")
        print(f"----------------")
        print()
        print(f"Revenues")
        print(f"Listing from {SF.FormatValues.FormatDateShort(startDate):<10s} to {SF.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Transaction    Transaction           Description            Subtotal         HST           Total")
        print(f"    ID            Date")
        print(f"---------------------------------------------------------------------------------------------------")

        # Print each revenue transaction
        # Transaction ID, Transaction Date, Description, Subtotal, HST, Total
        for listItem in revenuesLst:
            revenuesCtr += 1

            transactId = listItem[0]
            transactDate = DT.datetime.strptime(listItem[1], "%Y-%m-%d")
            transactDesc = listItem[2]
            subTot = float(listItem[3])
            hst = float(listItem[4])
            tot = float(listItem[5])

            print(f"  {transactId:<5s}        {SF.FormatValues.FormatDateShort(transactDate):<10s}   {transactDesc:<30s}  {SF.FormatValues.FormatDollar2(subTot):>9s}      {SF.FormatValues.FormatDollar2(hst):>7s}      {SF.FormatValues.FormatDollar2(tot):>10s}")

            revenuesSubTot += subTot
            revenuesHst += hst
            revenuesTot += tot

        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                          {SF.FormatValues.FormatDollar2(revenuesSubTot):>11s}   {SF.FormatValues.FormatDollar2(revenuesHst):>10s}   {SF.FormatValues.FormatDollar2(revenuesTot):>13s}")
        print(f"Number of transactions: {revenuesCtr:>3d}")
        print()
        print()

        # Trans.ID, Trans. Date, Desc., SubTotal, HST, Total
        expensesLst = []
       
        # Build a temporary list for testing purposes
        for listIndex in range(1,6):
            expensesLst.append(["12345", "234567", "3456789", f"Description Trans. {listIndex:2d}", 1234.33, 3, 555.45, 4258.44])

        print(f"Expenses")
        print(f"Listing from {SF.FormatValues.FormatDateShort(startDate):<10s} to {SF.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Expense   Invoice   Item              Item                Item        Qty     HST         Total")
        print(f"  ID      Number    Number         Description            Cost                            Cost")
        print(f"---------------------------------------------------------------------------------------------------")

        # Print each expense transaction
        # Expense ID, Invoice Number, Item Number, Item Description, Item Cost, Quantity, HST, Total Cost

        for listItem in expensesLst:
            expensesCtr += 1

            expenseId = listItem[0]
            invNum = listItem[1]
            itemNum = listItem[2]
            itemDesc = listItem[3]
            itemCost = float(listItem[4])
            itemQty = int(listItem[5])
            itemSubTot = itemQty * itemCost
            itemHst = float(listItem[6])
            itemTot = float(listItem[7])

            print(f" {expenseId:<5s}    {invNum:<6s}    {itemNum:<7s}   {itemDesc:<22s}   {SF.FormatValues.FormatDollar2(itemCost):>10s}     {itemQty:>3d}  {SF.FormatValues.FormatDollar2(itemHst):>9s}    {SF.FormatValues.FormatDollar2(itemTot):>10s} ")
            expensesSubTot += itemSubTot
            expensesHst += itemHst
            expensesTot += itemTot

        
        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                    {SF.FormatValues.FormatDollar2(expensesSubTot):>13s}     {SF.FormatValues.FormatDollar2(expensesHst):>11s}    {SF.FormatValues.FormatDollar2(expensesTot):>13s}")
        print(f"                                                      (Subtotal)         (HST)          (Total)")
        print()
        print(f"Number of transactions: {expensesCtr:>3d}")
        print()
        print()
        print(f"Profit Report")
        print(f"-------------")
        print()
        print(f"Revenues")
        print(f"     Subtotal:        {SF.FormatValues.FormatDollar2(revenuesSubTot):>11s}")
        print(f"     HST:              {SF.FormatValues.FormatDollar2(revenuesHst):>10s}")
        print(f"                    -------------")
        print(f"     Total:         {SF.FormatValues.FormatDollar2(revenuesTot):>13s}")




        input("Pause...")


class MichaelFunctions:
    pass # Delete this line and paste your functions here