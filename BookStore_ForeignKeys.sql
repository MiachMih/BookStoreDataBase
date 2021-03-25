use BookStore
/*
alter table item.BookSupplier
	add foreign key (bookId) references item.Books(id);
alter table item.BookSupplier
	add foreign key (supplierId) references item.Suppliers(id);

alter table item.BookStore
	add foreign key (bookId) references item.Books(id);
alter table item.BookStore
	add foreign key (storeId) references store.Stores(id);

alter table work.StoreEmployees
	add foreign key(employeeId) references work.Employees(id);
alter table work.StoreEmployees
	add foreign key (storeId) references store.Stores(id);

alter table ord.StoreBuyer
	add foreign key(buyerId) references ord.Buyer(id);
alter table ord.StoreBuyer
	add foreign key(storeId) references store.Stores(id);
alter table ord.StoreBuyer
	add foreign key(orderId) references ord.Orders(id);

alter table ord.BuyerGenrePreferences
	add foreign key(buyerId) references ord.Buyer(id);

alter table ord.BuyerAuthorPreferences
	add foreign key(buyerId) references ord.Buyer(id);
alter table ord.BuyerAuthorPreferences
	add foreign key(authorId) references item.Authors(id);

alter table ord.SupplierOrder
	add foreign key(bookSupplierId) references item.Suppliers(id);
alter table ord.SupplierOrder
	add foreign key(orderId) references ord.Orders(id);
*/

alter table item.Warehouse
	add foreign key(id) references item.Books(id)
	on delete cascade
	go

alter table store.Stores
	add foreign key(addressId) references location.Addressess(id)
	on delete cascade
	go
alter table store.Stores
	add foreign key(ownerId) references store.Owners(id)
	on delete cascade
	go

alter table work.Employees
	add foreign key(addressId) references location.Addressess(id)
	on delete cascade
	go
alter table work.Employees
	add foreign key(jobId) references work.Jobs(id)
	on delete cascade
	go

alter table location.Addressess
	add foreign key(cityId) references location.Cities(id)
	on delete cascade
	go

alter table ord.Buyer
	add foreign key(addressId) references location.Addressess(id)
	on delete cascade
	go
/*
alter table ord.Orders
	add foreign key(bookId) references item.Books(id)
	on delete no action;
*/
alter table ord.Orders
	add foreign key(employeeId) references work.Employees(id)
	on delete cascade
	go

alter table item.Books
	add foreign key(authorId) references item.Authors(id)
	on delete cascade
	go
