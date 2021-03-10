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
from supplierOrder import SupplierOrder
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

def date(): # asks for the date
    date = ''
    date = date + input('Year: ') + '-'
    date = date + input('Month: ') + '-'
    date = date + input('Day: ')
    return date           
        
def checkJob(jobC):
    jobs = Jobs.select(column = 'id')['id']
    jobCheck = jobC
    while(True):
        for j in jobs:
            if j == jobCheck:
                return jobCheck
        print('Job Title doesn\'t exist in database. Please, try again.')
        jobCheck = input('Job Title: ')
        

def cityID(session, city, state, country):
    c = Cities.select(column = 'countryName, stateName, cityName', value = f'{country}, {state}, {city}')
    if c.empty:
        print('City isn\'t in the database, adding new entry.')
        return addCity(session, city, state, country)
    else:
        return c['id'][0]
    
def addCity(session, city, state, country):
    id = Base.generateId()
    Cities.insert(session = session, value = f'{id}, {country}, {state}, {city}')
    return id
    
def addressCheck(session, cityID): # checks until existing address is found and returns it
    address = input('Address: ')
    addressess = Addressess.select(column = 'address, cityId', value = Base.toComma([address, cityID]))
    if addressess.empty:
        print('New entry in Addressess')
        id = Base.generateId()
        adr = Base.toComma([id, address, cityID, input('Phone Number: ')])
        Addressess.insert(session = session, value = adr)
        return id
    return addressess['id'][0]
        
def storeCheck(id): # asks for input until store exists and returns the store id if it exists
    stores = Stores.select(column = 'id')['id']
    id_check = id
    while (True):
        for i in stores:
            if i == id_check:
                return id_check
        print('Store doesn\'t exist in database. Please, try again.')
        id_check = input('Store ID: ')

def checkGenerateIdAddressCity(session):
    id = Base.generateId()
    city = str(input('City: '))
    state = str(input('State: '))
    country =  str(input('Country: '))
    cityi = cityID(session, city, state ,country)
    ad = addressCheck(session, cityi)
    return id, ad

@sess # wraps the function in a session and passes down the created session to the funciton
def addEmployee(session): # adds a new employee to the work.Employees table
                                  # adds employee to the work.StoreEmployee table
                                  # adds employee's address to the location.Addressess table
                                  # adds employee's city to the location.Cities table
                                  # if employee already has address in the database, then function skips adding new entries to location.Cities & location.Addressess
    print('Adding employee')
    id, ad = checkGenerateIdAddressCity(session)
    storeID = storeCheck(input('Store ID: '))
    storempl = Base.toComma([id, str(storeID)])
    job = checkJob(str(input('Job Title: ')))
    empl = Base.toComma([id, date(), str(input('Salary: ')), ad, str(input('First Name: ')), str(input('Last Name: ')), job, '0', str(input('Insurance: ')), '0', 'A'])
    Employees.insert(session = session, value = empl)
    StoreEmployees.insert(session = session, value = storempl)
        
@sess
def addBook(session):
    print('Adding a Book')
    id = Base.generateId()
    title = input('Title: ')
    if not Books.select(column = 'title', value = title).empty:
        print('This book title already exists')
        return
    genre = input('Genre: ')
    publicationDate = date()
    price = input('Price: ')
    authorFName = input('Author First Name: ')
    authorLName =input('Author Last Name: ')
    authors = Authors.select(column = 'authorFirstName, authorLastName', value = Base.toComma([authorFName, authorLName]))
    if(authors.empty):
        authorId = Base.generateId()
        newAuthor = Base.toComma([authorId, authorFName, authorLName])
        Authors.insert(session = session, value = newAuthor)
    else:
        authorId = authors['id'][0]
    book = Base.toComma([id, title, authorId, genre, publicationDate, price])
    Books.insert(session = session, value = book)

def findBookIdByTitle():
    books = Books.select(column = 'id, title')
    bookCheck = input('Book Title: ')
    while(True):
        for book in books['title']:
            if bookCheck == book:
                bk = Books.select(column = 'title', value = bookCheck)
                return bk['id'][0]
        print('Book Title doesn\'t exist in database. Please, try again')
        bookCheck = input('Book Title: ')

