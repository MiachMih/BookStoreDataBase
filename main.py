from base import Base
import pandas as pd
from authors import Authors
from books import Books
from bookStore import BookStore
from bookSupplier import BookSupplier
from suppliers import Suppliers
from addressess import Addressess
from cities import Cities
from buyer import Buyer
from buyerAuthorPreferences import BuyerAuthorPreferences
from buyerGenrePreferences import BuyerGenrePreferences
from orders import Orders
from storeBuyerOrder import StoreBuyerOrder
from salesDaily import SalesDaily
from salesWeekly import SalesWeekly
from salesMonthly import SalesMonthly
from salesYearly import SalesYearly
from owners import Owners
from stores import Stores
from employees import Employees
from jobs import Jobs
from storeEmployees import StoreEmployees
from addressBook import AddressBook
from sqlalchemy.orm.session import sessionmaker
from sess import sess
from warehouse import Warehouse
import datetime
from datetime import datetime as dt

# checker return true if empty
def checkOrderID(session, orderID) -> bool:
    return Orders.select(session = session, column = 'id', value = orderID).empty

def checkOrderList(session, columns, values) -> bool:
    return Orders.select(session = session, column = columns, value = values).empty

def checkStoreID(session, storeID: str) -> bool:
    return Stores.select(session = session, column = 'id', value = storeID).empty

def checkStore(session, storeAddressID):
    return Stores.select(session = session, column = 'addressId', value = storeAddressID).empty

def checkStoreList(session, columns, values) -> bool:
    return Stores.select(session = session, column = columns, value = values).empty

def checkBookTitle(session, bookTitle: str) -> bool:
    return Books.select(session = session, column = 'title', value = bookTitle).empty

def checkEmployeeID(session, employeeID: str) -> bool:
    return Employees.select(session = session, column = 'id', value = employeeID).empty

def checkEmployee(session, salary: str, addressID: str, firstName: str, lastName: str, jobID: str, insurance: str) -> bool:
    info = Base.toComma([salary, addressID, firstName, lastName, jobID, insurance])
    return Employees.select(session = session, column = 'salary, addressId, firstName, lastName, jobId, insurance', value = info).empty

def checkEmployeeList(session, columns: str, values: str) -> bool:
    return Employees.select(session = session, column = columns, value = values).empty

def checkOwnerID(session, ownerID) -> bool:
    return Owners.select(session = session, column = 'id', value = ownerID).empty

def checkOwnerList(session, columns, values) -> bool:
    return Owners.select(session = session, column = columns, value = values).empty

def checkBookID(session, bookID) -> bool:
    return Books.select(session = session, column = 'id', value = book).empty

def checkBookList(session, columns, values) -> bool:
    return Books.select(session = session, column = columns, value = values).empty

def checkCreditCard(session, creditCardNumber: str) -> bool:
    pass # TODO

def checkSalary(session, jobTitle: str, salary: int) -> bool:
    job = Jobs.select(session = session, column = 'id', value = jobTitle)
    return not(int(job['minSalary'][0]) <= salary and int(job['maxSalary'][0]) >= salary)

def checkJob(session, jobTitle: str) -> bool:
    return Jobs.select(session = session, column = 'id', value = jobTitle).empty

def checkJobID(session, jobID) -> bool:
    return Jobs.select(session = session, column = 'id', value = id).empty

def checkJobList(session, columns, values) -> bool:
    return Jobs.select(session = session, column = columns, value = values).empty

def checkAddressID(session, addressID: str) -> bool:
    return Addressess.select(session = session, column = 'id', value = addressID).empty

def checkAddress(session, address: str, cityID: str, phoneNumber: str) -> bool:
    info = Base.toComma([address, cityID, phoneNumber])
    return Addressess.select(session = session, column = 'address, cityId, phoneNumber', value = info).empty

def checkAddressList(session, columns, values) -> bool:
    return Addressess.select(session = session, column = columns, value = values)

def checkSupplierFirstName(session, suppliers: pd.DataFrame, firstName: str) -> bool:
    filt = suppliers['firstName'] == firstName
    return suppliers.loc[filt].empty

def checkSupplierLastName(session, suppliers: pd.DataFrame, firstName: str, lastName: str) -> bool:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName)
    return suppliers.loc[filt].empty

def checkSupplierCompanyName(session, suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> bool:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName) & (suppliers['companyName'] == companyName)
    return suppliers.loc[filt].empty

