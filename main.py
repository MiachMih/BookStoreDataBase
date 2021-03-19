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

# checker
def checkBookTitle(bookTitle: str) -> bool:
    return Books.select(column = 'title', value = bookTitle).empty

def checkEmployeeID(employeeID: str) -> bool:
    return Employees.select(column = 'id', value = emplyoeeID).empty

def checkCreditCard(creditCardNumber: str) -> bool:
    pass # TODO

def checkJob(jobTitle: str) -> bool:
    return Jobs.select(column = 'id', value = jobTitle).empty

def checkAddress(addressID: str) -> bool:
    return Addressess.select(column = 'id', value = addressID).empty

def checkStore(storeID: str) -> bool:
    return Stores.select(column = 'id', value = storeID).empty

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

# adder
def addAddress(addressID: str, address: str, cityID: str, phoneNumber: str) -> None:
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

def addSupplier(session, supplierID: str, supplierFirstName: str, supplierLastName: str, supplierAddress: str, supplierCompanyName: str) -> None:
    info = Base.toComma([supplierID, supplierFirstName, supplierLastName, supplierAddress, supplierCompanyName])
    Suppliers.insert(session = session, value = info)

def addBook(session, bookID: str, bookTitle: str, authorId: str, genre: str, publicationDate: str, price: str) -> None:
    book = Base.toComma([bookID, bookTitle, authorId, genre, publicationDate, price])
    Books.insert(session = session, value = book)

# getter
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

def getAuthor(bookID: str) -> str: # get and author's id by bookID
    return Books.select(column = 'id', value = bookID)['authorId'][0]

def getGenre(bookID: str) -> str: # get a genre of the book by bookID
    return Books.select(column = 'id', value = bookID)['genre'][0]

def getTax(storeID: str) -> int:
    return Stores.select(column = 'id', value = storeID)['taxP'][0]

# updater
def updateBookStore(session, bookID: str, storeID: str, amountOfBooksBought: int) -> None:
    bookStore = Base.toComma([bookID, storeID])
    numberOfBooksInStore = BookStore.select(column = 'bookId, storeId',
                                            value = bookStore)['numberOfBooksInStore'][0]
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

@sess
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
    bookID = findBookIdByTitle(bookTitle)
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
    updateBookStore(bookID, storeID, amountOfBooksToBuy)
    updateDaySales(session, total)

# editer
# TODO: implement edits
def editAuthors(session) -> None: # edit Author information
     Authors.update(session = session, column = columns, value = values, id = authorID)

def editEmployee(session) -> None: # edits employee information
    Employees.update(session = session, column = columns, value = values, id = employeeID)

def editOwners(session) -> None: # edits owner information
    Owners.update(session = session, column = columns, value = values, id = ownerID)

def editBooks(session) -> None: # edits book information
    Books.update(session = session, column = columns, value = values, id = bookID)

def editCity(session) -> None: # edits city
    Cities.update(session = session, column = columns, value = values, id = cityID)

def editAddress(session) -> None: # edits address
    Addressess.update(session = session, column = columns, value = values, id = addressID)

def editStore(session) -> None: # edits store information
    Stores.update(session = session, column = columns, value = values, id = storeID)

def editSupplier(session) -> None: # edits supplier information
    Suppliers.update(session = session, column = columns, value = values, id = supplierID)

def editJob(session) -> None: # edits job information
    Jobs.update(session = session, column = columns, value = values, id = jobID)

def editOrder(session) -> None: # edits order
    Orders.update(session = session, column = columns, value = values, id = orderID)

def editBuyer(session) -> None: # edits buyer information
    Buyer.update(session = session, column = columns, value = values, id = buyerID)

# deleter
@sess
def deleteStore(session):
    # deletes the store and everything related to that particular store
    pass

########################
# TODO implement options to choose from command line, to perform actions
########################
