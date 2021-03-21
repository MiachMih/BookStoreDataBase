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

# checker return true if empty
def checkOrderID(orderID) -> bool:
    return Orders.select(column = 'id', value = orderID).empty

def checkOrderList(columns, values) -> bool:
    return Orders.select(column = columns, value = values).empty

def checkStoreID(storeID: str) -> bool:
    return Stores.select(column = 'id', value = storeID).empty

def checkStore(storeAddressID):
    return Stores.select(column = 'addressId', value = storeID).empty

def checkStoreList(columns, values) -> bool:
    return Stores.select(column = columns, value = values).empty

def checkBookTitle(bookTitle: str) -> bool:
    return Books.select(column = 'title', value = bookTitle).empty

def checkEmployeeID(employeeID: str) -> bool:
    return Employees.select(column = 'id', value = emplyoeeID).empty

def checkEmployee(salary: str, addressID: str, firstName: str, lastName: str, jobID: str, insurance: str) -> bool:
    info = Base.toComma([salary, addressID, firstName, lastName, jobID, insurance])
    return Employees.select(column = 'salary, addressId, firstName, lastName, jobId, insurance', value = info).empty

def checkEmployeeList(columns: str, values: str) -> bool:
    return Employees.select(column = columns, value = values).empty

def checkOwnerID(ownerID) -> bool:
    return Owners.select(column = 'id', value = ownerID).empty

def checkOwnerList(columns, values) -> bool:
    return Owners.select(column = columns, value = values).empty

def checkBookID(bookID) -> bool:
    return Books.select(column = 'id', value = book).empty

def checkBookList(columns, values) -> bool:
    return Books.select(column = columns, value = values).empty

def checkCreditCard(creditCardNumber: str) -> bool:
    pass # TODO

def checkSalary(jobTitle: str, salary: int) -> bool:
    job = Jobs.select(column = 'id', value = jobTitle)
    return not(job['minSalary'][0] <= salary and job['maxSalary'][0] >= salary)

def checkJob(jobTitle: str) -> bool:
    return Jobs.select(column = 'id', value = jobTitle).empty

def checkJobID(jobID) -> bool:
    return Jobs.select(column = 'id', value = id).empty

def checkJobList(columns, values) -> bool:
    return Jobs.select(column = columns, value = values).empty

def checkAddressID(addressID: str) -> bool:
    return Addressess.select(column = 'id', value = addressID).empty

def checkAddress(address: str, cityID: str, phoneNumber: str) -> bool:
    info = Base.toComma([address, cityID, phoneNumber])
    return Addressess.select(column = 'address, cityId, phoneNumber', value = info).empty

def checkAddressList(columns, values) -> bool:
    return Addressess.select(column = columns, value = values)

def checkSupplierFirstName(suppliers: pd.DataFrame, firstName: str) -> bool:
    filt = suppliers['firstName'] == firstName
    return suppliers.loc[filt].empty

def checkSupplierLastName(suppliers: pd.DataFrame, firstName: str, lastName: str) -> bool:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName)
    return suppliers.loc[filt].empty

def checkSupplierCompanyName(suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> bool:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName) & (suppliers['companyName'] == companyName)
    return suppliers.loc[filt].empty

