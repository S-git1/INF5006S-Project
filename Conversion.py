# -*- coding: utf-8 -*-
"""
Convert SQL tables into .csv and JavaScript Array files
Initial template for sql from Data to Fish:
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/

Serialization of datetime code
https://code-maven.com/serialize-datetime-object-as-json-in-python

NB: Change Server to local server name!
    Need to install pyodbc which allows connection to SQL server
"""

#importing requisite libraries
import pyodbc
import pandas as pd
import json
import datetime as dt
#set up server object
conn=pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-Q0H6UCN\SQLEXPRESS;'
                      'Database=AIFMRM_ERS;'
                      'Trusted_Connection=yes;')
    
#Table names; note change to more appropriate variable names later
T1='dbo.tbl_BA_Beta_Output'
T2='dbo.tbl_Beta_Output'
T3='dbo.tbl_EOD_Equity_Data'
T4='dbo.tbl_EOD_Interest_Rate_Data'
T5='dbo.tbl_FTSEJSE_Index_Series'
T6='dbo.tbl_Index_Constituents'
T7='dbo.tbl_Industry_Classification_Benchmark'

#list of table names for easy traversal
tbls=[T1,T2,T3,T4,T5,T6,T7]

#gives json.dump a default function if it encounters some unknown type
def dtConvert(o):
    if isinstance(o, dt.datetime):
        return "{}-{}-{}".format(o.year, o.month, o.day)
  

#makes pandas dataframe into .csv and .js file and also prints the data headers
#Note: there is also a way to convert straight from pandas to json filetype but format not guaranteed as jsarray
def Convert2Files(filename,df):
    df.to_csv(filename+".csv") #.csv
    #df.to_json(filename+".csv") #Json
    with open(filename+".js", "w") as fp:  
        json.dump(df.to_dict("records"), fp, default=dtConvert) #.js
        
    print("The following columns were saved to"+filename+".csv and jsarrays in .js:")
    print(df.columns.values)

#converting each table from query to .csv and js
for i in tbls:
    sql_query = pd.read_sql_query('SELECT * FROM AIFMRM_ERS.'+i,conn)
    Convert2Files(i,sql_query)



#some test code: check conversion of file to an JSarray structure
temp=pd.DataFrame({"testcol":[1,2,3,4],"testcol2":[2,3,4,5], "testcol3":[1,2,3,4]})
#This gets it in js array of objects format
print(type(temp.to_dict('records')))
#just checking: case of going straight to json from pandas
print(temp.to_json())
#transposing the pandas frame
print(temp.T.to_json())