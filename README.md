# Invoice-generator-python

 - A simple python program used to print invoices with some features:
   - user can update menu using text file
   - now quantity againts products are shown
   - serial numbers are used to indenity products
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

## Author:

- [Atul Kushwaha](https://github.com/coderatul)

### Contributors:

- [kiozet](https://github.com/kiozet)
- [Bhavesh_71](https://github.com/Bhavesh71)
