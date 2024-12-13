'''
Names:
Dates: Dec 04, 2024 - 
Desc : Compilation of all functions to be used in main.py
Note : The amount of J-names are very confusing o_o -Ashton
'''

# Functions used across all classes
from time import sleep
from SharedFunctions import BackToMenu, FormatValues as fv, ProgressBar, clear
import datetime as dt
import sys


class AshFunctions:
    def placeholder():
        print("This is a placeholder!")
        sleep(1)
        print("It does nothing!")
        sleep(1)
        BackToMenu()
        return

    def end():
        totalIttr = 75
        for i in range(74):
            ProgressBar(i, totalIttr, prefix="Exiting", suffix="Complete", length=50)
            sleep(0.1)
        sleep(2)
        clear()
        for j in range(73, 30, -1):
            ProgressBar(j, totalIttr, prefix="Exiting", suffix="Take it back now y'all", length=50)
            sleep(0.3)
        sleep(1.5)
        clear()
        ProgressBar(74, totalIttr, prefix="Exiting", suffix="One hop this time", length=50)
        sleep(3)
        clear()
        ProgressBar(75, totalIttr, prefix="Exiting", suffix="Complete", length=50)
        sleep(1)
        print("\nThank you for using our program!")
        exit(0)

class JoeyFunctions:
    def CompanyRevenue():
        #I am Joey and I made this!!!1!11!1
        #This program will allow users to enter new 
        #revenue data information and save it to a file.
        #(rental info has to be input here too :P)

        #Constants.
        f = open("Python/Defaults.dat", "r")

        lineList = []
        for line in f:
            lineList.append(line)
        
        NEXT_TRANS_NUM = int(lineList[0].strip())
        NEXT_DRIVE_NUM = int(lineList[1].strip())
        MON_STAND_FEE = float(lineList[2].strip()) 
        DAY_REN_FEE = float(lineList[3].strip())
        WEE_REN_FEE = float(lineList[4].strip())
        HST_RATE = float(lineList[5].strip())

        f.close()

        VAL_NUM = set("1234")

        #Program start.
        while True:
            print(f"\n---Transaction Information---\n")
            while not False:
                try:
                    tranDate = dt.datetime.strptime(input("Enter The Transaction Date (YYYY-MM-DD): "), "%Y-%m-%d")
                except:
                    print("\n   Input Error: Transaction date cannot be an invalid value.\n")
                else:
                    break

            while True:
                tranDesc = input("Enter a Brief Description of The Transaction: ").capitalize()
                if tranDesc == "":
                    print("\n   Input Error: Transaction description cannot be empty.\n")
                else:
                    break

            print("\n---Rental Information---\n")

            #Owned or rented car option input.
            while True:
                carStat = input("Was The Driver's Car Their Own or Rented? (O/R): ").upper()
                if carStat == "":
                    print("\n   Input Error: Driver's car status cannot be empty.\n")
                elif carStat != "O" and carStat != "R":
                    print("\n   Input Error: Driver's car status must be an O or R.\n")
                else:
                    break

            if carStat == "R":
                while True:
                    carNum = input("Enter The Car's Number (1 - 4): ")
                    if carNum == "":
                        print("\n   Input Error: The car's number cannot be empty.\n")
                    elif set(carNum).issubset(VAL_NUM) == False:
                        print("\n   Input Error: The car's number must be a number between 1 and 4 inclusive.\n")
                    else:
                        break
            else:
                #This else should search based on the driver's number entered later to check if they've already paid this fee for the month.
                #Due to us only having to code one option, I'm hoping he will be okay with something like this.    
                #**This is where the Balance Due would be updated.**
                #if driverBalance += MON_STAND_FEE
                renCos = MON_STAND_FEE
                renCosHST = renCos * HST_RATE
                renTotal = renCos + renCosHST

            #Weekly option input.
            print()
            if carStat == "R":
                while True:
                    renType = input("Was The Rental Charged Daily or Weekly? (D/W): ").upper()
                    if renType == "":
                        print("\n   Input Error: Rental type cannot be empty.\n")
                    elif renType != "D" and renType != "W":
                        print("\n   Input Error: Rental type must be a D or W.\n")
                    else:
                        break

                if renType == "W":
                    while True:
                        try:
                            renStartDate = dt.datetime.strptime(input("Enter The Rental Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
                        except:
                            print("\n   Input Error: Rental start date cannot be an invalid value.\n")
                        else:
                            break
                    
                    while True:
                        userChoice = input("Would You Like to Enter The End Date or The Number of Weeks? (E/W): ").upper()
                        if userChoice == "":
                            print("\n   Input Error: Your choice cannot be empty.\n")
                        elif userChoice != "E" and userChoice != "W":
                            print("\n   Input Error: Your choice must be an E or W.\n")
                        else:
                            break
                    
                    if userChoice == "W":
                        while True:
                            try:
                                numWee = int(input("Enter The Number of Weeks Rented: "))
                            except:
                                print("\n   Input Error: Number of weeks cannot be an invalid value.\n")
                            else:
                                renEndDate = renStartDate + dt.timedelta(weeks=numWee)
                                break
                    else:
                        while True:
                            try:
                                renEndDate = dt.datetime.strptime(input("Enter The Rental End Date (YYYY-MM-DD): "), "%Y-%m-%d")
                            except:
                                print("\n   Input Error: Rental End date cannot be an invalid value.\n")
                            else:
                                numWee = round((renEndDate - renStartDate).days / 7)
                                break
                        
                    #Weekly option calculations.
                    renCos = numWee * WEE_REN_FEE

                    renCosHST = renCos * HST_RATE
                    renTotal = renCos + renCosHST
                
                #Daily option inputs.
                else:
                    
                    while True:
                        try:
                            renStartDate = dt.datetime.strptime(input("Enter The Rental Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
                        except:
                            print("\n   Input Error: Rental start date cannot be an invalid value.\n")
                        else:
                            break

                    while True:
                        userChoice = input("Would You Like to Enter The End Date or The Number of Days? (E/D): ").upper()
                        if userChoice == "":
                            print("\n   Input Error: Your choice cannot be empty.\n")
                        elif userChoice != "E" and userChoice != "D":
                            print("\n   Input Error: Your choice must be an E or D.\n")
                        else:
                            break
                    
                    print()
                    if userChoice == "E":
                        while True:
                            try:
                                renEndDate = dt.datetime.strptime(input("Enter The Rental End Date (YYYY-MM-DD): "), "%Y-%m-%d")
                            except:
                                print("\n   Input Error: Rental end date cannot be an invalid value.\n")
                            else:
                                numDay = (renEndDate - renStartDate).days
                                break
                    else:
                        while True:
                            try:
                                numDay = int(input("Enter The Number of Days for The Rental: "))
                            except:
                                print("\n   Input Error: Number of days cannot be an invalid value.\n")
                            else:
                                renEndDate = renStartDate + dt.timedelta(days=numDay)
                                break

                    #Daily option calculations.
                    renCos = numDay * DAY_REN_FEE

                    renCosHST = renCos * HST_RATE
                    renTotal = renCos + renCosHST
            else:
                # If the user chooses Own instead of Rented, renType is not defined and throws an error
                # This is here to fix that -Ashton
                renType = "N/A"
            #Output.
            print(f"\n\n==================================")
            print(f"New Revenue Addition:\n")
            print(f"Transaction Occurred on {fv.FormatDateShort(tranDate):>10s}")
            print(f'Transaction Description:\n\n"{tranDesc}"\n')
            print(f"==================================\n")

            print(f"Rental Information:")
            print(f"----------------------------------")
            print(f"Driver Number:                {NEXT_DRIVE_NUM:>4d}")
            if carStat == "R":
                print(f"Car Number:             {carNum:>10s}")
                print(f"Rental Start Date:      {fv.FormatDateShort(renStartDate):>10s}")
                print(f"Rental End Date:        {fv.FormatDateShort(renEndDate):>10s}\n")
            else:
                print(f"Car Status:                  Owned")
            print(f"Transaction SubTotal:   {fv.FormatDollar2(renCos):>10s}")
            print(f"Transaction HST:        {fv.FormatDollar2(renCosHST):>10s}")
            print(f"                        ----------")
            print(f"Transaction Total:      {fv.FormatDollar2(renTotal):>10s}")
            print(f"==================================")

            con = input("\nPress 'Enter' to Save Transaction Data: ")

            #Saving input and calculated values to revenue record.
            f = open("Python/Revenues.dat", "a")

            f.writelines(f"{str(NEXT_TRANS_NUM)}, ")
            f.writelines(f"{str(NEXT_DRIVE_NUM)}, ")
            f.writelines(f"{str(fv.FormatDateShort(tranDate))}, ")
            f.writelines(f"{tranDesc}, ")
            f.writelines(f"{str(renCos)}, ")
            f.writelines(f"{str(renCosHST)}, ")
            f.writelines(f"{str(renTotal)}\n")

            f.close()

            #Display saving message.
            print()
            TotalIterations = 30
            Message = "Saving Revenue Data..."
        
            for i in range(TotalIterations + 1):
                sleep(0.1)
                ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
            print()
        
            #Update constants and rewrite them to defaults.
            NEXT_TRANS_NUM += 1

            f = open("Python/Defaults.dat", "w")
            
            f.writelines(f"{str(NEXT_TRANS_NUM)}\n")
            f.writelines(f"{str(NEXT_DRIVE_NUM)}\n")
            f.writelines(f"{str(MON_STAND_FEE)}\n")
            f.writelines(f"{str(DAY_REN_FEE)}\n")
            f.writelines(f"{str(WEE_REN_FEE)}\n")
            f.writelines(f"{str(HST_RATE)}")

            f.close()

            con = input("\nWould You Like To Enter Another Transaction? (Y/N): ").upper()
            print()
            if con != "Y":
                BackToMenu()
                return

class JustinFunctions:
    pass # Delete this line and paste your functions here

class JakeFunctions:
    def FinancialListing():
        # option 7: print driver financial listing

        print("\nDRIVER FINANCIAL LISTING\n")
        DriverNumber = input("Enter driver/employee number: ")
        StartDate = input("Enter start date (YYYY-MM-DD): ")
        EndDate = input("Enter end date (YYYY-MM-DD): ")

        StartDate = dt.datetime.strptime(StartDate, "%Y-%m-%d")
        EndDate = dt.datetime.strptime(EndDate, "%Y-%m-%d")
        StartDateF = StartDate.strftime("%Y-%m-%d")
        EndDateF = EndDate.strftime("%Y-%m-%d")
        

        try:
            RevenuesFile = open("Python/Revenues.dat", "r")
            print(f"\nFinancial listing for driver {DriverNumber} ({StartDateF} to {EndDateF}):")
            TransactionAmount = 0.0
            TotalHst = 0.0
            TotalAmount = 0.0

            for Line in RevenuesFile:
                TransactionId, DriverId, Date, Description, Amount, Hst, Total = Line.replace(" ", "").split(",")
                Date = dt.datetime.strptime(Date, "%Y-%m-%d")
                DateF = Date.strftime("%Y-%m-%d")
                if DriverId == DriverNumber and StartDate <= Date <= EndDate:
                    print(f"Transaction #: {TransactionId}, {DateF}, {Amount}, {Hst}, {Total}")
                    TransactionAmount += float(Amount)
                    TotalHst += float(Hst)
                    TotalAmount += float(Total)

            print("\nAmount Summary: \n")
            print(f"subtotal: ${TransactionAmount:.2f}")
            print(f"Total HST: ${TotalHst:.2f}")
            print(f"Total amount: ${TotalAmount:.2f}")
        except:
            print("ERROR - failed to read revenues file.")

        input("Press Enter to Return to the Main Menu...")
        BackToMenu()
        return

class JosephFunctions:
    def CompanyProfitListing():
        '''
        Desc.: Print a company profit listing, including revenues and expenses, and profit margin.
        Author: Joseph Gallant
        Dates: Dec. 5, 2024 - Dec. 11, 2024
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

        # Initialize the variables
        STR_ADDR = "123 Main Street"
        CITY = "St. John's"
        PROV = "NL"
        POSTAL_CODE = "A2C4E6"
        PHONE = "7095554227" # HABS
        EMAIL = "service@habtaxi.com"

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
        print(f"     {STR_ADDR:<30s}")
        print(f"     {CITY}, {PROV:<2s}")
        print(f"     {fv.FormatPostalCode(POSTAL_CODE):<7s}")
        print()
        print(f"     Phone: {fv.FormatPhone(PHONE):<14s}")
        print(f"     Email: {EMAIL:<23s}")
        print()

        # Print the financial report
        print()
        print(f"Financial Report")
        print(f"----------------")
        print()
        print(f"Revenues")
        print()
        print(f"Listing from {fv.FormatDateShort(startDate):<10s} to {fv.FormatDateShort(endDate):<10s}")
        print()
        print(f" Transaction   Transaction            Description            Subtotal        HST          Total")
        print(f"     ID           Date")
        print(f"---------------------------------------------------------------------------------------------------")

        # Open the file to read the revenues data
        f = open("Python/Revenues.dat")

        # Print the revenue records that satisfy the conditions
        for revenue in f:
            # Transaction ID, Driver Number (not used), Transaction Date, Description, Subtotal, HST, Total
            revenueRecord = revenue.split(",")

            transactId = revenueRecord[0]
            transactDate = dt.datetime.strptime(revenueRecord[2].strip(), "%Y-%m-%d")
            transactDesc = revenueRecord[3].strip()
            revSubTot = float(revenueRecord[4].strip())
            revHst = float(revenueRecord[5].strip())
            revTot = float(revenueRecord[6].strip())

            # Check if the date is within the range, and if so, print the transaction and increment the counters and accumulators
            if transactDate >= startDate and transactDate <= endDate:
                revenuesCtr += 1

                revenuesSubTot += revSubTot
                revenuesHst += revHst
                revenuesTot += revTot
                # Print each revenue transaction
                # Transaction ID, Driver Number (not used), Transaction Date, Description, Subtotal, HST, Total

                print(f"    {transactId:<5s}      {fv.FormatDateShort(transactDate):<10s}     {transactDesc:<28s}  {fv.FormatDollar2(revSubTot):>9s}      {fv.FormatDollar2(revHst):>7s}      {fv.FormatDollar2(revTot):>10s}")

        # Close the file
        f.close()

        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                          {fv.FormatDollar2(revenuesSubTot):>11s}   {fv.FormatDollar2(revenuesHst):>10s}   {fv.FormatDollar2(revenuesTot):>13s}")
        print(f"Number of transactions: {revenuesCtr:>3d}")
        print()
        print()
        print(f"Expenses")
        print()
        print(f"Listing from {fv.FormatDateShort(startDate):<10s} to {fv.FormatDateShort(endDate):<10s}")
        print()
        print(f" Invoice  Invoice    Driver   Item        Description        Subtotal        HST          Total")
        print(f" Number    Date      Number  Number                                                       Cost")
        print(f"---------------------------------------------------------------------------------------------------")

        # Open the file to read the expenses data
        f = open("Python/Expenses.dat")

        # Print the expense records that satisfy the conditions
        for expense in f:
            # Invoice Number, Invoice Date, Driver Number, Item Number, Item Description, Item Cost (not used), Item Quantity (not used), Subtotal, HST, Total
            expenseRecord = expense.split(",")

            invNum = expenseRecord[0].strip()
            invDate = dt.datetime.strptime(expenseRecord[1].strip(), "%Y-%m-%d")
            driverNum = expenseRecord[2].strip()
            itemNum = expenseRecord[3].strip()
            itemDesc = expenseRecord[4].strip()
            itemSubTot = float(expenseRecord[7].strip())
            itemHst = float(expenseRecord[8].strip())
            itemTot = float(expenseRecord[9].strip())

            # Check if the date is within the range, and if so, print the transaction and increment the counters and accumulators
            if invDate >= startDate and invDate <= endDate:
                expensesCtr+=1

                expensesSubTot += itemSubTot
                expensesHst += itemHst
                expensesTot += itemTot

                # Print each expense transaction
                # Invoice Number, Invoice Date, Driver Number, Item Number, Item Description, Subtotal, HST, Total

                print(f" {invNum:<6s}  {fv.FormatDateShort(invDate):<10s}   {driverNum:<4s}   {itemNum:<7s}  {itemDesc:<20s}  {fv.FormatDollar2(itemSubTot):>10s}    {fv.FormatDollar2(itemHst):>9s}     {fv.FormatDollar2(itemTot):>10s} ")

        # Close the file
        f.close()
        
        print(f"---------------------------------------------------------------------------------------------------")
        print(f"                                                         {fv.FormatDollar2(expensesSubTot):>13s}  {fv.FormatDollar2(expensesHst):>11s}  {fv.FormatDollar2(expensesTot):>13s}")
        print()
        print(f"Number of transactions: {expensesCtr:>3d}")
        print()
        print()
        print(f"Profit Report")
        print(f"-------------")
        print()
        print(f"Revenues")
        print(f"     Subtotal:        {fv.FormatDollar2(revenuesSubTot):>11s}")
        print(f"     HST:              {fv.FormatDollar2(revenuesHst):>10s}")
        print(f"                    -------------")
        print(f"     Total:         {fv.FormatDollar2(revenuesTot):>13s}")
        print()
        print()
        print(f"Expenses")
        print(f"     Subtotal:        {fv.FormatDollar2(expensesSubTot):>11s}")
        print(f"     HST:              {fv.FormatDollar2(expensesHst):>10s}")
        print(f"                    -------------")
        print(f"     Total:         {fv.FormatDollar2(expensesTot):>13s}")
        print()
        print()
        print(f"Revenues Total:     {fv.FormatDollar2(revenuesTot):>13s}")
        print(f"Expenses Total:    -{fv.FormatDollar2(expensesTot):>13s}")
        print(f"                    -------------")

        # Calculate the profit margin
        profitMargin = revenuesTot - expensesTot

        print(f"Profit Margin:      {fv.FormatDollar2(profitMargin):>13s}")
        print()
        print()
        input("Press Enter to Return to the Main Menu...")
        BackToMenu()
        return


class MichaelFunctions:
    pass # Delete this line and paste your functions here