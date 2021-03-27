@sess decorator
is used to create a session that would secure a proper transaction.
It will update tables only if the entire transaction is successful, prints an error message but the program may still run without a crash.
Decorator passes down the session, so the function that uses this decorator must accept the session as its first value,
rest of the parameters can be whatever is necessary.
----------------------------------------------------------------------------------------
Base class
Base class holds the general structure that all classes inherit. Each class in this program,
for example Books.py, simply represent the respective table in the SQL Database 'BookStore'.
Base class has all its functions under @classmethod decorator, meaning they can be called through,
the format ClassName.method(*args).
It also stores variables
driver, specifies SQL driver used, example 'ODBC Driver 17 for SQL Server'
server, specifies the server used, for this program a local server was used.
database, specifies the database to connect to.
engine, creates a connection to the database using driver, server and database
conn, creates a connection to through the engine
schema, specifies the schema of the table from the database
table, specifies the name of the table from the database
----------------------------------------------------------------------------------------
Base class methods
*Note: cls should not be passed in when calling the function using format ClassName.method(*args),
because the decorator @classmethod automatically supplies an argument for the cls parameter.
---
columns(cls) -> list:
Returns a list of columns that the table has, example ['col_1', 'col_2', 'col_3']
---
columnsStr(cls) -> str:
Returns a list of columns that the table has, but in comma separated format, example: 'col_1, col_2, col_3'
---
toComma(cls, list: list) -> str:
accepts a list and converts it to a comma separated string, example:
ClassName.toComma(['a', 'b', 'c']) -> returns str('a, b, c')
---
update(cls, session, column: str, value: str, id: str, idVALUE: str ='id') -> None:
session comes from @sess decorator that establishes a transaction session
column (accepts multiple columns), of form str('col_a, col_b, col_c'), of columns that a table needs to update
value (accepts multiple values), of form str('val_x, val_y, val_z'), of values that will come as a replacement to the updated columns
column and value work in this way: col_a = val_x, col_b = val_y, col_c = val_z. They follow the order of what column to update with which value
id and idVALUE work together to check the specified row to have updated
idVALUE (accepts multiple columns) specifies the name of the column
id (accepts multiple values) specifies the value of the column(idVALUE) that specifies a row to be updated
---
generateId(cls) -> str:
generates a unique id of length 36 and returns it as a single string value that contains alphabet letters and numbers
---
insert(cls, session, column: str =None,value: str =None) -> None:
inserts a row into the table
session comes from @sess decorator that establishes a transaction session
column (accepts multiple columns) if not specified will contain a list of all columns of the table
value (accepts multiple values) that will insert into specified columns of the table
---
delete(cls, session, id: str, idVALUE: str = 'id') -> None:
session comes from @sess decorator that establishes a transaction session
id and idVALUE work together to check the specified row to have deleted
idVALUE (accepts multiple columns) specifies the name of the column
id (accepts multiple values) specifies the value of the column(idVALUE) that specifies a row to be deleted
---
select(cls, session, column: str =None, value: str =None) -> pd.DataFrame:
session comes from @sess decorator that establishes a transaction session
column (accepts multiple columns)
if not specified will return all rows that contain the said value (in this case only accepts singular value)
value (accepts multiple values) that will return rows that match values of the respective columns
if value not specified it will return all rows of the table
----------------------------------------------------------------------------------------
main.py
contains the functions that utilize the Base class and the table classes of the database,
to manipulate the information of the database.

At the end of the file contains a command line interface that interacts with user to manipulate data
----------------------------------------------------------------------------------------
main.py functions

add Functions
The purpose of the functions of this category is to simply insert the passed data into the table

addCity(session, cityID: str, cityName: str, stateName: str, countryName: str) -> None:
addAddress(session, addressID: str, address: str, cityID: str, phoneNumber: str) -> None:
addOwnerStore(session, ownerID: str, firstName: str, lastName: str, ownerAddressID: str, CompanyName: str, storeID: str, storeAddressID: str, taxP: str) -> None:
addBuyer(session, buyerID: str, buyerFirstName: str, buyerLastName: str, buyerAddressID: str, buyerCreditCard: str) -> None:
addOrder(session, orderID: str, employeeID: str, booksSold: str, total: str) -> None:
addEmployee(session, storeID: str, employeeID: str, employeeAddressID: str, date: str, jobTitle: str, employeeFirstName: str, employeeLastName: str, salary: str, insurance: str) -> None:
addSupplier(session, supplierID: str, supplierFirstName: str, supplierLastName: str, supplierAddressID: str, supplierCompanyName: str) -> None:
addBook(session, bookID: str, bookTitle: str, authorId: str, genre: str, publicationDate: str, price: str) -> None:
addAuthor(session, authorID: str, authorFirstName: str, authorLastName: str) -> None:
----------------------------------------------------------------------------------------
get Functions
Functions of this category returns requested data from tables
Parameters serve as specifiers of the row from which the data should be returned

