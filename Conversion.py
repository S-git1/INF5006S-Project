# -*- coding: utf-8 -*-
"""
Convert SQL tables into .csv and JavaScript Array files
Initial template for sql from Data to Fish:
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/

Serialization of datetime code
https://code-maven.com/serialize-datetime-object-as-json-in-python

NB: Change Server to local server name!
    Need to install pyodbc which allows connection to SQL server

NB: is Index is used to call a column name in SQL it must be in double quotes as Index is a special character in sql
"""

#importing requisite libraries
import pyodbc
import numpy as np
import pandas as pd
import json
import datetime as dt
#set up server object
conn=pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-Q0H6UCN\SQLEXPRESS;'
                      'Database=AIFMRM_ERS;'
                      'Trusted_Connection=yes;')
    
#Table names; note change to more appropriate variable names later
T1='AIFMRM_ERS.dbo.tbl_BA_Beta_Output'
T2='AIFMRM_ERS.dbo.tbl_Beta_Output'
T3='AIFMRM_ERS.dbo.tbl_EOD_Equity_Data'
T4='AIFMRM_ERS.dbo.tbl_EOD_Interest_Rate_Data'
T5='AIFMRM_ERS.dbo.tbl_FTSEJSE_Index_Series'
T6='AIFMRM_ERS.dbo.tbl_Index_Constituents'
T7='AIFMRM_ERS.dbo.tbl_Industry_Classification_Benchmark'

#list of table names for easy traversal
tbls=[T1,T2,T3,T4,T5,T6,T7]


boundary1=dt.datetime(2017,9,1) #sql database boundary for first date
boundary2=dt.datetime(2021,3,1) #sql database boundary for last date
month=[3,6,9,12]
mktC = ["J203", "J200", "J250", "J257", "J258"]

#gives json.dump a default function if it encounters some unknown type
def dtConvert(o):
    if isinstance(o, dt.datetime):
        return "{}-{}-{}".format(o.year, o.month, o.day)
  

#makes pandas dataframe into .csv and .js file and also prints the data headers
#Note: there is also a way to convert straight from pandas to json filetype but format not guaranteed as jsarray
#Currently csv version disabled otherwise takes script too long to run
def Convert2Files(filename,df):
    df.to_csv("./data/csv/"+filename+".csv") #.csv
    #df.to_json(filename+".csv") #Json
    with open("./data/js/"+filename+".js", "w") as fp:  
        json.dump(df.to_dict("records"), fp, default=dtConvert) #.js
        
    print("\nThe following columns were saved to"+filename+".csv and jsarrays in .js:")
    print(df.columns.values)

#converting each table from query to .csv and js
def allTables():
    for i in tbls:
        sql_query = pd.read_sql_query('SELECT * '+i,conn)
        Convert2Files(i,sql_query)







#function which converts sql query to csv and js for all index tables
#every table had the quarter and year of a row appended as a column attribute
#tables outputted to file are:
# - composite of all the index tables with additional columns to identify marketIndexCode, Year, Quarter (1 file) ---> set m=0 to not print to file
# - Index tables by quarter and year (15 files if start date (s) and end date (e) set for full period) ---> set q=0 to not print to file
# - Index tables by Index (5 files if full set of market index codes (mktc) used) ---> set m=0 to not print tp file
#By default it will output all files above ----> call IndexTables()
# Note: Index tables by quarter and Index tables by Index can be constructed by filtering the composite table
def IndexTables(s=boundary1, e=boundary2, mktC=mktC,a=1,q=1,m=1):
    #month=[3,6,9,12] #is a globa variable but its here just in case
    byMarket={
        "J203": None,
        "J200": None,
        "J250": None,
        "J257": None,
        "J258": None
        }
    
    for y in range(s.year,e.year+1):
        for i in range(0,4,1):
            print("#################QUARTER TEST######################")
            
            start=dt.datetime(y,month[i],1)
            end=dt.datetime(y,(month[i]+1)%12,1) # necessary because case of the 31st and 30th being end of month
            if (start.month==12):
                end=dt.datetime(end.year+1,1,1)
            #Must check date in acceptable range
            if(start<s or start>e):
                continue
            print(start)
            
            #query sql
            sql_query = pd.read_sql_query('SELECT Date, "Index" as "MarketID","Index Code" AS Code, "Index Name" AS Name, "Index Type", "Start Date","End Date","% Days Traded","Data Points", Alpha, Beta, "SE Alpha", "SE Beta", "p-Value Alpha", "p-Value Beta",R2, "Total Risk","Unique Risk" FROM '+T5+', '+T1+' WHERE Instrument like \'____\' AND Instrument ="Index Code" AND "Index" in (\'J203\', \'J200\', \'J250\', \'J257\', \'J258\') AND Date>\''+str(start)+'.000\' AND Date<\''+str(end)+'.000\' ORDER BY "Index Type"',conn)
            rows_returned=sql_query.shape[0]
            
            #making extra column for year and quarter and adjusting date to reference
            Year=np.ones(rows_returned)*start.year
            Quarter=np.ones(rows_returned)*(i+1)
            sql_query["Year"]=Year
            sql_query["Quarter"]=Quarter
            #sql_query["Date"]=start  #setting date to reference date
            
            if (a==1 or m==1):
                for j in mktC:
                    #check whether is first entry in dictionary
                    if (byMarket[j] is None):
                        byMarket[j]=sql_query[sql_query["MarketID"]==j]
                    else:
                        byMarket[j]=byMarket[j].append(sql_query[sql_query["MarketID"]==j])
                
            
            #makeing each quarter's index entries to file
            if (q==1):
                fname="IY"+str(start.year)+"Q"+str(i+1)
                Convert2Files(fname, sql_query)
            
    #making files by market
    if (m==1):
        for c in mktC:
            tbl=byMarket[c]
            fname='I'+c
            Convert2Files(fname, tbl)         
    
    #full set irrespective of market and date
    if(a==1):
        fname="indexTableView"
        Convert2Files(fname, pd.concat(mktC.values())) 
        print("full fileset complete")           
    return byMarket

