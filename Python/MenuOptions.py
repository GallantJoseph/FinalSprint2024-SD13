'''
Names:
Dates: Dec 04, 2024 - 
Desc : Compination of all functions to be used in main.py
Note : The amount of J-names are very confusing o_o -Ashton
'''

from time import sleep
from SharedFunctions import BackToMenu
import SharedFunctions as sf
import datetime as dt


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

        # Initialize counters and accumulators
        revenuesCtr = 0
        revenuesSubTot = 0.0
        revenuesHst = 0.0
        revenuesTot = 0.0

        expensesCtr = 0
        expensesSubTot = 0.0
        expensesHst = 0.0
        expensesTot = 0.0

        # Initialize the variables (TODO: From defaults file?)
        strAddr = "123 Main Street"
        city = "St. John's"
        prov = "NL"
        postalCode = "A2C4E6"
        phone = "7095554227" # HABS
        email = "service@habtaxi.com"

        # Print the program headings
        print()
        print("                             HAB Taxi Services - Company Profit Listing")
        print(f"---------------------------------------------------------------------------------------------------")
        print()

        # Gather the date range values for the listing

        # Validate the startDate
        while True:
            startDate = input("Enter the start date (YYYY-MM-DD): ")

            try:
                startDate = dt.datetime.strptime(startDate, "%Y-%m-%d")
            except:
                print()
                print("Data Entry Error - Invalid Date Format. ")
                print()
            else:
                break

        # Validate the endDate
        while True:
            endDate = input("Enter the end date (YYYY-MM-DD): ")

            try:
                endDate = dt.datetime.strptime(endDate, "%Y-%m-%d")
            except:
                print()
                print("Data Entry Error - Invalid Date Format. ")
                print()
            else:
                if endDate < startDate:
                    print()
                    print("Data Entry Error - End Date Must Be After Start Date")
                    print()
                else:
                    break

        # Print the report headings
        print()
        print(f"HAB Taxi Services")
        print(f"     {strAddr:<30s}")
        print(f"     {city}, {prov:<2s}")
        print(f"     {sf.FormatValues.FormatPostalCode(postalCode):<7s}")
        print()
        print(f"     Phone: {sf.FormatValues.FormatPhone(phone):<14s}")
        print(f"     Email: {email:<23s}")
        print()

        # Print the financial report
        print()
        print(f"Financial Report")
        print(f"----------------")
        print()
        print(f"Revenues")
        print(f"Listing from {sf.FormatValues.FormatDateShort(startDate):<10s} to {sf.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Transaction    Transaction           Description            Subtotal         HST           Total")
        print(f"    ID            Date")
        print(f"---------------------------------------------------------------------------------------------------")

        # Open the file to read the revenues data
        f = open("Revenues.dat")

        # Print the revenue records that satisfy the conditions
        for revenue in f:
            # Trans.ID, Trans. Date, Desc., SubTotal, HST, Total
            revenueRecord = revenue.split(",")

            transactId = revenueRecord[0]
            transactDate = dt.datetime.strptime(revenueRecord[1].strip(), "%Y-%m-%d")
            transactDesc = revenueRecord[2].strip()
            subTot = float(revenueRecord[3].strip())
            hst = float(revenueRecord[4].strip())
            tot = float(revenueRecord[5].strip())

            # Check if the date is within the range, and if so, print the transaction and increment the counters and accumulators
            if transactDate >= startDate and transactDate <= endDate:
                revenuesCtr += 1

                revenuesSubTot += subTot
                revenuesHst += hst
                revenuesTot += tot
                # Print each revenue transaction
                # Transaction ID, Transaction Date, Description, Subtotal, HST, Total

                print(f"  {transactId:<5s}        {sf.FormatValues.FormatDateShort(transactDate):<10s}   {transactDesc:<30s}  {sf.FormatValues.FormatDollar2(subTot):>9s}      {sf.FormatValues.FormatDollar2(hst):>7s}      {sf.FormatValues.FormatDollar2(tot):>10s}")

        # Close the file
        f.close()

        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                          {sf.FormatValues.FormatDollar2(revenuesSubTot):>11s}   {sf.FormatValues.FormatDollar2(revenuesHst):>10s}   {sf.FormatValues.FormatDollar2(revenuesTot):>13s}")
        print(f"Number of transactions: {revenuesCtr:>3d}")
        print()
        print()
        print(f"Expenses")
        print(f"Listing from {sf.FormatValues.FormatDateShort(startDate):<10s} to {sf.FormatValues.FormatDateShort(endDate):<10s}")
        print()
        print(f"Expense   Invoice   Item              Item                Item        Qty     HST         Total")
        print(f"  ID      Number    Number         Description            Cost                            Cost")
        print(f"---------------------------------------------------------------------------------------------------")

        # Open the file to read the expenses data
        f = open("Expenses.dat")

        # Print the revenue records that satisfy the conditions
        for expense in f:
            # Expense ID, Invoice Number, Item Number, Item Description, Item Cost, Quantity, HST, Total Cost
            expenseRecord = expense.split(",")

            expenseId = expenseRecord[0].strip()
            invNum = expenseRecord[1].strip()
            itemNum = expenseRecord[2].strip()
            itemDesc = expenseRecord[3].strip()
            itemCost = float(expenseRecord[4].strip())
            itemQty = int(expenseRecord[5].strip())
            itemSubTot = itemQty * itemCost # TODO, add this value to the file instead
            itemHst = float(expenseRecord[6].strip())
            itemTot = float(expenseRecord[7].strip())

            # TODO: Add a field/variable in the file, find a way to display it somewhere
            expenseDate = dt.datetime.strptime("2024-10-10", "%Y-%m-%d")

            # Check if the date is within the range, and if so, print the transaction and increment the counters and accumulators
            if expenseDate >= startDate and expenseDate <= endDate:
                expensesCtr+=1

                expensesSubTot += itemSubTot
                expensesHst += itemHst
                expensesTot += itemTot

                # Print each expense transaction
                # Expense ID, Invoice Number, Item Number, Item Description, Item Cost, Quantity, HST, Total Cost

                print(f" {expenseId:<5s}    {invNum:<6s}    {itemNum:<7s}   {itemDesc:<22s}   {sf.FormatValues.FormatDollar2(itemCost):>10s}     {itemQty:>3d}  {sf.FormatValues.FormatDollar2(itemHst):>9s}    {sf.FormatValues.FormatDollar2(itemTot):>10s} ")

        # Close the file
        f.close()
        
        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                    {sf.FormatValues.FormatDollar2(expensesSubTot):>13s}     {sf.FormatValues.FormatDollar2(expensesHst):>11s}    {sf.FormatValues.FormatDollar2(expensesTot):>13s}")
        print(f"                                                      (Subtotal)         (HST)          (Total)")
        print(f"Number of transactions: {expensesCtr:>3d}")
        print()
        print()
        print(f"Profit Report")
        print(f"-------------")
        print()
        print(f"Revenues")
        print(f"     Subtotal:        {sf.FormatValues.FormatDollar2(revenuesSubTot):>11s}")
        print(f"     HST:              {sf.FormatValues.FormatDollar2(revenuesHst):>10s}")
        print(f"                    -------------")
        print(f"     Total:         {sf.FormatValues.FormatDollar2(revenuesTot):>13s}")
        print()
        print()
        print(f"Expenses")
        print(f"     Subtotal:        {sf.FormatValues.FormatDollar2(expensesSubTot):>11s}")
        print(f"     HST:              {sf.FormatValues.FormatDollar2(expensesHst):>10s}")
        print(f"                    -------------")
        print(f"     Total:         {sf.FormatValues.FormatDollar2(expensesTot):>13s}")
        print()
        print()
        print(f"Revenues Total:     {sf.FormatValues.FormatDollar2(revenuesTot):>13s}")
        print(f"Expenses Total:    -{sf.FormatValues.FormatDollar2(expensesTot):>13s}")
        print(f"                    -------------")

        # Calculate the profit margin
        profitMargin = revenuesTot - expensesTot

        print(f"Profit Margin:      {sf.FormatValues.FormatDollar2(profitMargin):>13s}")
        print()
        print()
        input("Press Enter to Return to the Main Menu...")


class MichaelFunctions:
    pass # Delete this line and paste your functions here