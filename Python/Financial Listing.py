# imports

import datetime 

# constants

REVENUES_FILE = "Revenues.dat"

# option 7: print driver financial listing

print("\nDRIVER FINANCIAL LISTING\n")
DriverNumber = input("Enter driver/employee number: ")
StartDate = input("Enter start date (YYYY=MM-DD): ")
EndDate = input("Enter end date (YYYY-MM-DD): ")

StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
StartDateF = StartDate.strftime("%Y-%m-%d")
EndDateF = EndDate.strftime("%Y-%m-%d")
 

try: 
    RevenuesFile = open(REVENUES_FILE, "r")
    print(f"\nFinancial listing for driver {DriverNumber} ({StartDateF} to {EndDateF}):")
    TransactionAmount = 0.0
    TotalHst = 0.0
    TotalAmount = 0.0

    for Line in RevenuesFile:
        TransactionId, Date, Description, DriverId, Amount, Hst, Total = Line.strip()
        total = Line.strip().split(",")
        Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
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