def checkBuyer(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> bool:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(session = session, column = 'firstName, lastName, creditCardNumber', value = info).empty

def checkBuyerID(session, buyerID):
    return Buyer.select(session = session, column = 'id', value = buyerID).empty

def checkBuyerList(session, columns, values):
    return Buyer.select(session = session, column = columns, value = values).empty

def checkAuthorID(session, authorID: str) -> bool:
    return Authors.select(session = session, column = 'id', value = authorID).empty

def checkAuthor(session, authorFirstName: str, authorLastName: str) -> bool:
    info = Base.toComma([authorFirstName, authorLastName])
    return Authors.select(session = session, column = 'authorFirstName, authorLastName', value = info).empty

def checkAuthorList(session, columns: str, values: str) -> bool:
    return Authors.select(session = session, column = columns, value = values).empty

def checkSupplierID(session, supplierID: str) -> bool:
    return Suppliers.select(session = session, column = 'id', value = supplierID).empty

def checkSupplier(session, supplierFirstName: str, supplierLastName: str, supplierAddressID: str, supplierCompanyName: str) -> bool:
    info = Base.toComma([supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName])
    return Suppliers.select(session = session, column = 'firstName, lastName, addressId, companyName', value = info).empty

def checkSupplierList(session, columns, values) -> bool:
    return Suppliers.select(session = session, column = columns, value = values).empty

def checkCityID(session, cityID: str) -> bool:
    return Cities.select(session = session, column = 'id', value = cityID).empty

def checkCity(session, country: str, state: str, city: str) -> bool:
    info = Base.toComma([country, state, city])
    return Cities.select(session = session, column = 'countryName, stateName, cityName', value = info).empty

def checkCityList(session, columns, values) -> bool:
    return Cities.select(session = session, column = columns, value = values).empty
# specialChecker
def specialCheckInput(inpt: str, allowedMaxLength: int) -> str:
    allowedMinLength = 2
    fixedInput = ''
    for char in inpt.strip():
        if char.isalpha():
            fixedInput += char
    if len(fixedInput) > allowedMaxLength or len(fixedInput) < allowedMinLength:
        return print(f'The allowed length is between {allowedMinLength} and {allowedMaxLength}, everything that isn\'t a letter of the alphabet is removed')
    return fixedInput

def specialCheckNumberInputVaried(inpt: str, allowedMinLength: int, allowedMaxLength: int) -> str:
    fixedInput = ''
    for num in inpt.strip():
        if num.isnumeric():
            fixedInput += num
    if fixedInput == '':
        return print(f'Allowed length is between {allowedMinLength} and {allowedMaxLength}')
    fixedInput = str(int(fixedInput))
    if len(fixedInput) < allowedMinLength or len(fixedInput) > allowedMaxLength:
        return print(f'Allowed length is between {allowedMinLength} and {allowedMaxLength}')
    return fixedInput

def specialCheckNumberInput(inpt: str, allowedLength: int) -> str:
    fixedInput = ''
    for num in inpt.strip():
        if num.isnumeric():
            fixedInput += num
    fixedInput = str(int(fixedInput))
    if len(fixedInput) != allowedLength:
        return print(f'The allowed length {allowedLength}, everything that isn\'t a number is removed')
    return fixedInput

def specialCheckStringNumberInput(inpt: str, allowedMaxLength: int) -> str:
    allowedMinLength = 2
    fixedInput = ''
    for char in inpt.strip():
        if char.isalpha() or char.isnumeric() or char == ' ':
            fixedInput += char
    if len(fixedInput) > allowedMaxLength or len(fixedInput) < allowedMinLength:
        return print(f'The allowed length is between {allowedMinLength} and {allowedMaxLength}, everything that isn\'t a letter of the alphabet, whitespace or a number is removed')
    return fixedInput

def specialCheckTax(inpt: str, length: int) -> str:
    fixedInput = ''
    isempty = True
    allowedMaxLength = length
    for char in inpt.strip():
        if char.isnumeric():
            fixedInput += char
            if isempty:
                allowedMaxLength -= 1
        if allowedMaxLength < 0:
            return print(f'The allowed length before a decimal point is {length}')
        if char == '.' and isempty: # allows only one dot to make up a float
            fixedInput += char
            isempty = False
    return str(round(float(fixedInput), 2))

def specialCheckAddress(session, address: str, cityID: str, phoneNumber: str) -> str:
    if checkAddress(session, address, cityID, phoneNumber):
        addressID = Base.generateId()
        info = Base.toComma([])
        addAddress(session, addressID, address, cityID, phoneNumber)
        return addressID
    addressID = getAddressID(session, address, cityID, phoneNumber)
    return addressID

def specialCheckCity(session, country: str, state: str, city: str) -> str:
    if checkCity(session, country, state, city):
        cityID = Base.generateId()
        addCity(session, cityID, city, state, country)
        return cityID
    cityID = getCityID(session, country, state, city)
    return cityID

def specialEditor(columns: list, listOfColumns: list) -> [list, list]:
    values = []
    tempColumns = columns.copy()
    for column in columns:
        if column in listOfColumns:
            val = input(f'Add to {column}: ')
            while(val == ''):
                print('can not be empty entry')
                val = input(f'Add to {column}: ')
            values.append(val)
        else:
            print(f'{column} is not in the list of editable columns, removing it from your list of edits')
            tempColumns.remove(column)
    return tempColumns, values

# adder
def addCity(session, cityID: str, cityName: str, stateName: str, countryName: str) -> None:
    info = Base.toComma([cityID, countryName, stateName, cityName])
    Cities.insert(session = session, value = info)

def addAddress(session, addressID: str, address: str, cityID: str, phoneNumber: str) -> None:
    addressinfo = Base.toComma([addressID, address, cityID, phoneNumber])
    Addressess.insert(session = session, value = addressinfo)

def addOwnerStore(session, ownerID: str, firstName: str, lastName: str, ownerAddressID: str, CompanyName: str, storeID: str, storeAddressID: str, taxP: str) -> None:
    ownerinfo = Base.toComma([ownerID, firstName, lastName, ownerAddressID, CompanyName])
    Owners.insert(session = session, value = ownerinfo)
    storeinfo = Base.toComma([storeID, ownerID, storeAddressID, taxP])
    Stores.insert(session = session, value = storeinfo)

def addBuyer(session, buyerID: str, buyerFirstName: str, buyerLastName: str, buyerAddressID: str, buyerCreditCard: str) -> None: # adds new buyer if doesn't exist in database. Returns id of the buyer
    info = [buyerID, buyerFirstName, buyerLastName, buyerAddressID, buyerCreditCard]
    Buyer.insert(session = session, value = Base.toComma(info))

def addOrder(session, orderID: str, employeeID: str, booksSold: str, total: str) -> None:
    orderDate = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    info = Base.toComma([orderID, orderDate, employeeID, booksSold, total])
    Orders.insert(session = session, value = info)

def addEmployee(session, storeID: str, employeeID: str, employeeAddressID: str, date: str, jobTitle: str, employeeFirstName: str, employeeLastName: str, salary: str, insurance: str) -> None:
    storeEmployee = Base.toComma([employeeID, storeID])
    employeeInformation = Base.toComma([employeeID, date, salary, employeeAddressID, employeeFirstName, employeeLastName, jobTitle, '0', insurance, '0', 'A'])
    Employees.insert(session = session, value = employeeInformation)
    StoreEmployees.insert(session = session, value = storeEmployee)

def addSupplier(session, supplierID: str, supplierFirstName: str, supplierLastName: str, supplierAddressID: str, supplierCompanyName: str) -> None:
    info = Base.toComma([supplierID, supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName])
    Suppliers.insert(session = session, value = info)

def addBook(session, bookID: str, bookTitle: str, authorId: str, genre: str, publicationDate: str, price: str) -> None:
    book = Base.toComma([bookID, bookTitle, authorId, genre, publicationDate, price])
    Books.insert(session = session, value = book)

def addAuthor(session, authorID: str, authorFirstName: str, authorLastName: str) -> None:
    info = Base.toComma([authorID, authorFirstName, authorLastName])
    Authors.insert(session = session, value = info)

# getter
def getAddressID(session, address: str, cityID: str, phoneNumber: str) -> str:
    info = Base.toComma([address, cityID, phoneNumber])
    return Addressess.select(session = session, column = 'address, cityId, phoneNumber', value = info)['id'][0]

def getMinSalary(session, jobTitle: str) -> str:
    return Jobs.select(session = session, column = 'id', value = jobTitle)['minSalary'][0]

def getMaxSalary(session, jobTitle: str) -> str:
    return Jobs.select(session = session, column = 'id', value = jobTitle)['maxSalary'][0]

def getBookIdByTitle(session, bookTitle: str) -> str:
    books = Books.select(session = session, column = 'id, title').set_index('id')
    filt = books['title'] == bookTitle
    return books.loc[filt].index[0]

def getSupplierID(session, suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> str:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName) & (suppliers['companyName'] == companyName)
    return suppliers.loc[filt].index[0]

def getWarehouseBooks(session, bookID: str) -> int:
    amount = Warehouse.select(session = session, column = 'id', value = bookID)['amount']
    if(amount.empty): # creates a new entry when book doesn't exist in warehouse
        Warehouse.insert(session = session, value = f'{bookID}, 0')
        return 0
    return int(amount[0])

def getNumberOfBooksInStore(session, bookID: str, storeID: str) -> int:
    num = BookStore.select(session = session, column = 'bookId, storeId',
                            value = f'{bookID}, {storeID}')['numberOfBooksInStore']
    if num.empty:
        BookStore.insert(session = session, value = f'{bookID}, {storeID}, 0')
        return 0
    return int(num[0])

def getBuyerAddress(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) ->str:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(session = session, column = 'firstName, lastName, creditCardNumber', value = info )['addressId'][0]

def getBuyerID(session, buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> str:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(session = session, column = 'firstName, lastName, creditCardNumber', value = info)['id'][0]

def getAuthorIDbyBookID(session, bookID: str) -> str: # get and author's id by bookID
    return Books.select(session = session, column = 'id', value = bookID)['authorId'][0]

def getAuthorID(session, authorFirstName: str, authorLastName: str) -> str:
    info = Base.toComma([authorFirstName, authorLastName])
    return Authors.select(session = session, column = 'authorFirstName, authorLastName', value = info)['id'][0]

def getGenre(session, bookID: str) -> str: # get a genre of the book by bookID
    return Books.select(session = session, column = 'id', value = bookID)['genre'][0]

def getTax(session, storeID: str) -> int:
    return Stores.select(session = session, column = 'id', value = storeID)['taxP'][0]

def getCityID(session, country: str, state: str, city: str) -> str:
    info = Base.toComma([country, state, city])
    return Cities.select(session = session, column = 'countryName, stateName, cityName', value = info)['id'][0]

# updater
def updateBookStore(session, bookID: str, storeID: str, amountOfBooksBought: int) -> None:
    bookStore = Base.toComma([bookID, storeID])
    numberOfBooksInStore = BookStore.select(session = session, column = 'bookId, storeId', value = bookStore)['numberOfBooksInStore'][0]
    info = str(int(numberOfBooksInStore) - amountOfBooksBought)
    BookStore.update(session = session, column = 'numberOfBooksInStore',
                        value = info, id = bookStore, idVALUE = 'bookId, storeId')

def updateDaySales(session, total: str) -> None: # adds up the profit over the day
    day = datetime.date.today().strftime('%Y-%m-%d')
    dSale = SalesDaily.select(session = session, column = 'dayDate', value = day)
    if dSale.empty:
        id = Base.generateId()
        info = Base.toComma([id, day, total])
        SalesDaily.insert(session = session, value = info)
        return
    id = dSale['id'][0]
    current = float(dSale['sales'][0])
    SalesDaily.update(session = session, column = 'sales', value = str(current + float(total)), id = id)

def updateSales(session):
    # calculates weekly, monthly, yearly Sales
    pass # TODO

# other
def calculateTotal(session, bookID: str, amountOfBooks: int, tax: float) -> str: # calculates total by bookID and amount of books
    bookPrice = float(Books.select(session = session, column = 'id', value = bookID)['price'][0])
    total = amountOfBooks * bookPrice
    total = total + total * (tax/100)
    return str(round(total, 2))

def findSupplier(session) -> str:
    suppliers = Suppliers.select(session = session)
    firstName = input('Supplier First name: ')
    while(checkSupplierFirstName(session, suppliers, firstName)):
        print('No such supplier')
        firstName = input('Supplier First name: ')
    lastName = input('Supplier Last name: ')
    while(checkSupplierLastName(session, suppliers, firstName, lastName)):
        print('No such supplier')
        lastName = input('Supplier Last name: ')
    companyName = input('Supplier Company name: ')
    while (checkSupplierCompanyName(session, suppliers, firstName, lastName, companyName)):
        print('No such supplier')
        companyName = input('Supplier Company name: ')
    suppliers = suppliers.set_index('id')
    return getSupplierID(session, suppliers, firstName, lastName, companyName)

def supplyBook(session, bookID: str, supplierID: str, booksSupplied: int) -> None:
    d = datetime.date.today()
    insrt = Base.toComma([bookID, supplierID, str(booksSupplied), str(d)])
    BookSupplier.insert(session = session, value = insrt)
    bookAmount = getWarehouseBooks(session, bookID) + int(booksSupplied)
    Warehouse.update(session = session, column = 'amount', value = str(bookAmount), id = bookID)

def populateBookStore(session, bookID: str, storeID: str, warehouseBooks: int) -> None:
    bookAmount = warehouseBooks + getNumberOfBooksInStore(session, bookID, storeID)
    BookStore.update(session = session, column = 'numberOfBooksInStore', value = f'{bookAmount}',
                        id = f'{bookID}, {storeID}', idVALUE = 'bookId, storeId')
    warehouseCurrentAmount = int(Warehouse.select(session = session, column = 'id', value = bookID)['amount'][0])
    Warehouse.update(session = session, column = 'amount', value = str(warehouseCurrentAmount - warehouseBooks), id = bookID)

def newBook(session, bookID: str, bookTitle: str, genre: str, publicationDate: str, price: str, authorFirstName: str, authorLastName: str) -> None:
    if checkAuthor(session, authorFirstName, authorLastName):
        authorID = Base.generateId()
        addAuthor(session, authorID, authorFirstName, authorLastName)
    else:
        authorID = getAuthorID(session, authorFirstName, authorLastName)
    addBook(session, bookID, bookTitle, authorID, genre, publicationDate, price)

def placeOrder(session):
    print('Placing Order')
    storeID = input('Current Store: ')
    while checkStoreID(session, storeID):
        storeID = input('Current Store: ')
    buyerID = Base.generateId()
    buyerFirstName = specialCheckInput(input('Buyer First Name: '), 36)
    while buyerFirstName == None:
        buyerFirstName = specialCheckInput(input('Buyer First Name: '), 36)
    buyerLastName = specialCheckInput(input('Buyer Last Name: '), 36)
    while buyerLastName == None:
        buyerLastName = specialCheckInput(input('Buyer Last Name: '), 36)
    buyerCreditCard = specialCheckNumberInput(input('Buyer Credit Card: '), 16)
    while buyerCreditCard == None:
        buyerCreditCard = specialCheckNumberInput(input('Buyer Credit Card: '), 16)
    if checkBuyer(session, buyerFirstName, buyerLastName, buyerCreditCard):
        city = specialCheckInput(input('Buyer City: '), 50)
        while city == None:
            city = specialCheckInput(input('Buyer City: '), 50)
        state = specialCheckInput(input('Buyer State: '), 50)
        while state == None:
            state = specialCheckInput(input('Buyer State: '), 50)
        country = specialCheckInput(input('Buyer Country: '), 50)
        while country == None:
            country = specialCheckInput(input('Buyer Country: '), 50)
        cityID = specialCheckCity(session, country, state, city)
        address = specialCheckStringNumberInput(input('Buyer Address: '), 50)
        while address == None:
            address = specialCheckStringNumberInput(input('Buyer Address: '), 50)
        phoneNumber = specialCheckNumberInput(input('Buyer Phone Number: '), 10)
        while phoneNumber == None:
            phoneNumber = specialCheckNumberInput(input('Buyer Phone Number: '), 10)
        buyerAddressID = specialCheckAddress(session, address, cityID, phoneNumber)
        addBuyer(session, buyerID, buyerFirstName, buyerLastName, buyerAddressID, buyerCreditCard)
    else:
        buyerID = getBuyerID(session, buyerFirstName, buyerLastName, buyerCreditCard)
    bookTitle = input('Book Title to buy: ')
    while(checkBookTitle(session, bookTitle)):
        bookTitle = input('Book Title to buy: ')
    bookID = getBookIdByTitle(session, bookTitle)
    employeeID = input('Employee ID: ')
    while(checkEmployeeID(session, employeeID)):
        employeeID = input('Employee ID: ')
    amountOfBooksToBuy = input('How many books to buy: ')
    while(getNumberOfBooksInStore(session, bookID, storeID) < int(amountOfBooksToBuy)):
        amountOfBooksToBuy = input('How many books to buy: ')
    orderID = Base.generateId()
    tax = getTax(session, storeID)
    total = calculateTotal(session, bookID, int(amountOfBooksToBuy), tax)
    addOrder(session, orderID, employeeID, amountOfBooksToBuy, total)
    updateBookStore(session, bookID, storeID, int(amountOfBooksToBuy))
    updateDaySales(session, str(total))

# editer
def editAuthor(session, columns: str, values: str, authorID: str) -> None: # edit Author information
     Authors.update(session = session, column = columns, value = values, id = authorID)

def editEmployee(session, columns: str, values: str, employeeID: str) -> None: # edits employee information
    Employees.update(session = session, column = columns, value = values, id = employeeID)

def editOwner(session, columns: str, values: str, ownerID: str) -> None: # edits owner information
    Owners.update(session = session, column = columns, value = values, id = ownerID)

def editBook(session, columns: str, values: str, bookID: str) -> None: # edits book information
    Books.update(session = session, column = columns, value = values, id = bookID)

def editCity(session, columns: str, values: str, cityID: str) -> None: # edits city
    Cities.update(session = session, column = columns, value = values, id = cityID)

def editAddress(session, columns: str, values: str, addressID: str) -> None: # edits address
    Addressess.update(session = session, column = columns, value = values, id = addressID)

def editStore(session, columns: str, values: str, storeID: str) -> None: # edits store information
    Stores.update(session = session, column = columns, value = values, id = storeID)

def editSupplier(session, columns: str, values: str, supplierID: str) -> None: # edits supplier information
    Suppliers.update(session = session, column = columns, value = values, id = supplierID)

def editJob(session, columns: str, values: str, jobID: str) -> None: # edits job information
    Jobs.update(session = session, column = columns, value = values, id = jobID)

def editOrder(session, columns: str, values: str, orderID: str) -> None: # edits order
    Orders.update(session = session, column = columns, value = values, id = orderID)

def editBuyer(session, columns: str, values: str, buyerID: str) -> None: # edits buyer information
    Buyer.update(session = session, column = columns, value = values, id = buyerID)

# deleter
def deleteStore(session, storeID):
    Stores.delete(session = session, id = storeID)

def deleteBook(session, bookID):
    Books.delete(session = session, id = bookID)

def deleteEmployee(session, employeeID):
    Employees.delete(session = session, id = employeeID)

def deleteSupplier(session, supplierID):
    Suppliers.delete(session = session, id = supplierID)

def deleteOwner(session, ownerID):
    Owners.delete(session = session, id = ownerID)

def deleteOrder(session, orderID):
    Orders.delete(session = session, id = orderID)

def deleteBuyer(session, buyerID):
    Buyer.delete(session = session, id = buyerID)

def deleteJob(session, jobID):
    Jobs.delete(session = session, id = jobID)

def deleteAddress(session, addressID):
    Addressess.delete(session = session, id = addressID)

def deleteCity(session, cityID):
    Cities.delete(session = session, id = cityID)

def deleteAuthor(session, authorID):
    Authors.delete(session = session, id = authorID)

# display
def display_main() -> list:
    print('1. Add new entry')
    print('2. Edit entry')
    print('3. Delete entry')
    print('4. Exit')
    return range(1, 5)

# TODO: redo this mess so that only things that are supposed to be addable are here
def display_Add_p1() -> list:
    print('1. Place Order')
    print('2. Populate Store with books')
    print('3. Supply books to warehouses')
    print('4. Add new book to sell')
    print('5. Add new employee to the store')
    print('6. Add new store and store owner')
    print('7. Add new supplier')
    print('0. return to main menu')
    return range(0,8)

def display_Edit_p1() -> list:
    print('1. editAuthors')
    print('2. editEmployee')
    print('3. editOwners')
    print('4. editBooks')
    print('5. editCity')
    print('6. editAddress')
    print('7. editStore')
    print('8. editSupplier')
    print('9. next page')
    print('0. get back to main page')
    return range(0, 10)

def display_Edit_p2() -> list:
    print('1. editJob')
    print('2. editOrder')
    print('3. editBuyer')
    print('4. previous page')
    print('0. get back to main page')
    return range(0, 5)

def display_Delete_p1() -> list:
    print('1. Delete Employee')
    print('2. Delete Store')
    print('3. Delete Owner')
    print('4. Delete Book')
    print('5. Delete Supplier')
    print('6. DeleteOrder')
    print('7. Delete Buyer')
    print('8. Delete Job')
    print('9. Next Page')
    return range(0, 10)

def display_Delete_p2() -> list:
    print('1. Delete Address')
    print('2. Delete City')
    print('3. Delete Author')
    print('4. Previous Page')
    return range(0, 5)

def getInput(options: list) -> str:
    query = input('Your input: ').replace('.', '')
    if query.isdigit():
        query = int(query)
    while not str(query).isdigit() or not (query in options):
        print('Your input does not match any of the options.')
        query = input('Your input: ').replace('.', '')
        if query.isdigit():
            query = int(query)
    return str(query)

@sess
def optionOne(session) -> None: # Add new entry
    options = display_Add_p1()
    query = getInput(options)
    if query == '1': # 1. Place Order
        placeOrder(session)
    elif query == '2': # 2. Populate Store with books from Warehouse
        bookTitle = input('Book Title: ')
        while(checkBookTitle(session, bookTitle)):
            print('Title isn\'t in the database')
            bookTitle = input('Book Title: ')
        bookID = getBookIdByTitle(session, bookTitle)
        warehouseBooks = specialCheckNumberInputVaried(input('Amount of books to supply: '), 1, 6)
        while warehouseBooks == None:
            warehouseBooks = specialCheckNumberInputVaried(input('Amount of books to supply: '), 1, 6)
        currentWarehouseAmount = getWarehouseBooks(session, bookID)
        if currentWarehouseAmount == 0:
            print(f'Warehouse currently out of stock on book {bookTitle}')
            return
        while(currentWarehouseAmount < int(warehouseBooks)):
            print(f'Warehouse currently in posession of {currentWarehouseAmount} books')
            print('Can not supply more than that')
            warehouseBooks = specialCheckNumberInputVaried(input('Amount of books to supply: '), 1, 6)
            while warehouseBooks == None:
                warehouseBooks = specialCheckNumberInputVaried(input('Amount of books to supply: '), 1, 6)
        storeID = input('Store ID: ').strip()
        while(checkStoreID(session, storeID)):
            print('Store isn\'t in the database')
            storeID = input('Store ID: ').strip()
        populateBookStore(session, bookID, storeID, int(warehouseBooks))
    elif query == '3': # 3. Supply books to warehouses
        bookTitle = input('Book Title: ').strip()
        while(checkBookTitle(session, bookTitle)):
            print('Title isn\'t in the database')
            bookTitle = input('Book Title: ').strip()
        bookID = getBookIdByTitle(session, bookTitle)
        supplierID = findSupplier(session)
        booksSupplied = specialCheckNumberInputVaried(input('Books supplied to warehouses: '), 1, 6)
        while booksSupplied == None:
            booksSupplied = specialCheckNumberInputVaried(input('Books supplied to warehouses: '), 1, 6)
        supplyBook(session, bookID, supplierID, booksSupplied)
    elif query == '4': # 4. Add new book to sell
        bookID = Base.generateId()
        bookTitle = specialCheckStringNumberInput(input('Book Title: '), 36)
        while bookTitle == None:
            bookTitle = specialCheckStringNumberInput(input('Book Title: '), 36)
        while(not checkBookTitle(session, bookTitle)):
            print('Book title already exists')
            bookTitle = specialCheckStringNumberInput(input('Book Title: '), 36)
            while bookTitle == None:
                bookTitle = specialCheckStringNumberInput(input('Book Title: '), 36)
        genre = specialCheckInput(input('Genre: '), 36)
        while genre == None:
            genre = specialCheckInput(input('Genre: '), 36)
        year = specialCheckNumberInput(input('Year: '), 4)
        while year == None:
            year = specialCheckNumberInput(input('Year: '), 4)
        month = specialCheckNumberInputVaried(input('Month: '), 1, 2)
        while month == None:
            month = specialCheckNumberInputVaried(input('Month: '), 1, 2)
        day = specialCheckNumberInputVaried(input('Day: '), 1, 2)
        while day == None:
            day = specialCheckNumberInputVaried(input('Day: '), 1, 2)
        price = specialCheckTax(input('Price: '), 3)
        while price == None:
            price = specialCheckTax(input('Price: '), 3)
        publicationDate = year + '-' + month + '-' + day
        authorFirstName = specialCheckInput(input('Author First Name: '), 36)
        while authorFirstName == None:
            authorFirstName = specialCheckInput(input('Author First Name: '), 36)
        authorLastName = specialCheckInput(input('Author Last Name: '), 36)
        while authorLastName == None:
            authorLastName = specialCheckInput(input('Author Last Name: '), 36)
        newBook(session, bookID, bookTitle, genre, publicationDate, price, authorFirstName, authorLastName)
    elif query == '5': # 5. Add new employee to the store
        employeeFirstName = specialCheckInput(input('Employee first name: '), 36)
        while employeeFirstName == None:
            employeeFirstName = specialCheckInput(input('Employee first name: '), 36)
        employeeLastName = specialCheckInput(input('Employee last name: '), 36)
        while employeeLastName == None:
            employeeLastName = specialCheckInput(input('Employee last name: '), 36)
        jobTitle = input('Job Title: ').strip()
        while(checkJob(session, jobTitle)):
            print('Job title doesn\'t exist')
            jobTitle = input('Job Title: ').strip()
        print(f'Salary for the job must be between {getMinSalary(session, jobTitle)} and {getMaxSalary(session, jobTitle)}')
        employeeSalary = specialCheckNumberInputVaried(input('Employee Salary: '), 1, 6)
        while employeeSalary == None:
            employeeSalary = specialCheckNumberInputVaried(input('Employee Salary: '), 1, 6)
        while(checkSalary(session, jobTitle, int(employeeSalary))):
            print(f'Salary for the job must be between {getMinSalary(session, jobTitle)} and {getMaxSalary(session, jobTitle)}')
            employeeSalary = specialCheckNumberInputVaried(input('Employee Salary: '), 1, 6)
            while employeeSalary == None:
                employeeSalary = specialCheckNumberInputVaried(input('Employee Salary: '), 1, 6)
        storeID = input('Store ID: ').strip()
        while(checkStoreID(session, storeID)):
            print('Store ID doesn\'t exist in the database')
            storeID = input('Store ID: ').strip()
        employeeCountry = specialCheckInput(input('Employee Country: '), 50)
        while employeeCountry == None:
            employeeCountry = specialCheckInput(input('Employee Country: '), 50)
        employeeState = specialCheckInput(input('Employee State: '), 50)
        while employeeState == None:
            employeeState = specialCheckInput(input('Employee State: '), 50)
        employeeCity = specialCheckInput(input('Employee City: '), 50)
        while employeeCity == None:
            employeeCity = specialCheckInput(input('Employee City: '), 50)
        employeeCityID = specialCheckCity(session, employeeCountry, employeeState, employeeCity)
        employeePhoneNumber = specialCheckNumberInput(input('Employee Phone number: '), 10)
        while employeePhoneNumber == None:
            employeePhoneNumber = specialCheckNumberInput(input('Employee Phone number: '), 10)
        employeeAddress = specialCheckStringNumberInput(input('Employee Address: '), 50)
        while employeeAddress == None:
            employeeAddress = specialCheckStringNumberInput(input('Employee Address: '), 50)
        employeeAddressID = specialCheckAddress(session, employeeAddress, employeeCityID, employeePhoneNumber)
        employeeInsurance = specialCheckInput(input('Employee Insurance: '), 50)
        while employeeInsurance == None:
            employeeInsurance = specialCheckInput(input('Employee Insurance: '), 50)
        if checkEmployee(session, employeeSalary, employeeAddressID, employeeFirstName, employeeLastName, jobTitle, employeeInsurance):
            employeeID = Base.generateId()
        else:
            print('Employee already exists in the database')
            return
        date = datetime.date.today().strftime('%Y-%m-%d')
        addEmployee(session, storeID, employeeID, employeeAddressID, date, jobTitle, employeeFirstName, employeeLastName, employeeSalary, employeeInsurance)
    elif query == '6': # 6. Add new store and store owner
        storeCountry = specialCheckInput(input('Store Country: '), 50)
        while storeCountry == None:
            storeCountry = specialCheckInput(input('Store Country: '), 50)
        storeState = specialCheckInput(input('Store State: '), 50)
        while storeState == None:
            storeState = specialCheckInput(input('Store State: '), 50)
        storeCity = specialCheckInput(input('Store City: '), 50)
        while storeCity == None:
            storeCity = specialCheckInput(input('Store City: '), 50)
        storeCityID = specialCheckCity(session, storeCountry, storeState, storeCity)
        storePhoneNumber = specialCheckNumberInput(input('Store Phone Number: '), 10)
        while storePhoneNumber == None:
            storePhoneNumber = specialCheckNumberInput(input('Store Phone Number: '), 10)
        storeAddress = specialCheckStringNumberInput(input('Store Address: '), 50)
        while storeAddress == None:
            storeAddress = specialCheckStringNumberInput(input('Store Address: '), 50)
        storeAddressID = specialCheckAddress(session, storeAddress, storeCityID, storePhoneNumber)
        if not checkStore(session, storeAddressID):
            print('Store already exists')
            return
        storeID = Base.generateId()
        taxP = specialCheckTax(input('Tax percent: '), 2)
        while taxP == None:
            taxP = specialCheckTax(input('Tax percent: '), 2)
        ownerCountry = specialCheckInput(input('Owner Country: '), 50)
        while ownerCountry == None:
            ownerCountry = specialCheckInput(input('Owner Country: '), 50)
        ownerState = specialCheckInput(input('Owner State: '), 50)
        while ownerState == None:
            ownerState = specialCheckInput(input('Owner State: '), 50)
        ownerCity = specialCheckInput(input('Owner City: '), 50)
        while ownerCity == None:
            ownerCity = specialCheckInput(input('Owner City: '), 50)
        ownerCityID = specialCheckCity(session, ownerCountry, ownerState, ownerCity)
        ownerPhoneNumber = specialCheckNumberInput(input('Phone Number: '), 10)
        while ownerPhoneNumber == None:
            ownerPhoneNumber = specialCheckNumberInput(input('Phone Number: '), 10)
        ownerAddress = specialCheckStringNumberInput(input('Owner Address: '), 50)
        while ownerAddress == None:
            ownerAddress = specialCheckStringNumberInput(input('Owner Address: '), 50)
        ownerAddressID = specialCheckAddress(session, ownerAddress, ownerCityID, ownerPhoneNumber)
        date = datetime.date.today().strftime('%Y-%m-%d')
        ownerID = Base.generateId()
        ownerFirstName = specialCheckInput(input('Owner first name: '), 36)
        while ownerFirstName == None:
            ownerFirstName = specialCheckInput(input('Owner first name: '), 36)
        ownerLastName = specialCheckInput(input('Owner last name: '), 36)
        while ownerLastName == None:
            ownerLastName = specialCheckInput(input('Owner last name: '), 36)
        ownerCompanyName = specialCheckStringNumberInput(input('Owner company name: '), 50)
        while ownerCompanyName == None:
            ownerCompanyName = specialCheckStringNumberInput(input('Owner company name: '), 50)
        addOwnerStore(session, ownerID, ownerFirstName, ownerLastName, ownerAddressID, ownerCompanyName, storeID, storeAddressID, taxP)
    elif query == '7': # 7. Add new supplier
        supplierFirstName = specialCheckInput(input('Supplier First Name: '), 36)
        while supplierFirstName == None:
            supplierFirstName = specialCheckInput(input('Supplier First Name: '), 36)
        supplierLastName = specialCheckInput(input('Supplier Last Name: '), 36)
        while supplierLastName == None:
            supplierLastName = specialCheckInput(input('Supplier Last Name: '), 36)
        supplierCountry = specialCheckInput(input('Supplier Country: '), 50)
        while supplierCountry == None:
            supplierCountry = specialCheckInput(input('Supplier Country: '), 50)
        supplierState = specialCheckInput(input('Supplier State: '), 50)
        while supplierState == None:
            supplierState = specialCheckInput(input('Supplier State: '), 50)
        supplierCity = specialCheckInput(input('Supplier City: '), 50)
        while supplierCity == None:
            supplierCity = specialCheckInput(input('Supplier City: '), 50)
        supplierCityID = specialCheckCity(session, supplierCountry, supplierState, supplierCity)
        supplierPhoneNumber = specialCheckNumberInput(input('Supplier Phone Number: '), 10)
        while supplierPhoneNumber == None:
            supplierPhoneNumber = specialCheckNumberInput(input('Supplier Phone Number: '), 10)
        supplierAddress = specialCheckInput(input('Supplier Address: '), 50)
        while supplierAddress == None:
            supplierAddress = specialCheckInput(input('Supplier Address: '), 50)
        supplierAddressID = specialCheckAddress(session, supplierAddress, supplierCityID, supplierPhoneNumber)
        supplierCompanyName = specialCheckInput(input('Supplier Company Name: '), 50)
        while supplierCompanyName == None:
            supplierCompanyName = specialCheckInput(input('Supplier Company Name: '), 50)
        if not checkSupplier(session, supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName):
            print('Supplier already exists in database')
            return
        supplierID = Base.generateId()
        addSupplier(session, supplierID, supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName)

@sess
def optionTwo(session) -> None:  # edit entry, you have to know the id of the table to edit
    options = display_Edit_p1()
    query = getInput(options)
    if query == '1': # edit AUthors
        authorID = input('Author ID: ')
        while checkAuthorID(session, authorID):
            print('Author ID doesn\'t exist in database.')
            authorID = input('Author ID: ')
        print(f'List of columns to edit ({Authors.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Authors.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkAuthorList(session, columns, values):
            editAuthor(session, columns, values, authorID)
            print('Successful edit')
            return
        print('Such author already exists')
        return
    elif query == '2': # edit Employee
            employeeID = input('Employee ID: ')
            while checkEmployeeID(session, employeeID):
                print('Employee ID doesn\'t exist in database.')
                employeeID = input('Employee ID: ')
            print(f'List of columns to edit ({Employees.columnsStr()[4:]})')
            columns = input('Write columns to edit, separating by comma: ')
            while columns == '':
                print('List can not be empty')
                columns = input('Write columns to edit, separating by comma: ')
            columns = columns.replace(' ', '')
            columns = list(set(columns.split(',')))
            if('id' in columns):
                print('id can not be edited, removing from the list of columns to edit')
                columns.remove('id')
            listOfColumns = Employees.columns()[1:]
            columns, values = specialEditor(columns, listOfColumns)
            columns = Base.toComma(columns)
            values = Base.toComma(values)
            if checkEmployeeList(session, columns, values):
                editEmployee(session, columns, values, employeeID)
                print('Successful edit')
                return
            print('Such employee already exists')
            return
    elif query == '3': # edit Owner
        ownerID = input('Owner ID: ')
        while checkOwnerID(session, ownerID):
            print('Owner ID doesn\'t exist in database.')
            ownerID = input('Owner ID: ')
        print(f'List of columns to edit ({Owners.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Owners.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkOwnerList(session, columns, values):
            editOwner(session, columns, values, ownerID)
            print('Successful edit')
            return
        print('Such owner already exists')
        return
    elif query == '4': # edit Book
        bookID = input('Book ID: ')
        while checkBookID(session, bookID):
            print('Book ID doesn\'t exist in database.')
            bookID = input('Book ID: ')
        print(f'List of columns to edit ({Books.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Books.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkBookList(session, columns, values):
            editBook(session, columns, values, bookID)
            print('Successful edit')
            return
        print('Such book already exists')
        return
    elif query == '5': # edit City
        cityID = input('City ID: ')
        while checkCityID(session, cityID):
            print('City ID doesn\'t exist in database.')
            authorID = input('City ID: ')
        print(f'List of columns to edit ({Cities.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Cities.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkCityList(session, columns, values):
            editCity(session, columns, values, cityID)
            print('Successful edit')
            return
        print('Such city already exists')
        return
    elif query == '6': # edit Address
        addressID = input('Address ID: ')
        while checkAddressID(session, addressID):
            print('Address ID doesn\'t exist in database.')
            addressID = input('Address ID: ')
        print(f'List of columns to edit ({Addressess.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Addressess.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkAddressList(session, columns, values):
            editAddress(session, columns, values, addressID)
            print('Successful edit')
            return
        print('Such address already exists')
        return
    elif query == '7': # edit Store
        storeID = input('Store ID: ')
        while checkStoreID(session, storeID):
            print('Store ID doesn\'t exist in database.')
            storeID = input('Store ID: ')
        print(f'List of columns to edit ({Stores.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Stores.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkStoreList(session, columns, values):
            editStore(session, columns, values, storeID)
            print('Successful edit')
            return
        print('Such store already exists')
        return
    elif query == '8': # edit Supplier
        supplierID = input('Supplier ID: ')
        while checkSupplierID(session, supplierID):
            print('Supplier ID doesn\'t exist in database.')
            supplierID = input('Supplier ID: ')
        print(f'List of columns to edit ({Suppliers.columnsStr()[4:]})')
        columns = input('Write columns to edit, separating by comma: ')
        columns = columns.replace(' ', '')
        columns = list(set(columns.split(',')))
        if('id' in columns):
            print('id can not be edited, removing from the list of columns to edit')
            columns.remove('id')
        listOfColumns = Suppliers.columns()[1:]
        columns, values = specialEditor(columns, listOfColumns)
        columns = Base.toComma(columns)
        values = Base.toComma(values)
        if checkSupplierList(session, columns, values):
            editSupplier(session, columns, values, supplierID)
            print('Successful edit')
            return
        print('Such supplier already exists')
        return
    elif query == '9': # next page
        options = display_Edit_p2()
        query = getInput(options)
        if query == '1': # edit Job
            jobID = input('Job ID: ')
            while checkJobID(session, jobID):
                print('Job ID doesn\'t exist in database.')
                jobID = input('Job ID: ')
            print(f'List of columns to edit ({Jobs.columnsStr()[4:]})')
            columns = input('Write columns to edit, separating by comma: ')
            columns = columns.replace(' ', '')
            columns = list(set(columns.split(',')))
            if('id' in columns):
                print('id can not be edited, removing from the list of columns to edit')
                columns.remove('id')
            listOfColumns = Jobs.columns()[1:]
            columns, values = specialEditor(columns, listOfColumns)
            columns = Base.toComma(columns)
            values = Base.toComma(values)
            if checkJobList(session, columns, values):
                editJob(session, columns, values, jobID)
                print('Successful edit')
                return
            print('Such job already exists')
            return
        elif query == '2': # edit Order
            orderID = input('Order ID: ')
            while checkOrderID(session, orderID):
                print('Order ID doesn\'t exist in database.')
                orderID = input('Order ID: ')
            print(f'List of columns to edit ({Orders.columnsStr()[4:]})')
            columns = input('Write columns to edit, separating by comma: ')
            columns = columns.replace(' ', '')
            columns = list(set(columns.split(',')))
            if('id' in columns):
                print('id can not be edited, removing from the list of columns to edit')
                columns.remove('id')
            listOfColumns = Orders.columns()[1:]
            columns, values = specialEditor(columns, listOfColumns)
            columns = Base.toComma(columns)
            values = Base.toComma(values)
            if checkOrderList(session, columns, values):
                editOrder(session, columns, values, orderID)
                print('Successful edit')
                return
            print('Such order already exists')
            return
        elif query == '3': # edit Buyer
            buyerID = input('Buyer ID: ')
            while checkBuyerID(session, buyerID):
                print('Buyer ID doesn\'t exist in database.')
                buyerID = input('Buyer ID: ')
            print(f'List of columns to edit ({Buyer.columnsStr()[4:]})')
            columns = input('Write columns to edit, separating by comma: ')
            columns = columns.replace(' ', '')
            columns = list(set(columns.split(',')))
            if('id' in columns):
                print('id can not be edited, removing from the list of columns to edit')
                columns.remove('id')
            listOfColumns = Buyer.columns()[1:]
            columns, values = specialEditor(columns, listOfColumns)
            columns = Base.toComma(columns)
            values = Base.toComma(values)
            if checkBuyerList(session, columns, values):
                editBuyer(session, columns, values, buyerID)
                print('Successful edit')
                return
            print('Such buyer already exists')
            return
        elif query == '4': # previous page
            optionTwo()

@sess
def optionThree(session) -> None: # delete entry
    options = display_Delete_p1()
    query = getInput(options)
    if query == '1':
        employeeID = input('Employee ID: ')
        while checkEmployeeID(session, employeeID):
            print('Employee ID is not in the database')
            employeeID = input('Employee ID: ')
        deleteEmployee(session, employeeID)
    elif query == '2':
        storeID = input('Store ID: ')
        while checkStoreID(session, storeID):
            storeID = input('Store ID: ')
        deleteStore(session, storeID)
    elif query == '3':
        ownerID = input('Owner ID: ')
        while checkOwnerID(session, orderID):
            ownerID = input('Owner ID: ')
        deleteOwner(session, ownerID)
    elif query == '4':
        bookID = input('Book ID: ')
        deleteBook(session, bookID)
    elif query == '5':
        supplierID = input('Supplier ID: ')
        while checkSupplierID(session, supplierID):
            supplierID = input('Supplier ID: ')
        deleteSupplier(session, supplierID)
    elif query == '6':
        orderID = input('Order ID: ')
        while checkOrderID(session, orderID):
            orderID = input('Order ID: ')
        deleteOrder(session, orderID)
    elif query == '7':
        buyerID = input('Buyer ID: ')
        while checkBuyerID(session, buyerID):
            buyerID = input('Buyer ID: ')
        deleteBuyer(session, buyerID)
    elif query == '8':
        jobID = input('Job ID: ')
        while checkJobID(session, jobID):
            jobID = input('Job ID: ')
        deleteJob(session, jobID)
    elif query == '9':
        options = displaye_Delete_p2()
        query = getInput(options)
        if query == '1':
            addressID = input('Address ID: ')
            while checkAddressID(session, addressID):
                addressID = input('Address ID: ')
            deleteAddress(session, addressID)
        elif query == '2':
            cityID = input('City ID: ')
            while checkCityID(session, cityID):
                cityID = input('City ID: ')
            deleteCity(session, cityID)
        elif query == '3':
            authorID = input('Author ID: ')
            while checkAuthorID(session, authorID):
                authorID = input('Author ID: ')
            deleteAuthor(session, authorID)
        elif query == '4':
            return optionThree()
########################
while(True):
    options = display_main()
    query = getInput(options)
    if query == '1': # Add new entry
        optionOne()
    elif query == '2': # edit entry
        optionTwo()
    elif query == '3': # delete entry
        optionThree()
        # optionThree()
    else:
        print('Exiting program')
        break
########################