def findSupplier(): # finds supplier id by first name, last name, company name
    suppliers = Suppliers.select()
    fnameCheck = input('Supplier First Name: ')
    check = True
    while(check):
        for name in suppliers['firstName']:
            if name == fnameCheck:
                check = False
        if (check):
            print('First Name doesn\'t exist in the database. Please, try again.')
            fnameCheck = input('Supplier First Name: ')
            
    lnameCheck = input('Supplier Last Name: ')
    filt = (suppliers['firstName'] == fnameCheck) & (suppliers['lastName'] == lnameCheck)
    while(suppliers.loc[filt].empty):
        print('Such supplier doesn\'t exist in the database. Please, try again.')
        lnameCheck = input('Supplier Last Name: ')
        filt = (suppliers['firstName'] == fnameCheck) & (suppliers['lastName'] == lnameCheck)
        
    cnameCheck = input('Supplier Company Name: ')
    filt = (suppliers['firstName'] == fnameCheck) & (suppliers['lastName'] == lnameCheck) & (suppliers['companyName'] == cnameCheck)
    while(suppliers.loc[filt].empty):
        print('Such supplier doesn\'t exist in the database. Please, try again.')
        cnameCheck = input('Supplier Company Name: ')
        filt = (suppliers['firstName'] == fnameCheck) & (suppliers['lastName'] == lnameCheck) & (suppliers['companyName'] == cnameCheck)
    supplierID = Suppliers.select(column = 'firstName, lastName, companyName', value = Base.toComma([fnameCheck, lnameCheck, cnameCheck]))['id'][0]
    return supplierID

def checkWarehouse(session, id):
    amount = Warehouse.select(column = 'id', value = id)['amount']
    if(amount.empty):
        Warehouse.insert(session = session, value = f'{id}, 0')
        return 0
    else:
        return int(amount[0])

@sess
def supplyBook(session):
    # when a supplier supplies books this function is called
    print('Supplying Books')
    bookID = findBookIdByTitle()
    supplierID = findSupplier()
    booksSupplied = input('How many books being supplied? : ')
    d = date()
    insrt = Base.toComma([bookID, supplierID, booksSupplied, d])
    BookSupplier.insert(session = session, value = insrt)
    bks = int(checkWarehouse(session, bookID)) + int(booksSupplied)
    Warehouse.update(session = session, column = 'amount', value = bks, id = bookID)

def checkBookAmount(session, id):
    books = int(checkWarehouse(session, id))
    print(f'Currently in possession of {books} books')
    amount =int(input(f'How many books to supply to the store? : '))
    if books == 0:
        return print('Can\'t supply any books of this title.')
    while (True):
        if (books >= amount):
            spl = books - amount
            Warehouse.update(session = session, column = 'amount', value = str(spl), id = id)
            return amount
        print('Warehouses can not supply that amount of books. Please, try again.')
        amount = int(input('How many books to supply to the store? : '))
        
def checkBookStore(session, bookID, storeID):
    num = BookStore.select(column = 'bookId, storeId', value = f'{bookID}, {storeID}')['numberOfBooksInStore']
    if num.empty:
        BookStore.insert(session = session, value = f'{bookID}, {storeID}, 0')
        return 0
    return num[0]

@sess
def populateBookStore(session):
    # adds to a particular store more books and subtracts from the warehouse
    print('Populating BookStore')
    bookID = findBookIdByTitle()
    storeID = storeCheck(input('Store ID: '))
    bookAmount = int(checkBookAmount(session, bookID)) + int(checkBookStore(session, bookID, storeID))
    BookStore.update(session = session, column = 'numberOfBooksInStore', value = f'{bookAmount}', id = f'{bookID}, {storeID}', idVALUE = 'bookId, storeId')
    
@sess
def addStore(session):
    ownerID = ''
    Session = sessionmaker(bind=Base.engine)
    s = Session()
    try:
        print('Adding Owner')
        id,  ad = checkGenerateIdAddressCity(s)
        ownerID = id
        info = Base.toComma([id, input('Owner First Name: '), input('Owner Last Name: '), ad, input('Owner Company Name: ')])
        Owners.insert(session = s, value = info)
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()
    print('Adding Store')
    storeID, storeAD = checkGenerateIdAddressCity(session)
    storeinfo = Base.toComma([storeID, ownerID, storeAD, input('Tax Percent: ')])
    Stores.insert(session = session, value = storeinfo)
    
    

