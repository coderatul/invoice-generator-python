import sys
import pyfiglet
from datetime import date, datetime
from prettytable import PrettyTable

#here store name is LOS POLLOS HERMANOS 
print(pyfiglet.figlet_format("LOS POLLOS HERMANOS"))

#you can add row-wise-details by editing Menu.txt file where elements are seperated by a comma "," 

#printing Menu
menu = PrettyTable(['S.no','Items','Cost'])
with open("Menu.txt","r") as f:
    rows =[]
    for i in (f.read().split("\n")):
        rows.append(i.split(","))
try:
    menu.add_rows(rows)
except:
    print("  ~ something is wrong with Menu.txt file ~ ")
    print("""
    - make sure you don't leave any empty line in the start or in between
    - make sure all 3 elements of row are present and are seperated by a comma (,)
    - make sure that only 3 elemets are present for a row as there are only 3 columns
    - a ideal row in Menu.txt would look like -> 1, pizza, 169
    """)
    sys.exit()
print('-'*19,'Menu','-'*19)
print(menu)
print('-'*44,"\n")

#getting name of customer
name = input("Name of Customer: ").title()

#basic info about entering prices based on flow of control of this project
print("""
 *_* enter slno. to add items or enter "q" to quit adding times *_*
 *_* if you added something by mistake then enter quantity as 0 *_*
""")
#creating a dictionary to get product_name(value) and price(value) via Slno.(key)
data = {}
for j in rows:
    data[j[0]] = list(j[1:])

slno = 1
total_quantity = 0
amount = 0
recipt = []
# the above list_nested recipt would contain row-wise info for invoice
while(True):
    item = input("enter the slno. of item you want to order: ").strip()
    try:
        data.get(item)[0]
    except:
        if item == "q":
            pass
        else:
            print(f"~ slno.\"{item}\" not found, please check and enter again ~\n")
    else:
        try:
            quantity = input("enter quantity desired(default = 1, to skip press enter): ")

            if quantity == '':
                quantity = 1

            else: 
                quantity = int(quantity)

            print("\n")
        except:
            raise TypeError("please enter an integer as quantity")
        if quantity == 0:
            slno -= 1
        else:
            recipt.append([slno,data.get(item)[0],quantity,data.get(item)[1],int(data.get(item)[1]) * quantity])
            amount += int(data.get(item)[1]) * quantity
            total_quantity += quantity
        slno += 1
    finally:
        pass
    if item == "q":
        break

#calculating GST(Goods Service Tax) apllying GST as 5%
GST = 5 
gst = (amount * GST) / 100
final_amount = amount + gst

date = date.today().strftime("%d/%m/%y")
time = datetime.now().strftime("%H:%M:%S")


#printing recipt
print(f"             INVOICE")
print(f"Name : {name}")
print(f"Date : {date}    Time: {time}")
print(f"GST (%): {GST}")
print(f"The Net Amount To Be Paid is: {final_amount}")
print(f"The total number of item purchase : {total_quantity}")

#printing INVOICE/BILL using prettytable module
print('-'*37,'INVOICE','-'*37)
from prettytable import PrettyTable
invoice = PrettyTable(['slno','item','quantity','price of [1 u]nit','price of n units'])
invoice.add_rows(recipt)
print(invoice)
print('-'*85)
print("      Thanks for shopping with us !!!")
print("   Visit us again , have a great day😊 !!!")







