############################################
############################################
############INVOICE GENERATOR ##############
############################################
############################################

print("Author : Atul kushwaha")      
#importing pyfiglet module for bill header / ASCII ART
import pyfiglet
print(pyfiglet.figlet_format("karthu"))#here store name is karthu

#importing datetime module for time and date
import datetime
date = datetime.datetime.now()

#getting name of customer
name = input("Name of Customer: ")
while type(name) != str or name.isalpha() != True:
    name = input("Please re-enter customer's name without any spaces: ") # Checks to see if the name is valid

#printing menu using prettytable module
print('-'*40,'Menu','-'*40)
from prettytable import PrettyTable
menu = PrettyTable(['S.no','Items','Cost'])
menu.add_rows([
    ['1','Margherita','Rs.75/-'],
    ['2','Double cheese Margherita','Rs.130/-'],
    ['3','Pepper','Rs.175/-'],
    ['4','Cheese & Barbeque Chicken','Rs.130/-'],
    ['5','Veg Extravaganza','Rs.210/-'],
    ['6','Meatza','Rs.245/-'],
    ['7','Veg singles','Rs.170/-'],
    ['8','Chochlate lava cake','Rs.160/-']
])
print(menu)
print('-'*85)
    
#basic info about entering prices based on algoryth of this code
print(" ##ENTER PRICE OF ITEM  AND ENTER ZER0 (0) TO QUIT##")
print(" ##IF YOU WANT AN ITEM WHOSE QUANTITY IS (n) ENTER IT'S PRICE (n) TIMES## ")
Sum = 0
total_items = 0
while(True):
    userinput = input("Enter the price: ")
    while type(userinput) != str or userinput.isnumeric() != True:
        userinput = input("Please re-enter a number: ")
    userinput = int(userinput)

    if(userinput != 0):
        Sum = (Sum + userinput)
        total_items = total_items + 1
    else:
       break

#calculating GST(Goods Service Tax)
GST = float(input("Enter the GST amount (%): "))
gst = (Sum * GST) / 100
amount = Sum + gst

#printing recipt
print("             INVOICE")
print("Name : ",name)
print("Date : ",date)
print("GST (%): ",GST)
print("GST Amount: ",gst)
print("Original price without GST(tax): ",Sum)
print("The Net Amount To Be Paid is: ",amount)
print("The total number of item purchase : ",total_items)

#printing INVOICE/BILL using prettytable module
print('-'*40,'INVOICE','-'*40)
from prettytable import PrettyTable
invoice = PrettyTable(['Name','date','Total items','Total Amount(Rs./-)'])
invoice.add_rows([
[name,date,total_items,amount]
])
print(invoice)
print('-'*85)
print("      Thanks for shopping with us !!!")
print("   Visit us again , have a great day😊 !!!")


