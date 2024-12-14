# imports

import datetime

# constants

REVENUES_FILE = "Revenues.dat"
EMPLOYEES_FILE = "Employees.dat"

# option 7: print driver financial listing

print("\nDriver Financial Listing\n")
DriverNumber = input("Enter Driver/employee number: ")
StartDate = input("Enter Start Date (YYYY-MM-DD): ")
EndDate = input("Enter End Date (YYYY-MM-DD): ")

StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")

try:
    with open(REVENUES_FILE, "r") as RevenuesFile:
        TransactionAmount = 0.0
        TotalHst = 0.0
        TotalAmount = 0.0

        for Line in RevenuesFile:
            try:
                TransactionId, DriverId, Date, Description, Amount, Hst, Total = Line.strip().split(",")
                Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
                if DriverId == DriverNumber and StartDate <= Date <= EndDate:
                    TransactionAmount += float(Amount)
                    TotalHst += float(Hst)
                    TotalAmount += float(Total)
            except ValueError as E:
                print(f"Error processing line: {Line.strip()} - {E}")

    with open(EMPLOYEES_FILE, "r") as EmployeesFile:
        DriverFound = False
        for Line in EmployeesFile:
            DriverId, FirstName, LastName, Address, City, Prov, PostalCode, Phone1, Phone2, Date, Num1, Num2, EmpTotal = Line.strip().split(",")
            Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
            if DriverId == DriverNumber:
                DriverFound = True
                break

        if not DriverFound:
            print(f"Driver {DriverNumber} not found in employees file.")
        else:
            print("\nDriver Financial Report:")
            print(f"     Driver Number:      {DriverNumber}")
            print(f"     Driver Name:        {FirstName} {LastName}")
            EmpTotal = float(EmpTotal)
            print(f"     Current Balance:    ${EmpTotal:,.2f}")
            print()

except FileNotFoundError as E:
    print(f"Error: {E}")
except Exception as E:
    print(f"An unexpected error occurred: {E}")