############Note: this takes 30-40 minutes to run on i7 24GBRAM to generate all files
#                   just printing the composite takes 20 minutes
#function which converts sql query to csv and js for all share tables
#every table had the quarter and year of a row appended as a column attribute
#tables outputted to file are:
# - composite of all the Share tables with additional columns to identify marketIndexCode, Year, Quarter (1 file)
# - Share tables by quarter and year (15 files if start date (s) and end date (e) set for full period)
# - Share tables by Index (5 files if full set of market index codes (mktc) used)
#By default it will output all files above ---> call ShareTables()
# Note: share tables by quarter and share tables by market can be constructed by filtering the composite table
def ShareTables(s=boundary1, e=boundary2, mktC=mktC,a=1,q=1,m=1):
    month=[3,6,9,12]
    byMarket={
        "J203": None,
        "J200": None,
        "J250": None,
        "J257": None,
        "J258": None
        }
    
    #configuring constants in sql statment
    #fields to grab
    A='A.Date, A."Index" as "MarketID",  A.Instrument, A."Start Date", A."End Date", A."% Days Traded", A."Data Points", A.Alpha, A.Beta, A."SE Alpha", A."SE Beta", A."p-Value Alpha", A."p-Value Beta", A.R2, A."Total Risk", A."Unique Risk"'
    case1= 'WHEN B."Index New"=\'LRGC\' THEN \'L\''
    case2= 'WHEN B."Index New"=\'MIDC\' THEN \'M\''
    case3= 'WHEN B."Index New"=\'SMLC\' THEN \'S\''
    case4= 'WHEN B."ALTI New"=\'FLED\' THEN \'F\''
    case5= 'WHEN B."ALTI New"=\'ALTI\' THEN \'A\''
    B='CASE '+ case1+' '+ case2+' '+case3+' '+case4+' '+case5+' ELSE \'\' END as \'Cap\''
    C='C.Industry, C."Super Sector", C.Sector, C."Sub-Sector"'
    fields=A+', '+B+', '+C
    #order statement
    order='ORDER BY Industry, "Super Sector",Sector,"Sub-Sector"'
    
    for y in range(s.year,e.year+1):
        for i in range(0,4,1):
            print("#################QUARTER TEST######################")
            
            start=dt.datetime(y,month[i],1)
            end=dt.datetime(y,(month[i]+1)%12,1) # necessary because case of the 31st and 30th being end of month
            if (start.month==12):
                end=dt.datetime(end.year+1,1,1)
            #Must check date in acceptable range
            if(start<s or start>e):
                continue
            print(start)
            
            #Because Joins are super expensive will reduce the number of joins as much as possible by selecting fewer rows from Index table
            #construct where statement
            
            sql_query=None
            for k in mktC:
                wherestat= 'WHERE A."Index" =\''+k+'\' AND A.Instrument=B.Alpha AND A.Date >= \''+str(s)+'.000\' AND A.Date<\''+str(e)+'.000\' AND B.Date >= \''+str(s)+'.000\' AND B.Date<\''+str(e)+'.000\''
                #construct query
                query='SELECT '+fields+' FROM '+T1 +' AS A,'+T6+' AS B INNER JOIN '+T7+' AS C ON C."Sub-sector Code"=B."ICB Sub-Sector" '+wherestat+' '+order
                #query sql
                if sql_query is None:
                    sql_query = pd.read_sql_query(query,conn)
                else:
                    sql_query = sql_query.append(pd.read_sql_query(query,conn))
            """
            #OG way takes a lot more time
            wherestat= 'WHERE A."Index" in (\'J203\', \'J200\', \'J250\', \'J257\', \'J258\') AND A.Instrument=B.Alpha AND A.Date >= \''+str(s)+'.000\' AND A.Date<\''+str(e)+'.000\' AND B.Date >= \''+str(s)+'.000\' AND B.Date<\''+str(e)+'.000\''
                #construct query
            query='SELECT '+fields+' FROM '+T1 +' AS A,'+T6+' AS B INNER JOIN '+T7+' AS C ON C."Sub-sector Code"=B."ICB Sub-Sector" '+wherestat+' '+order
                #query sql
            sql_query = pd.read_sql_query(query,conn)
            """
            
            #get length of dataframe
            rows_returned=sql_query.shape[0]
            
            #making extra column for year and quarter and adjusting date to reference
            sql_query["Year"]=np.ones(rows_returned)*start.year
            sql_query["Quarter"]=np.ones(rows_returned)*(i+1)
            #sql_query["Date"]=start  #setting date to reference date
            
            #segregate the data by market index
            if (a==1 or m==1):
                for j in mktC:
                    #check whether is first entry in dictionary
                    if (byMarket[j] is None):
                        byMarket[j]=sql_query[sql_query["MarketID"]==j]
                    else:
                        byMarket[j]=byMarket[j].append(sql_query[sql_query["MarketID"]==j])
                
            #makeing each quarter's index entries to file
            if (q==1):
                fname="SY"+str(y)+"Q"+str(i+1)
                Convert2Files(fname, sql_query)
                
    
    #making files by market
    if (m==1):
        for c in mktC:
            tbl=byMarket[c]
            fname='S'+c
            Convert2Files(fname, tbl)
        print("files by market complete")
        
    #full set irrespective with market and date
    if (a==1):
                 
        fname="shareTableView"
        Convert2Files(fname, pd.concat(mktC.values())) 
        print("full fileset complete")     
    
    return byMarket  