@sess
def updateOwners(session):
    # allows to change an owner of the store
    pass

@sess
def deleteStore(session):
    # deletes the store and everything related to that particular store
    pass

def checkBuyer(session):
    # adds new buyer
    id,  ad = checkGenerateIdAddressCity(session)
    info = Base.toComma([id, input('First Name: '), input('Last Name: '), ad, checkCreditCard(input('Credit Card Number: '))])
    check = Buyer.select(column = 'firstName, lastName, addressId, creditCardNumber', value = Base.toComma(info[1:]))
    if not check.empty:
        return check['id'][0]
    Buyer.insert(session = session, value = info)
    return id

def checkUpdateBookAmountStore(session, bookID, storeID):
    info = Base.toComma([bookID, storeID])
    books = int(BookStore.select(column = 'bookId, storeId', value = info)['numberOfBooksInStore'][0])
    if books == 0:
        print('Book is not in the stock currently')
        return 0
    amount = int(input('How many books to buy? : '))
    while amount > books:
        print(f'Store doesn\'t have that many books right now current amount is {books}')
        amount = int(input('How many books to buy? : '))
    return amount
    BookStore.update(session = session, column = 'numberOfBooksInStore', value = (books - amount), id = info, idValue = 'bookId, storeId')

def calculateTotal(bookID, amount):
    bookPrice = float(Books.select(column = 'id', value = bookID)['price'][0])
    total = amount * bookPrice
    return round(total, 2)
    
@sess
def placeOrder(session):
    print('Placing Order')
    storeID = storeCheck(input('Current Store: '))
    print('Buyer information')
    id = Base.generateId()
    buyerID = checkBuyer(session)
    bookID = []
    amount = []
    check = True
    bookID = findBookIdByTitle()
    amount = int(checkUpdateBookAmountStore(session, bookID, storeID))
    d = date()
    employeeID = input('Employee ID: ')
    total = calculateTotal(bookID, amount)
    tax = float(Stores.select(column = 'id', value = storeID)['taxP'][0])
    total = str(total + total * (tax/100))
    info = Base.toComma([id, d, employeeID, total])
    storeBuyerInfo = Base.toComma([storeID, buyerID, id])
    Orders.insert(session = session, value = info)
    StoreBuyerOrder.insert(session = session, value = storeBuyerInfo)
    inf = Base.toComma([id, bookID, str(input('Supplier ID: ')), str(amount)])
    SupplierOrder.insert(session = session, value = inf)
    info = Base.toComma([buyerID, getAuthor(bookID)])
    BuyerAuthorPreferences.insert(session = session, value = info)
    info = Base.toComma([buyerID, getGenre(bookID)])
    BuyerGenrePreferences.insert(session = session, value = info)
    updateDaySales(session, d, total)
    
def checkCreditCard(crd):
    cardNumber = crd
    while True:
        if len(cardNumber) == 16:
            return cardNumber 
        print('Credit Card number is invalid. Please, try again')
        cardNumber = input('Credit Card Number: ')

def updateDaySales(session, day, total):
    dSale = SalesDaily.select(column = 'dayDate', value = day)
    if dSale.empty:
        id = Base.generateId()
        info = Base.toComma([id, day, str(total)])
        SalesDaily.insert(session = session, value = info)
        return
    id = dSale['id'][0]
    current = int(dSale['sales'][0])
    SalesDaily.update(session = session, column = 'sales', value = (current + int(total)), id = id)

def getAuthor(id):
    return Books.select(column = 'id', value = id)['authorId'][0]
        
def getGenre(id):
    return Books.select(column = 'id', value = id)['genre'][0]

@sess    
def updateSales(session):
    # calculates weekly, monthly, yearly Sales
    pass

@sess
def addSupplier(session):
    pass

########################
addStore()
print('Owner and Store Created')
addEmployee()
print('Employee Added')
addBook()
print('Book added')
supplyBook()
print('Book supplied')
populateBookStore()
print('Store recieved the book')
placeOrder()
print('Book ordered')
########################
