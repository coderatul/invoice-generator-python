# Invoice-generator-python

 - A simple python program used to print invoices with some features:
   - automatic calculation
   - nice output
   - intuitive procedure
___
## Dependencies

 - pyfiglet : The ASCII text can be used to display many stylish texts by using the module pyfiglet. ![coderatul pyfiglet git main commit ](https://user-images.githubusercontent.com/72141859/116881225-fcfef480-abf0-11eb-92af-55bdf8825d1b.png)

 - PrettyTable : PrettyTable is a Python library for generating simple ASCII tables. It was inspired by the ASCII tables used in the PostgreSQL shell psql. We can control many aspects of a table, such as the width of the column padding, the alignment of text, or the table border, We can sort data. 

- DateTime : Datetime module supplies classes to work with date and time.

## Installation

- Clone the repository to your system:

```
git clone https://github.com/MySTerY1747/invoice-generator-python.git
```

- Next, cd into the program's directory:

```
cd invoice-generator-python/
```

- Install all the dependencies are met:

```
pip install -r requirements.txt
```

- Lastly, run the program using python:

```
python3 '.\invoice generator.py'
```

## Usage: 
- To change the menu, go to "menu.txt" in the root folder of the project and following the formatting in the example, describe the desired menu.
- Formatting "menu.txt":
- - make sure you don't leave any empty line in the start or in between
  - make sure all 3 elements of row are present and are seperated by a comma (,)
  - make sure that only 3 elemets are present for a row as there are only 3 columns
  - a ideal row in Menu.txt would look like -> 1, pizza, 169 
- To change the name of the restaurant, change line 7 of the code in the "invoice generator.py" file.

=======
## Features
- Menu can be modified by simpling changing Menu.txt
- Now Quantity is also shown against products added
- Other small But useful features are commented below
```
------------------- Menu -------------------
+------+----------------------------+-------+
| S.no |           Items            |  Cost |
+------+----------------------------+-------+
|  1   |         Margherita         |   75  |
|  2   |  Double cheese Margherita  |   130 |
|  3   |           Pepper           |   175 |
|  4   |  Cheese & Barbeque Chicken |   130 |
|  5   |      Veg Extravaganza      |   210 |
|  6   |           Meatza           |   245 |
|  7   |         Veg singles        |   170 |
|  8   |     Chochlate lava cake    |  160  |
|  9   |          mogumogu          |   80  |
|  10  |            coke            |   50  |
|  11  |           mazza            |   25  |
+------+----------------------------+-------+
-------------------------------------------- 

Name of Customer: atul kushwaha

 *_* enter slno. to add items or enter "q" to quit adding times *_*
 *_* if you added something by mistake then enter quantity as 0 *_*
 *_* Default Quantity is set to 1 *_*


enter the slno. of item you want to order: 2
enter quantity desired(default = 1, to skip press enter):


enter the slno. of item you want to order: 3 
enter quantity desired(default = 1, to skip press enter): 1


enter the slno. of item you want to order: 122
~ slno."122" not found, please check and enter again ~

enter the slno. of item you want to order: q
             INVOICE
Name : Atul Kushwaha
Date : 21/05/23    Time: 02:00:33
GST (%): 5
The Net Amount To Be Paid is: 320.25
The total number of item purchase : 2
------------------------------------- INVOICE -------------------------------------
+------+---------------------------+----------+-------------------+------------------+
| slno |            item           | quantity | price of [1 u]nit | price of n units |
+------+---------------------------+----------+-------------------+------------------+
|  1   |  Double cheese Margherita |    1     |         130       |       130        |
|  2   |           Pepper          |    1     |         175       |       175        |
+------+---------------------------+----------+-------------------+------------------+
-------------------------------------------------------------------------------------
      Thanks for shopping with us !!!
   Visit us again , have a great day😊 !!!
   
```
## Author:
- [Atul Kushwaha](https://github.com/coderatul)

## Contributors:
- [kiozet](https://github.com/kiozet)
- [Bhavesh_71](https://github.com/Bhavesh71)