"""
################################
# running to generate files    
# q and m flags set to zero so will only generate composite files
"""

"""
#Raw tables
"""
#print(dt.datetime.now())
#allTables()

print(dt.datetime.now())
"""
#For index tables
"""
IndexTables(q=0,m=0)
print(dt.datetime.now())


"""
#For Share tables
"""
ShareTables(q=0,m=0)
print(dt.datetime.now())



#some test code: check conversion of file to an JSarray structure
temp=pd.DataFrame({"testcol":[1,2,3,4],"testcol2":[2,3,4,5], "testcol3":[1,2,3,4]})
#This gets it in js array of objects format
print(type(temp.to_dict('records')))
#just checking: case of going straight to json from pandas
print(temp.to_json())
#transposing the pandas frame
print(temp.T.to_json())

#testing if statement on dictionary
temp={}

if "a" not in temp.keys():
    print("works")

"""
#working for share tables query

#fields to grab
A='A.Date, "Index" as "MarketID",  A.Instrument, A."Start Date", A."End Date", A."% Days Traded", A."Data Points", A.Alpha, A.Beta, A."SE Alpha", A."SE Beta", A."p-Value Alpha", A."p-Value Beta", A.R2, A."Total Risk", A."Unique Risk"'
case1= 'WHEN B."Index New"=\'LRGC\' THEN \'L\''
case2= 'WHEN B."Index New"=\'MIDC\' THEN \'M\''
case3= 'WHEN B."Index New"=\'SMLC\' THEN \'S\''
case4= 'WHEN B."ALTI New"=\'FLED\' THEN \'F\''
case5= 'WHEN B."ALTI New"=\'ALTI\' THEN \'A\''
B='CASE '+ case1+' '+ case2+' '+case3+' '+case4+' '+case5+' ELSE \'\' END as \'Cap\''
C='C.Industry, C."Super Sector", C.Sector, C."Sub-Sector"'
fields=A+', '+B+', '+C
#where statment
wherestat= 'WHERE "Index" = \''+mktC[1]+'\' AND A.Instrument=B.Alpha AND A.Date >= \''+str(s)+'.000\' AND A.Date<\''+str(e)+'.000\' AND B.Date >= \''+str(s)+'.000\' AND B.Date<\''+str(e)+'.000\''
#order statement
order='ORDER BY Industry, "Super Sector",Sector,"Sub-Sector"'
#building query string
query='SELECT '+fields+' FROM '+T1 +' AS A,'+T6+' AS B INNER JOIN '+T7+' AS C ON C."Sub-sector Code"=B."ICB Sub-Sector" '+wherestat

sql_query = pd.read_sql_query(query,conn)
"""