def checkBuyer(buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> bool:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(column = 'firstName, lastName, creditCardNumber', value = info).empty

def checkBuyerID(buyerID):
    return Buyer.select(column = 'id', value = buyerID).empty

def checkBuyerList(columns, values):
    return Buyer.select(column = columns, value = values).empty

def checkAuthorID(authorID: str) -> bool:
    return Authors.select(column = 'id', value = authorID).empty

def checkAuthor(authorFirstName: str, authorLastName: str) -> bool:
    info = Base.toComma([authorFirstName, authorLastName])
    return Authors.select(column = 'authorFirstName, authorLastName', value = info).empty

def checkAuthorList(columns: str, values: str) -> bool:
    return Authors.select(column = columns, value = values).empty

def checkSupplierID(supplierID: str) -> bool:
    return Suppliers.select(column = 'id', value = supplierID).empty

def checkSupplier(supplierFirstName: str, supplierLastName: str, supplierAddressID: str, supplierCompanyName: str) -> bool:
    info = Base.toComma([supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName])
    return Suppliers.select(column = 'firstName, lastName, addressId, companyName', value = info).empty

def checkSupplierList(columns, values) -> bool:
    return Suppliers.select(column = columns, value = values).empty

def checkCityID(cityID: str) -> bool:
    return Cities.select(column = 'id', value = cityID).empty

def checkCity(country: str, state: str, city: str) -> bool:
    info = Base.toComma([country, state, city])
    return Cities.select(column = 'countryName, stateName, cityName', value = info).empty

def checkCityList(columns, values) -> bool:
    return Cities.select(column = columns, value = values).empty
# specialChecker
def specialCheckAddress(session, address: str, cityID: str, phoneNumber: str) -> str:
    if checkAddress(address, cityID, phoneNumber):
        addressID = Base.generateId()
        return addressID
    addressID = getAddressID(address, cityID, phoneNumber)
    return addressID

def specialCheckCity(session, country: str, state: str, city: str) -> str:
    if checkCity(country, state, city):
        cityID = Base.generaeId()
        addCity(session, cityID, city, state, country)
        return cityID
    cityID = getCItyID(country, state, city)
    return cityID

def specialEditor(columns: list, listOfColumns: list) -> [list, list]:
    values = []
    tempColumns = columns.copy()
    for column in columns:
        if column in listOfColumns:
            values.append(input(f'Add {column}: '))
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
    orderDate = datetime.date.today().strftime('%Y-%m-%d')
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
def getAddressID(address: str, cityID: str, phoneNumber: str) -> str:
    info = Base.toComma([address, cityID, phoneNumber])
    return Addressess.select(column = 'address, cityId, phoneNumber', value = info)

def getMinSalary(jobTitle: str) -> str:
    return Jobs.select(column = 'id', value = jobTitle)['minSalary'][0]

def getMaxSalary(jobTitle: str) -> str:
    return Jobs.select(column = 'id', value = jobTitle)['maxSalary'][0]

def getBookIdByTitle(bookTitle: str) -> str:
    books = Books.select(column = 'id, title').set_index('id')
    filt = books['title'] == bookTitle
    return books.loc[filt].index[0]

def getSupplierID(suppliers: pd.DataFrame, firstName: str, lastName: str, companyName: str) -> str:
    filt = (suppliers['firstName'] == firstName) & (suppliers['lastName'] == lastName) & (suppliers['companyName'] == companyName)
    return suppliers.loc[filt].index[0]

def getWarehouseBooks(session, bookID: str) -> int:
    amount = Warehouse.select(column = 'id', value = bookID)['amount']
    if(amount.empty): # creates a new entry when book doesn't exist in warehouse
        Warehouse.insert(session = session, value = f'{bookID}, 0')
        return 0
    return int(amount[0])

def getNumberOfBooksInStore(session, bookID: str, storeID: str) -> int:
    num = BookStore.select(column = 'bookId, storeId',
                            value = f'{bookID}, {storeID}')['numberOfBooksInStore']
    if num.empty:
        BookStore.insert(session = session, value = f'{bookID}, {storeID}, 0')
        return 0
    return int(num[0])

def getBuyerAddress(buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) ->str:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(column = 'firstName, lastName, creditCardNumber', value = info )['addressId'][0]

def getBuyerID(buyerFirstName: str, buyerLastName: str, buyerCreditCard: str) -> str:
    info = Base.toComma([buyerFirstName, buyerLastName, buyerCreditCard])
    return Buyer.select(column = 'firstName, lastName, creditCardNumber', value = info)['id'][0]

def getAuthorIDbyBookID(bookID: str) -> str: # get and author's id by bookID
    return Books.select(column = 'id', value = bookID)['authorId'][0]

def getAuthorID(authorFirstName: str, authorLastName: str) -> str:
    info = Base.toComma([authorFirstName, authorLastName])
    return Authors.select(column = 'authorFirstName, authorLastName', value = info)['id'][0]

def getGenre(bookID: str) -> str: # get a genre of the book by bookID
    return Books.select(column = 'id', value = bookID)['genre'][0]

def getTax(storeID: str) -> int:
    return Stores.select(column = 'id', value = storeID)['taxP'][0]

def getCityID(country: str, state: str, city: str) -> str:
    info = Base.toComma([country, state, city])
    return Cities.select(column = 'countryName, stateName, cityName', value = info)['id'][0]

# updater
def updateBookStore(session, bookID: str, storeID: str, amountOfBooksBought: int) -> None:
    bookStore = Base.toComma([bookID, storeID])
    numberOfBooksInStore = BookStore.select(column = 'bookId, storeId', value = bookStore)['numberOfBooksInStore'][0]
    info = str(numberOfBooksInStore - amountOfBooksBought)
    BookStore.update(session = session, column = 'numberOfBooksInStore',
                        value = info, id = bookStore, idVALUE = 'bookId, storeId')

def updateDaySales(session, total) -> None: # adds up the profit over the day
    day = datetime.date.today().strftime('%Y-%m-%d')
    dSale = SalesDaily.select(column = 'dayDate', value = day)
    if dSale.empty:
        id = Base.generateId()
        info = Base.toComma([id, day, str(total)])
        SalesDaily.insert(session = session, value = info)
        return
    id = dSale['id'][0]
    current = int(dSale['sales'][0])
    SalesDaily.update(session = session, column = 'sales', value = (current + int(total)), id = id)

def updateSales(session):
    # calculates weekly, monthly, yearly Sales
    pass # TODO

# other
def calculateTotal(bookID: str, amountOfBooks: int, tax: float) -> str: # calculates total by bookID and amount of books
    bookPrice = float(Books.select(column = 'id', value = bookID)['price'][0])
    total = amountOfBooks * bookPrice
    total = total + total * (tax/100)
    return str(round(total, 2))

def findSupplier() -> str:
    suppliers = Suppliers.select()
    firstName = input('First name: ')
    while(checkSupplierFirstName(suppliers, firstName)):
        firstName = input('First name: ')
    lastName = input('Last name: ')
    while(checkSupplierLastName(suppliers, firstName, lastName)):
        lastName = input('Last name: ')
    companyName = input('Company name: ')
    while (checkSupplierCompanyName(suppliers, firstName, lastName, companyName)):
        companyName = input('Company name: ')
    suppliers = suppliers.set_index('id')
    return findSupplierID(suppliers, firstName, lastName, companyName)

def supplyBook(session, bookID: str, supplierID: str, booksSupplied: int) -> None:
    d = datetime.date.today()
    insrt = Base.toComma([bookID, supplierID, str(booksSupplied), d])
    BookSupplier.insert(session = session, value = insrt)
    bookAmount = getWarehouseBooks(session, bookID) + booksSupplied
    Warehouse.update(session = session, column = 'amount', value = bookAmount, id = bookID)

def populateBookStore(session, bookID: str, storeID: str, warehouseBooks: int) -> None:
    bookAmount = warehouseBooks + getNumberOfBooksInStore(session, bookID, storeID)
    BookStore.update(session = session, column = 'numberOfBooksInStore', value = f'{bookAmount}',
                        id = f'{bookID}, {storeID}', idVALUE = 'bookId, storeId')
    warehouseCurrentAmount = int(Warehouse.select(column = 'id', value = bookID)['amount'][0])
    Warehouse.update(session = session, column = 'amount', value = str(warehouseCurrentAmount - warehouseBooks))

def newBook(session, bookID: str, bookTitle: str, genre: str, publicationDate: str, price: str, authorFirstName: str, authorLastName: str) -> None:
    if checkAuthor(authorFirstName, authorLastName):
        authorID = Base.generateId()
        addAuthor(session, authorID, authorFirstName, authorLastName)
    else:
        authorID = getAuthorID(authorFirstName, authorLastName)
    addBook(bookID, bookTitle, authorID, genre, publciationDate, price)

def placeOrder(session):
    print('Placing Order')
    storeID = input('Current Store: ')
    while checkStore(storeID):
        storeID = input('Current Store: ')
    buyerID = Base.generateId()
    buyerFirstName = input('Buyer First Name: ')
    buyerLastName = input('Buyer Last Name: ')
    buyerCreditCard = input('Buyer Credit Card: ')
    if checkBuyer(buyerFirstName, buyerLastName, buyerCreditCard):
        city = input('City: ')
        state = input('State: ')
        country = input('Country: ')
        cityID = checkAddCityID(session, city, state, country)
        address = input('Address: ')
        buyerAddressID = checkAddAddress(session, cityID)
        addBuyer(session, buyerID, buyerFirstName, buyerLastName, buyerAddressID, buyerCreditCard)
    else:
        buyerID = getBuyerID(buyerFirstName, buyerLastName, buyerCreditCard)
    bookTitle = input('Book Title to buy: ')
    while(checkBookTitle(bookTitle)):
        bookTitle = input('Book Title to buy: ')
    bookID = getBookIdByTitle(bookTitle)
    employeeID = input('Employee ID: ')
    while(checkEmployeeID(employeeID)):
        employeeID = input('Employee ID: ')
    amountOfBooksToBuy = input('How many books to buy: ')
    while(getNumberOfBooksInStore(session, bookID, storeID) < amountOfBooksToBuy):
        amountOfBooksToBuy = input('How many books to buy: ')
    orderID = Base.generateId()
    tax = getTax(storeID)
    total = calculateTotal(bookID, amountOfBooksToBuy, tax)
    addOrder(session, orderID, employeeID, amountOfBooksToBuy, total)
    updateBookStore(session, bookID, storeID, amountOfBooksToBuy)
    updateDaySales(session, total)

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
def deleteStore(session):
    # deletes the store and everything related to that particular store
    pass

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

def display_Delete() -> list:
    print('1. Delete Employee')
    print('2. Delete Store & Owner')
    print('3. Delete ')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

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
        placeOrder()
    elif query == '2': # 2. Populate Store with books from Warehouse
        bookTitle = input('Book Title: ')
        while(checkBookTitle(bookTitle)):
            print('Title isn\'t in the database')
            bookTitle = input('Book Title: ')
        bookID = getBookIdByTitle(bookTitle)
        warehouseBooks = input('Amount of books to supply: ')
        currentWarehouseAmount = getWarehouseBooks(session, bookID)
        if currentWarehouseAmount == 0:
            print(f'Warehouse currently out of stock of book {bookTitle}')
            return optionOne()
        while(currentWarehouseAmount < warehouseBooks):
            print(f'Warehouse currently in posession of {currentWarehouseAmount} books')
            print('Can not supply more than that')
            warehouseBooks = input('Amount of books to supply: ')
        storeID = input('Store ID: ')
        while(checkStoreID(storeID)):
            print('Store isn\'t in the database')
            storeID = input('Store ID: ')
        populateBookStore(session, bookID, storeID, warehouseBooks)
    elif query == '3': # 3. Supply books to warehouses
        bookTitle = input('Book Title: ')
        while(checkBookTitle(bookTitle)):
            print('Title isn\'t in the database')
            bookTitle = input('Book Title: ')
        bookID = getBookIdByTitle(bookTitle)
        supplierID = findSupplier()
        supplyBook(session, bookID, supplierID, booksSupplied)
    elif query == '4': # 4. Add new book to sell
        bookID = Base.generateId()
        bookTitle = input('Book Title: ')
        while(not checkBookTitle(bookTitle)):
            print('Book title already exists')
            bookTitle = input('Book Title: ')
        genre = input('Genre: ')
        year = input('Year: ')
        month = input('Month: ')
        day = input('Day: ')
        price = input('Price')
        authorFirstName = input('First Name: ')
        authorLastName = input('Last Name: ')
        newBook(session, bookID, bookTitle, genre, publicationDate, price, authorFirstName, authorLastName)
    elif query == '5': # 5. Add new employee to the store
        employeeFirstName = input('Employee first name: ')
        employeeLastName = input('Employee last name: ')
        jobTitle = input('Job Title: ')
        while(checkJob(jobTitle)):
            print('Job title doesn\'t exist')
            jobTitle = input('Job Title: ')
        employeeSalary = input('Employee Salary: ')
        while(checkSalary(jobTitle, employeeSalary)):
            print(f'Salary for the job must be between {getMinSalary(jobTitle)} and {getMaxSalary(jobTitle)}')
            employeeSalary = input('Employee Salary: ')
        storeID = input('Store ID: ')
        while(checkStoreID(storeID)):
            print('Store ID doesn\'t exist in the database')
            storeID = input('Store ID: ')
        employeeCountry = input('Employee Country: ')
        employeeState = input('Employee State: ')
        employeeCity = input('Employee City: ')
        employeeCityID = specialCheckCity(session, employeeCountry, employeeState, employeeCity)
        employeePhoneNumber = input('Employee Phone number: ')
        employeeAddress = input('Employee Address: ')
        employeeAddressID = specialCheckAddress(session, employeeAddress, employeeCityID, employeePhoneNumber)
        employeeInsurance = input('Employee Insurance: ')
        if checkEmployee(salary, employeeAddressID, employeeFirstName, employeeLastName, jobTitle, employeeInsurance):
            employeeID = Base.generaeId()
        else:
            print('Employee already exists in the database')
            return optionOne()
        date = datetime.date.today().strftime('%Y-%m-%d')
        addEmployee(session, storeID, employeeID, employeeAddressID, date, jobTitle, employeeFirstName, employeeLastName, employeeSalary, employeeInsurance)
    elif query == '6': # 6. Add new store and store owner
        storeCountry = input('Store Country: ')
        storeState = input('Store State: ')
        storeCity = input('Store City: ')
        storeCityID = specialCheckCity(session, storeCountry, storeState, storeCity)
        storePhoneNumber = input('Store Number: ')
        storeAddress = input('Store Address: ')
        storeAddressID = specialCheckAddress(session, storeAddress, storeCityID, storePhoneNumber)
        if not checkStore(storeAddressID):
            print('Store already exists')
            return optionOne()
        storeID = Base.generateId()
        taxP = input('Tax percent: ')
        ownerCountry = input('Owner Country: ')
        ownerState = input('Owner State: ')
        ownerCity = input('Owner City: ')
        ownerCityID = specialCheckCity(session, ownerCountry, ownerState, ownerCity)
        ownerPhoneNumber = input('Phone Number: ')
        ownerAddress = input('Owner Address: ')
        employeeAddressID = specialCheckAddress(session, ownerAddress, ownerCityID, ownerPhoneNumber)
        date = datetime.date.today().strftime('%Y-%m-%d')
        addOwnerStore(session, ownerID, ownerFirstName, ownerLastName, ownerAddressID, ownerCompanyName, storeID, storeAddressID, taxP)
    elif query == '7': # 7. Add new supplier
        supplierFirstName = input('Supplier First Name: ')
        supplierLastName = input('Supplier Last Name: ')
        supplierCountry = input('Supplier Country: ')
        supplierState = input('Supplier State: ')
        supplierCity = input('Supplier City: ')
        supplierCityID = specialCheckCity(session, supplierCountry, supplierState, supplierCity)
        supplierPhoneNumber = input('Supplier Phone Number: ')
        supplierAddress = input('Supplier Address: ')
        supplierAddressID = specialCheckAddress(session, supplierAddress, supplierCityID, supplierPhoneNumber)
        supplierCompanyName = input('Supplier Company Name: ')
        if not checkSupplier(supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName):
            print('Supplier already exists in database')
            return optionOne()
        supplierID = Base.generateId()
        addSupplier(session, supplierID, supplierFirstName, supplierLastName, supplierAddressID, supplierCompanyName)

@sess
def optionTwo(session) -> None:  # edit entry, you have to know the id of the table to edit
    options = display_Edit_p1()
    query = getInput(options)
    if query == '1': # edit AUthors
        authorID = input('Author ID: ')
        while checkAuthorID(authorID):
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
        if checkAuthorList(columns, values):
            editAuthor(session, columns, values, authorID)
            print('Successful edit')
            return optionTwo()
        print('Such author already exists')
        return optionTwo()
    elif query == '2': # edit Employee
            employeeID = input('Employee ID: ')
            while checkEmployeeID(employeeID):
                print('Employee ID doesn\'t exist in database.')
                authorID = input('Employee ID: ')
            print(f'List of columns to edit ({Employees.columnsStr()[4:]})')
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
            if checkEmployeeList(columns, values):
                editEmployee(session, columns, values, employeeID)
                print('Successful edit')
                return optionTwo()
            print('Such employee already exists')
            return optionTwo()
    elif query == '3': # edit Owner
        ownerID = input('Owner ID: ')
        while checkOwnerID(ownerID):
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
        if checkOwnerList(columns, values):
            editOwner(session, columns, values, ownerID)
            print('Successful edit')
            return optionTwo()
        print('Such owner already exists')
        return optionTwo()
    elif query == '4': # edit Book
        bookID = input('Book ID: ')
        while checkBookID(bookID):
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
        if checkBookList(columns, values):
            editBook(session, columns, values, bookID)
            print('Successful edit')
            return optionTwo()
        print('Such book already exists')
        return optionTwo()
    elif query == '5': # edit City
        cityID = input('City ID: ')
        while checkCityID(cityID):
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
        if checkCityList(columns, values):
            editCity(session, columns, values, cityID)
            print('Successful edit')
            return optionTwo()
        print('Such city already exists')
        return optionTwo()
    elif query == '6': # edit Address
        addressID = input('Address ID: ')
        while checkAddressID(addressID):
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
        if checkAddressList(columns, values):
            editAddress(session, columns, values, addressID)
            print('Successful edit')
            return optionTwo()
        print('Such address already exists')
        return optionTwo()
    elif query == '7': # edit Store
        storeID = input('Store ID: ')
        while checkStoreID(storeID):
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
        if checkStoreList(columns, values):
            editStore(session, columns, values, storeID)
            print('Successful edit')
            return optionTwo()
        print('Such store already exists')
        return optionTwo()
    elif query == '8': # edit Supplier
        supplierID = input('Supplier ID: ')
        while checkSupplierID(supplierID):
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
        if checkSupplierList(columns, values):
            editSupplier(session, columns, values, supplierID)
            print('Successful edit')
            return optionTwo()
        print('Such supplier already exists')
        return optionTwo()
    elif query == '9': # next page
        options = display_Edit_p2()
        query = getInput(options)
        if query == '1': # edit Job
            jobID = input('Job ID: ')
            while checkJobID(jobID):
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
            if checkJobList(columns, values):
                editJob(session, columns, values, jobID)
                print('Successful edit')
                return optionTwo()
            print('Such job already exists')
            return optionTwo()
        elif query == '2': # edit Order
            orderID = input('Order ID: ')
            while checkOrderID(orderID):
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
            if checkOrderList(columns, values):
                editOrder(session, columns, values, orderID)
                print('Successful edit')
                return optionTwo()
            print('Such order already exists')
            return optionTwo()
        elif query == '3': # edit Buyer
            buyerID = input('Buyer ID: ')
            while checkBuyerID(buyerID):
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
            if checkBuyerList(columns, values):
                editBuyer(session, columns, values, buyerID)
                print('Successful edit')
                return optionTwo()
            print('Such buyer already exists')
            return optionTwo()
        elif query == '4': # previous page
            optionTwo()

@sess
def optionThree(session) -> None: # delete entry
    options = display_Delete()
    query = getInput(options)
    if query == '1':
        pass
    elif query == '2':
        pass
    elif query == '3':
        pass
    elif query == '4':
        pass
    elif query == '5':
        pass
    elif query == '6':
        pass
    elif query == '7':
        pass
    elif query == '8':
        pass
    elif query == '9':
        pass
########################
# TODO implement options to choose from command line, to perform actions
while(True):
    options = display_main()
    query = getInput(options)
    if query == '1': # Add new entry
        optionOne()
    elif query == '2': # edit entry
        optionTwo()
    elif query == '3': # delete entry
        print('We are under construction right now, please check in later.')
        # optionThree()
    else:
        print('Exiting program')
        break
########################
