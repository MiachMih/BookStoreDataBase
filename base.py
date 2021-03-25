import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm.session import sessionmaker
import urllib
import time
import numpy as np
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt


class Base:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'DESKTOP-CUO07RF'
    database = 'BookStore'
    engine = create_engine(f'mssql+pyodbc://{server}/{database}?driver={driver}')
    conn = engine.connect()
    schema = 'work'
    table = 'EmployeeInformation'

    @classmethod # prints out methods available and other valuable information
    def help():
        print(f'''
Table: {schema}.{table}
Callable Functions:
columns(columns, value, id)
update(column=None, value=None)
insert(column=None,value=None)
select(column=None, value=None)
''')

    @classmethod # returns a list of column names of the table
    def columns(cls) -> list:
        return list(pd.read_sql_query(f'''
SELECT COLUMN_NAME as C
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = \'{cls.table}\' AND TABLE_SCHEMA= \'{cls.schema}\'''', cls.conn)['C'])

    @classmethod # returns a comma separated string of column names of the table
    def columnsStr(cls) -> str:
        return cls.toComma(cls.columns())

    @classmethod # accepts a list and turns it into a string where each element is separated by comma
    def toComma(cls, list: list) -> str:
        n = len(list)
        lis = ''
        for element in list:
            n -= 1
            lis += element
            if(n != 0):
                lis += ', '
        return lis

    @classmethod  # updates by a unique id singular row's column with the value
    # TODO update the description, check that this actually works properly
    # TODO change the idVALUE to something more meaningfull, or provide a description
    def update(cls, session, column: str, value: str, id: str, idVALUE: str ='id') -> None:
        columnUpdate = ''
        for col, val in zip(column.split(', '), value.split(', ')):
            columnUpdate = columnUpdate + f' {col} = \'{val}\','
        columnUpdate = columnUpdate[:-1]
        query = ''
        for i, v in zip(id.split(', '), idVALUE.split(', ')):
            query = query + f' {v} = \'{i}\' and'
        query = query[:-3]
        session.execute(f'''
    update {cls.schema}.{cls.table}
    set{columnUpdate}
    where{query}
    ''')

    @classmethod # returns a random unique id as a string with no whitespaces
    def generateId(cls) -> str:
        return  pd.read_sql_query('select convert(nvarchar(36),newid())', cls.conn).iloc[0].to_string().replace(' ', '').replace('-','')

    @classmethod # accepts comma separated column and value and inserts in a table that called the method
    def insert(cls, session, column: str =None,value: str =None) -> None:
        if column == None:
            column = cls.columnsStr()
        query = ''
        for val in value.split(', '):
            query = query + '\'' + val + '\', '
        query = query[:-2] # removes the last unncesessery string data
        session.execute(f'insert into {cls.schema}.{cls.table} ({column}) values ({query})')

    @classmethod # deletes a row by the specified id
    def delete(cls, session, id: str, idVALUE: str = 'id') -> None:
        query = ''
        for i, v in zip(id.split(', '), idVALUE.split(', ')):
            query = query + f' {v} = \'{i}\' and'
        query = query[:-3]
        session.execute(f'delete from {cls.schema}.{cls.table} where{query}')

    @classmethod # accepts comma separtated columns (returns all rows with information in specified columns)
                              # accepts comma separtated  column and value (returns a rows based on matching values in a columns )
                              # accepts  a value (finds an exact match of the value in any column and returns the rows)
                              #returns pandas DataFrame
    def select(cls, session, column: str =None, value: str =None) -> pd.DataFrame:
        if column != None and value !=None: # columns and values are supplied
            query  = f'select * from {cls.schema}.{cls.table} where'
            for col, val in zip(column.split(', '), value.split(', ')):
                query = query + f' {col} = \'{val}\' and'
            query = query[:-3]
            return pd.read_sql_query(query, session.connection())
        if column != None: # only columns supplied
            return pd.read_sql_query(f'select {column} from {cls.schema}.{cls.table}', session.connection())
        if value !=None: # only value supplied
            value = [value]
            x = pd.read_sql_query(f'select * from {cls.schema}.{cls.table}', session.connection())
            l = pd.DataFrame()
            for col in x.columns:
                filt = x[col].isin(value)
                if not x.loc[filt].empty:
                   l = pd.concat([l, x.loc[filt]])
            return l.drop_duplicates()

        return pd.read_sql_query(f'select * from {cls.schema}.{cls.table}', session.connection())
