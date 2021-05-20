# -*- coding: utf-8 -*-
"""
Initial template for sql from Data to Fish:
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
How to use datetime:
https://www.w3schools.com/python/python_datetime.asp

NB: Change Server to local server name!
    Need to install pyodbc which allows connection to SQL server
    
NB: SQL queries structure requires '' to be escaped and surrounding values that are not numbers or text to be searched
    Case: column name has a space in it, required to use double quotations, EG: "Gross Market Capitalisation", escape not needed provided it is different from the quotation marks
    Escape using prefix of backslash \
"""

import pyodbc
import pandas as pd
import numpy as np
import datetime as dt

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
"""
#Code for testing sql queries
x = dt.datetime(2017, 9, 18)
#sql to pandas, a test query
sql_query=pd.read_sql_query('SELECT Date, Alpha, "Gross Market Capitalisation" as GMC FROM AIFMRM_ERS.'+T6+' WHERE Date=\''+str(x)+'.000\' AND ("ALSI New" =\'ALSI\')',conn)
print(sql_query)
"""

#makes pandas dataframe into .csv file and also prints the data headers (bit redundant)
def MakeCsv(filename,df):
    df.to_csv(filename+".csv")
    print("The following columns were saved to"+filename+".csv:")
    print(df.columns.values)

#Table names; note change to more appropriate variable names later
T1='dbo.tbl_BA_Beta_Output'
T2='dbo.tbl_Beta_Output'
T3='dbo.tbl_EOD_Equity_Data'
T4='dbo.tbl_EOD_Interest_Rate_Data'
T5='dbo.tbl_FTSEJSE_Index_Series'
T6='dbo.tbl_Index_Constituents'
T7='dbo.tbl_Industry_Classification_Benchmark'

#Dictionary of memberships to indices
#makes it easier to check whether membership exists or not for error handling
cNMS = {
  "ALSI": "ALSI New",
  "FLED": "ALSI New",
  "LRGC": "Index New",
  "MIDC": "Index New",
  "SMLC": "Index New",
  "TOPI": "TOPI New",
  "RESI": "RESI New",
  "FINI": "FINI New",
  "INDI": "INDI New",
  "PCAP": "PCAP New",
  "SAPY": "SAPY New",
  "ALTI": "ALTI New"
}

#again for error checking
mktC = ["J203", "J200", "J250", "J257", "J258"]


#rDate is a datetime object, datetime library has been imported to support this
#dbo.tbl_Index_Constituents required to be used as table insert
#I've made it a fixed variable to avoid syntax mistakes, call T6
#Function returns pandas dataframe containing column of index constituents and corresponding weight in index by gross market cap
def GetICsAndWeights(table, rDate, indexCode):
    try:
        cNm = cNMS[indexCode]
        assert table == 'dbo.tbl_Index_Constituents'
        sql_query = pd.read_sql_query('SELECT Alpha, "Gross Market Capitalisation" as Weight FROM AIFMRM_ERS.'+T6+' WHERE Date=\''+str(x)+'.000\' AND ("'+cNm+'"=\''+indexCode+'\')',conn)
        sql_query['Weight']=sql_query['Weight']/sum(sql_query['Weight'])
        return sql_query
    except KeyError as e:
        print("error: please enter a indexCode that is in the database")
        print(e)
        return 0
    except AssertionError as e:
        print("error: incorrect table field")
        print(e)


#dbo.tbl BA Beta Output
#Assume that ICs is passed in as a pandas dataframe or list type
#If pandas type, will be converted within function into list type anyways
def GetBetasMktAndSpecVols(table, rDate, ICs, mktIndexCode):
    try:
        assert mktIndexCode in mktC
        sql_query = pd.read_sql_query('SELECT Instrument, Beta, "Unique Risk" as specVols, "Total Risk" as mktVol FROM AIFMRM_ERS.'+table+' WHERE Date=\''+str(rDate)+'.000\' AND Instrument IN ('+str(list(ICs))[1:-1]+') AND "Index"=\''+mktIndexCode+'\'' ,conn)
        return sql_query
    except AssertionError as e:
        print("Market code not in database")
        print(e)
    except:
        print("ohno, ohno, oh no no no no")


#first convert everything to numpy arrays
#direct call to numpy array constructor to make either pandas or list or numpy data structures into array
#calling constructor on numpy array makes a copy it seems (will need to look at whether numpy has copy constructor)
#weights,betas,specvols all column vectors
#mktVols is a scalar
#Q: is total asset volatility, totcov?
def CalcStats(weights, betas, mktVol,specVols):
    w = np.array(weights)
    b = np.array(betas)
    m = mktVol
    s = np.array(specVols)
    
    pfBeta = w.T@b #Portfolio Beta
    sysCov = (b@b.T)*(m**2) #Systematic Covariance Matrix
    pfSysVol = (w.T@b)*(b.T@w)*(m**2) #Portfolio Systematic Variance
    specCov = np.diag(s)**2 #Specific Covariance Matrix
    pfSpecVol = w.T@specCov@w #Portfolio Specific volatility
    totCov = sysCov + specCov #total covariance matrix
    pfVol = pfSysVol + pfSpecVol #portfolio total volatility
    
    D_ = np.linalg.inv(np.diag(np.diag(totCov)))
    corrMat = D_@[totCov]@D_ #correlation matrix
    
    allStats={
        "pfBeta":pfBeta,
        "sysCov":sysCov,
        "pfSysVol":pfSysVol,
        "specCov":specCov,
        "pfSpecVol":pfSpecVol,
        "totCov":totCov,
        "pfVol":pfVol,
        "corrMat":corrMat
        }
    return allStats
 

# running some tests   
x = dt.datetime(2017, 9, 18)
funstuff = GetICsAndWeights(T6, x, "FLED")
print(funstuff)

x = dt.datetime(2017,9,29)
Mofun = GetBetasMktAndSpecVols(T1, x, funstuff['Alpha'], "J203")
print(Mofun)

lastfun = CalcStats(funstuff['Weight'], Mofun['Beta'], 1, Mofun['specVols'])    
print(lastfun)