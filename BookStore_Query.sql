use BookStore
select e.id,e.firstName, e.lastName, j.job, e.salary, l.address as 'Employee Address', l.phoneNumber, r.countryName as 'employee country', r.regionName as 'employee state', r.stateName, s.id as 'StoreId',
o.firstName as 'StoreOwner', ls.address as 'Store Address', rs.stateName as 'store region', rs.regionName as 'store state'
from work.Employees as e
join work.Jobs as j on e.jobId = j.id
join location.Addressess as l on  e.addressId = l.id
join location.Regions as r on l.regionId = r.id
join work.StoreEmployees as wrk on wrk.employeeId = e.id
join store.Stores as s on wrk.storeId = s.id
join store.Owners as o on o.id = s.ownerId
join location.Addressess as ls on ls.id = s.addressId
join location.Regions as rs on ls.regionId = rs.id
order by o.firstName, s.id

select o.id as 'orderId', b.id as 'buyerId', b.firstName, b.lastName, b.creditCardNumber, bo.title, au.authorFirstName, au.authorLastName, so.booksSold, st.taxP as 'taxPercentage',
su.companyName as 'supplierCompany', e.id as 'employeeId', e.firstName, e.lastName, j.job, s.storeId as 'storeId', ad.address as 'storeAddress', r.stateName as 'storeRegion', r.stateName as 'storeState'
from BookStore.ord.Buyer as b
join BookStore.location.Addressess as a on a.id = b.addressId
join BookStore.ord.StoreBuyer as s on s.buyerId = b.id
join BookStore.store.Stores as st on st.id = s.storeId
join BookStore.location.Addressess as ad on ad.id = st.addressId
join BookStore.location.Regions as r on r.id = ad.regionId
join BookStore.ord.Orders as o on s.orderId = o.id
join BookStore.work.Employees as e on e.id = o.employeeId
join BookStore.ord.SupplierOrder as so on so.orderId = o.id
join BookStore.item.Suppliers as su on so.bookSupplierId = su.id
join BookStore.item.Books as bo on bo.id = o.bookId
join BookStore.work.Jobs as j on j.id = e.jobId
join BookStore.item.Authors as au on bo.authorId = au.id