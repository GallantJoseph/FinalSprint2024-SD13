'''
Names:
Dates: Dec 04, 2024 - 
Desc : Compination of all functions to be used in main.py
Note : The amount of J-names are very confusing o_o -Ashton
'''

from time import sleep
from SharedFunctions import BackToMenu
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
       """
       Desc.: Print a company profit listing, including revenues and expenses.
       Author: Joseph Gallant
       Dates: Dec. 5, 2024 - 
       """

        # Read the informations from files



       # Print the headings


       strAddr = "123 Main Street"
       city = "St. John's"
       prov = "NL"
       postalCode = "A2C4E6"
       phone = "7095554227" # HABS
       email = ""



       # Trans.ID, Trans. Date, Desc., SubTotal, HST, Total
       revenuesLst = []

       for listIndex in range(1,6):
            revenuesLst.append(["12345", "2024-10-11", f"Description Trans. {listIndex:2d}", 1234.33, 185.15, 1419.48])
            
       for listItem in revenuesLst:
           print(revenuesLst)


       print(f"HAB Taxi Services")
       print(f"     {strAddr:<30s}")



class MichaelFunctions:
    pass # Delete this line and paste your functions here