# -*- coding: utf-8 -*-
"""
Initial template for sql from Data to Fish:
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
How to use datetime:
https://www.w3schools.com/python/python_datetime.asp

NB: Change Server to local server name!
    Need to install pyodbc which allows connection to SQL server
"""

import pyodbc
import pandas as pd
import datetime as dt


#Table names; note change to more appropriate name later
T1='dbo.tbl_BA_Beta_Output'
T2='dbo.tbl_Beta_Output'
T3='dbo.tbl_EOD_Equity_Data'
T4='dbo.tbl_EOD_Interest_Rate_Data'
T5='dbo.tbl_FTSEJSE_Index_Series'
T6='dbo.tbl_Index_Constituents'
T7='dbo.tbl_Industry_Classification_Benchmark'

#set up server object
conn=pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-Q0H6UCN\SQLEXPRESS;'
                      'Database=AIFMRM_ERS;'
                      'Trusted_Connection=yes;')

"""
#Standard call to database user a cursor, returns cursor type data

cursor=conn.cursor()
cursor.execute('SELECT TOP 1000 * FROM AIFMRM_ERS.'+T1) #String concatenation, testing whether it works
for row in cursor:
    print(row)
"""

#sql to pandas
sql_query=pd.read_sql_query('SELECT TOP 1000 * FROM AIFMRM_ERS.'+T1,conn)


#makes pandas dataframe into .csv file and also prints the data headers (bit redundant)
def MakeCsv(filename):
    sql_query.to_csv(filename+".csv")
    print("The below columns were saved to"+filename+".csv")
    print(sql_query.columns.values)

#rDate is a datetime object, datetime library has been imported to support this

#The below are currently stubs

#dbo.tbl Index Constituents
def GetICsAndWeights(table, rDate,indexCode):
    print(0)

#dbo.tbl BA Beta Output
def GetBetasMktAndSpecVols(table, rDate, ICs, mktIndexCode):
    print(0)
    
def CalcStats(weights, betas, mktVol,specVols):
    print(0)
    
    