import datetime
from os import system, name
from time import sleep

class FormatValues:
    def FormatDollar2(DollarValue: float):
        '''Function will accept a value and format it to $#,###.##'''

        return "${:,.2f}".format(DollarValue)


    def FormatDollar0(DollarValue: float):
        '''Function will accept a value and format it to $#,###'''

        return "${:,.0f}".format(DollarValue)


    def FormatComma2(Value: float):
        '''Function will accept a value and format it to #,###.##'''

        return "{:,.2f}".format(Value)


    def FormatComma0(Value: float):
        '''Function will accept a value and format it to #,###'''

        return "{:,.0f}".format(Value)


    def FormatNumber0(Value: float):
        '''Function will accept a value and format it to ########'''

        return "{:.0f}".format(Value)


    def FormatNumber1(Value: float):
        '''Function will accept a value and format it to ####.#'''

        return "{:.1f}".format(Value)


    def FormatNumber2(Value: float):
        '''Function will accept a value and format it to ####.##'''

        return "{:.2f}".format(Value)


    def FormatDateShort(DateValue:datetime.datetime):
        '''
        Function will accept a value and format it to yyyy-mm-dd.
        Ex: 2024-11-21
        '''

        return DateValue.strftime("%Y-%m-%d")


    def FormatDateMedium(DateValue:datetime.datetime):
        '''
        Function will accept a value and format it to dd-Mon-yy.
        Ex: 11-Oct-24
        '''

        return DateValue.strftime("%d-%b-%y")


    def FormatDateLong(DateValue:datetime.datetime):
        '''
        Function will accept a value and format it to Day, Month dd, yyyy.
        Ex: Thursday, October 21, 2024
        '''

        return DateValue.strftime("%A, %B %d, %Y")

    def FormatSIN(sin: str):
        '''Function will accept a value as 9 digits SIN and format it with spacing.'''
            
        return sin[0:3] + " " + sin[3:6] + " " + sin[6:9]

    def FormatPhone(phone: str):
        '''Function will accept a value as a 10 digit Phone Number and format it'''

        return f"({phone[0:3]}) {phone[3:6]}-{phone[6:10]}"
    
    def FormatPostalCode(postalCode):
        '''Function that formats a postal code in the X#X #X# format.'''

        formPostalCode = postalCode[0:3] + " " + postalCode[3:6]

        return formPostalCode

def clear():
    system("cls" if name == "nt" else "clear")

def BackToMenu():
    clear()
    print("Returning to menu...")
    sleep(1)
    return