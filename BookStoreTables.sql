USE [BookStore]
GO

/****** Object:  Table [dbo].[Addresses]    Script Date: 1/25/3621 10:15:35 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE item.BookSupplier(
bookId nvarchar(36) not null,
supplierId nvarchar(36) not null,
booksSupplied int not null,
suppliedDate date not null,
);
GO

create table item.BookStore(
bookId nvarchar(36) not null,
storeId nvarchar(36) not null,
numberOfBooksInStore int not null
);
GO

CREATE TABLE work.StoreEmployees(
employeeId nvarchar(36) not null,
storeId nvarchar(36) not null
);
GO

create table ord.StoreBuyerOrder(
buyerId nvarchar(36) not null,
storeId nvarchar(36) not null,
orderId nvarchar(36) not null unique
);
go

create table ord.BuyerGenrePreferences(
buyerId nvarchar(36) not null,
genre nvarchar(36) not null,
);
go

create table ord.BuyerAuthorPreferences(
buyerId nvarchar(36) not null,
authorId nvarchar(36) not null,
);
go

CREATE TABLE store.Stores(
id nvarchar(36) primary key,
ownerId nvarchar(36) not null,
addressId nvarchar(36) not null,
taxP numeric(4,2) not null
);
GO

CREATE TABLE work.Employees(
id nvarchar(36) primary key clustered,
hireDate date not null,
salary smallint not null check (salary > 0),
addressId nvarchar(36) not null,
firstName nvarchar(36) not null,
lastName nvarchar(36) not null,
jobId nvarchar (50) not null,
totalWorkHours int not null,
insurance nvarchar(50) not null,
sickTime int not null,
performance char(1) not null
check (performance = 'A' or performance = 'B' or performance = 'C' or performance = 'D' or performance = 'F')
);
GO

CREATE TABLE location.Addressess(
id nvarchar(36) primary key,
address nvarchar(50) not null,
cityId nvarchar(36) not null,
phoneNumber nvarchar(36) not null unique
);
GO

CREATE TABLE ord.Buyer(
id nvarchar(36) primary key,
firstName nvarchar(36) not null,
lastName nvarchar(36) not null,
addressId nvarchar(36) not null,
creditCardNumber nvarchar(16) not null
);
GO

CREATE TABLE ord.Orders(
id nvarchar(36) primary key,
orderDate dateTime not null,
employeeId nvarchar(36),
booksSold smallint not null,
total numeric(10,2)
);
GO

CREATE TABLE item.Books(
id nvarchar(36) primary key,
title nvarchar(50) not null unique,
authorId nvarchar(36) not null,
genre nvarchar(36) not null,
publicationDate date not null,
price numeric(5,2) check (price > 0.0)
);
GO

create table item.Authors(
id nvarchar(36) primary key,
authorFirstName nvarchar(36) not null,
authorLastName nvarchar(36) not  null
);
go

CREATE TABLE item.Suppliers(
id nvarchar(36) primary key,
firstName nvarchar(36) not null,
lastName nvarchar(36) not null,
addressId nvarchar(36) not null,
companyName nvarchar(50)
);
GO

CREATE TABLE location.Cities(
id nvarchar(36) primary key,
countryName nvarchar(50) not null,
stateName nvarchar(50) not null,
cityName nvarchar(50) not null
);
GO

CREATE TABLE work.Jobs(
id nvarchar(50) primary key,
jobDescription nvarchar (100) not null,
minSalary int not null check (minSalary > 0),
maxSalary int not null check (maxSalary > 0)
);
GO

CREATE TABLE store.Owners(
id nvarchar(36) primary key,
firstName nvarchar(36) not null,
lastName nvarchar(36) not null,
addressId nvarchar(36) not null,
companyName nvarchar(50)
);
GO

create table sales.SalesDaily(
id nvarchar(36) primary key,
dayDate date not null unique,
sales numeric(15,2)
);
GO

create table sales.SalesWeekly(
id nvarchar(36) primary key,
startDate date not null unique,
endDate date unique,
sales numeric(15,2)
);
GO

create table sales.SalesMonthly(
id nvarchar(36) primary key,
startDate date not null unique,
endDate date unique,
sales numeric(15,2)
);
GO

create table sales.SalesYearly(
id nvarchar(36) primary key,
startDate date not null unique,
endDate date unique,
sales numeric(15,2)
);
GO

create table item.Warehouse(
id nvarchar(36) unique,
amount int not null
);
GO