getAddressID(session, address: str, cityID: str, phoneNumber: str) -> str:
getMinSalary(session, jobTitle: str) -> str:
getMaxSalary(session, jobTitle: str) -> str:
getBookIdByTitle(session, bookTitle: str) -> str:
getSupplierID(session, suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> str:
getWarehouseBooks(session, bookID: str) -> int:
getNumberOfBooksInStore(session, bookID: str, storeID: str) -> int:
getBuyerAddress(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) ->str:
getBuyerID(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> str:
getAuthorIDbyBookID(session, bookID: str) -> str:
getAuthorID(session, authorFirstName: str, authorLastName: str) -> str:
getGenre(session, bookID: str) -> str:
getTax(session, storeID: str) -> int:
getCityID(session, country: str, state: str, city: str) -> str:
----------------------------------------------------------------------------------------
check Functions
They check if the rows exist and returns True if there is no such row
If the row does exist in the database the returning value is False
parameters specify a row to check on its emptiness

functions of format check*Name*List(session, columns, values) accept specific columns and value to check of the table
for example checkEmployeeList(session, columns, values),
where columns = 'hireDate, salary, firstName', value = '2014-03-15, 1250, Joe',
checks if the row's existence where those specified columns have specified values,
if it doesn't exist the function returns True, if it does exist returns False

checkOrderID(session, orderID) -> bool:
checkOrderList(session, columns: str, values: str) -> bool:
checkStoreID(session, storeID: str) -> bool:
checkStoreAddressID(session, storeAddressID: str) -> bool:
checkStoreList(session, columns: str, values: str) -> bool:
checkBookTitle(session, bookTitle: str) -> bool:
checkEmployeeID(session, employeeID: str) -> bool:
checkEmployee(session, salary: str, addressID: str, firstName: str, lastName: str, jobID: str, insurance: str) -> bool:
checkEmployeeList(session, columns: str, values: str) -> bool:
checkOwnerID(session, ownerID: str) -> bool:
checkOwnerList(session, columns: str, values: str) -> bool:
checkBookID(session, bookID: str) -> bool:
checkBookList(session, columns: str, values: str) -> bool:
checkSalary(session, jobTitle: str, salary: int) -> bool:
checkJob(session, jobTitle: str) -> bool:
checkJobID(session, jobID: str) -> bool:
checkJobList(session, columns: str, values: str) -> bool:
checkAddressID(session, addressID: str) -> bool:
checkAddress(session, address: str, cityID: str, phoneNumber: str) -> bool:
checkAddressList(session, columns: str, values: str) -> bool:
checkSupplierFirstName(session, suppliers: pd.DataFrame, firstName: str) -> bool:
checkSupplierLastName(session, suppliers: pd.DataFrame, firstName: str, lastName: str) -> bool:
checkSupplierCompanyName(session, suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> bool:
checkSupplierCompanyName(session, suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> bool:
checkBuyer(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> bool:
checkBuyerID(session, buyerID: str):
checkBuyerList(session, columns: str, values: str):
checkAuthorID(session, authorID: str) -> bool:
checkAuthor(session, authorFirstName: str, authorLastName: str) -> bool:
checkAuthorList(session, columns: str, values: str) -> bool:
checkSupplierID(session, supplierID: str) -> bool:
checkSupplier(session, supplierFirstName: str, supplierLastName: str, supplierAddressID: str, supplierCompanyName: str) -> bool:
checkSupplierList(session, columns: str, values: str) -> bool:
checkCityID(session, cityID: str) -> bool:
checkCity(session, country: str, state: str, city: str) -> bool:
checkCityList(session, columns: str, values: str) -> bool:
----------------------------------------------------------------------------------------
specialCheck Functions
special check functions are a little unique
Their purpose is to check on the validity and give appropriate response
Check each function's description individually, because their functionalities vary.

specialCheckInput(inpt: str, allowedMaxLength: int) -> str:
checks that a string is of length 2 or allowedMaxLength.
And returns only the letters of alphabet from the supplied string
specialCheckNumberInputVaried(inpt: str, allowedMinLength: int, allowedMaxLength: int) -> str:
checks that a string is of length between allowedMinLength and allowedMaxLength.
returns only numbers from the specified string (does not work with float numbers, use specialCheckTax in that case)
specialCheckStringNumberInput(inpt: str, allowedMaxLength: int) -> str:
checks that a string is of length strictly allowedMaxLength.
returns only the numbers from the specified string (does not work with float numbers, use specialCheckTax in that case)
specialCheckTax(inpt: str, length: int) -> str:
accepts floats and checks that the length before the decimal point is less than provided 'length'
returns only the float number from the supplied string with a precision of hundredths
specialCheckAddress(session, address: str, cityID: str, phoneNumber: str) -> str:
checks if the specified address exists, if it doesn't the program inserts a new row into the address table
specialCheckCity(session, country: str, state: str, city: str) -> str:
checks if the city exists if it doesn't the program inserts a new row into the cities table
specialEditor(columns: list, listOfColumns: list) -> [list, list]:
checks if the supplied columns of the table exist
columns is the user input columns they wish to edit
listOfColumns is the list of the table that the program accepts and can edit
----------------------------------------------------------------------------------------
edit Functions
edits specified columns with specified values of a specified row,
where row is specified by the supplied id

editAuthor(session, columns: str, values: str, authorID: str) -> None:
editEmployee(session, columns: str, values: str, employeeID: str) -> None:
editOwner(session, columns: str, values: str, ownerID: str) -> None:
editBook(session, columns: str, values: str, bookID: str) -> None:
editCity(session, columns: str, values: str, cityID: str) -> None:
editAddress(session, columns: str, values: str, addressID: str) -> None:
editStore(session, columns: str, values: str, storeID: str) -> None:
editSupplier(session, columns: str, values: str, supplierID: str) -> None:
editJob(session, columns: str, values: str, jobID: str) -> None:
editOrder(session, columns: str, values: str, orderID: str) -> None:
editBuyer(session, columns: str, values: str, buyerID: str) -> None:
----------------------------------------------------------------------------------------
delete Functions
deletes a row from the table using the id of that row

deleteStore(session, storeID: str) -> None:
deleteBook(session, bookID: str) -> None:
deleteEmployee(session, employeeID: str) -> None:
deleteSupplier(session, supplierID: str) -> None:
deleteOwner(session, ownerID: str) -> None:
deleteOrder(session, orderID: str) -> None:
deleteBuyer(session, buyerID: str) -> None:
deleteJob(session, jobID: str) -> None:
deleteAddress(session, addressID: str) -> None:
deleteCity(session, cityID: str) -> None:
deleteAuthor(session, authorID: str) -> None:
----------------------------------------------------------------------------------------
update Functions
this is a special case of edit functions, they allow to update the values in join tables

updateBookStore(session, bookID: str, storeID: str, amountOfBooksBought: int) -> None:
updateDaySales(session, total: str) -> None:
----------------------------------------------------------------------------------------
other Functions
These are functions help with user input and call necessary functions to insert the data in the correct tables

calculateTotal(session, bookID: str, amountOfBooks: int, tax: float) -> str:
calculates how much the specified book will cost based on the amount of books supplied
findSupplier(session) -> str:
uses various check functions to find a specific supplier that exists in the database, using first, last and company names
supplyBook(session, bookID: str, supplierID: str, booksSupplied: int) -> None:
supplies books to the warehouses which can later be distributed to the stores
populateBookStore(session, bookID: str, storeID: str, warehouseBooks: int) -> None:
supplies books to the specified store from warehouses
newBook(session, bookID: str, bookTitle: str, genre: str, publicationDate: str, price: str, authorFirstName: str, authorLastName: str) -> None:
creates a new book title and author
placeOrder(session):
creates a new buyer and adds a new order to buy the book. Calculates the total and updates the profits in the sales schemas
----------------------------------------------------------------------------------------
