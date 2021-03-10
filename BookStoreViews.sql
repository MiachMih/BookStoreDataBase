create or alter view ord.Purchase as
select o.id, o.orderDate, bo.title, bo.price, so.booksSold, o.total, b.firstName, b.lastName, b.creditCardNumber, su.companyName, st.storeId as 'storeId', a.address, r.CityName, r.stateName, sto.taxP as 'taxPercent' 
from ord.Orders as o
join ord.StoreBuyerOrder as st on st.orderId = o.id
join ord.Buyer as b on b.id = st.buyerId
join ord.SupplierOrder as so on so.orderId = o.id
join item.Suppliers as su on su.id = so.bookSupplierId
join item.Books as bo on bo.id = o.bookId
join store.Stores as sto on sto.id = st.storeId
join location.Addressess as a on a.id = sto.addressId
join location.Cities as r on r.id = a.cityId


create or alter view ord.BuyerInformationShort as
select b.id, b.firstName, b.lastName, b.creditCardNumber, a.phoneNumber, a.address, r.cityName, r.stateName, r.countryName
from ord.Buyer as b
join location.Addressess as a on a.id = b.addressId
join location.Cities as r on r.id = a.cityId


create or alter view ord.BuyerInformation as
select b.id, b.firstName, b.lastName, b.creditCardNumber, a.phoneNumber, a.address, r.cityName, r.stateName, r.countryName, au.authorFirstName as 'prefAuthorFN', au.authorLastName as 'prefAuthorLN', bg.genre 'prefGenre'
from ord.Buyer as b
join location.Addressess as a on a.id = b.addressId
join location.Cities as r on r.id = a.cityId
join ord.BuyerAuthorPreferences as ba on ba.buyerId = b.id
join item.Authors as au on au.id = ba.authorId
join ord.BuyerGenrePreferences as bg on bg.buyerId = b.id


create or alter view work.EmployeeInformation as
select e.id,e.firstName, e.lastName, j.id as 'jobTitle', e.salary, l.phoneNumber, l.address as 'employeeAddress', r.cityName as 'employeeCity', r.stateName as 'employeeState',r.countryName as 'employeeCountry', 
s.id as 'storeId', ls.address as 'storeAddress', rs.cityName as 'storeCity'
from work.Employees as e
join work.Jobs as j on e.jobId = j.id
join location.Addressess as l on  e.addressId = l.id
join location.Cities as r on l.cityId = r.id
join work.StoreEmployees as wrk on wrk.employeeId = e.id
join store.Stores as s on wrk.storeId = s.id
join location.Addressess as ls on ls.id = s.addressId
join location.Cities as rs on ls.cityId = rs.id

create or alter view store.StoreInformation as
select s.id, a.phoneNumber as 'storePhoneNumber', o.companyName as 'ownerCompanyName',
a.address as 'storeAddress', r.cityName as 'storeCity', r.stateName as 'storeState', r.countryName as 'storeCountry', eps.employeeCount
from store.Stores as s
join store.Owners as o on o.id = s.ownerId
join location.Addressess as a on a.id = s.addressId
join location.Cities as r on r.id = a.cityId
join location.Addressess as ad on ad.id = o.addressId
join location.Cities as re on re.id = ad.cityId
join dbo.employeesPerStore as eps on eps.storeId = s.id

create or alter view store.OwnerInformation as
select o.firstName as 'ownerFirstName', o.lastName as 'ownerLastName', o.companyName as 'ownerCompanyName', ad.phoneNumber as 'ownerPhoneNumber',
ad.address as 'ownerAddress', re.cityName as 'ownerCity', re.stateName as 'ownerState', re.countryName as 'ownerCountry'
from store.Owners as o
join location.Addressess as ad on ad.id = o.addressId
join location.Cities as re on re.id = ad.cityId


create or alter view item.StorageInformation as
select b.id, b.title, b.genre, b.publicationDate, b.price, au.authorFirstName as 'authorFirstName', au.authorLastName as 'authorLastName', 
s.id as 'storeId', ad.address as 'storeAddress', ad.phoneNumber as 'storePhoneNumber', r.cityName as 'storeCity', r.stateName as 'storeState', bs.numberOfBooksInStore
from item.Books as b
join item.BookStore as bs on bs.bookId = b.id
join store.Stores as s on s.id = bs.storeId
join item.Authors as au on au.id = b.authorId
join location.Addressess as ad on ad.id = s.addressId
join location.Cities as r on r.id = ad.cityId


create or alter view item.StorageSupplierInformation as
select s.id, s.firstName, s.lastName, s.companyName, a.phoneNumber, a.address, c.cityName, c.stateName, bs.booksSupplied, bs.suppliedDate
from item.Suppliers as s
join location.Addressess as a on a.id = s.addressId
join location.Cities as c on c.id = a.cityId
join item.BookSupplier as bs on bs.supplierId = s.id


create or alter view dbo.employeesPerStore as
select s.id as 'storeId', count(e.id) as 'employeeCount'
from work.Employees as e, store.Stores as s, work.StoreEmployees as se
where e.id = se.employeeId and s.id = se.storeId
group by s.id

create or alter view location.AddressBook as 
select a.id, a.address, a.phoneNumber, c.cityName, c.countryName, c.stateName
from location.Addressess as a
join location.Cities as c on c.id = a.cityId