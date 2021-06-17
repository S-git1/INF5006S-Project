# -*- coding: utf-8 -*-
"""
Initial template for sql from Data to Fish:
https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
How to use datetime:
https://www.w3schools.com/python/python_datetime.asp
How to make sql inserts faster
https://towardsdatascience.com/how-i-made-inserts-into-sql-server-100x-faster-with-pyodbc-5a0b5afdba5
df['measurement'] = [format(i, '.3f') for i in df['measurement']]

NB: Change Server to local server name!
    Need to install pyodbc which allows connection to SQL server
    
NB: SQL queries structure requires '' to be escaped and surrounding values that are not numbers to be searched
    Case: column name has a space in it, required to use double quotations, EG: "Gross Market Capitalisation", escape not needed provided it is different from the quotation marks
    Escape using prefix of backslash \
"""

import pyodbc
import pandas as pd
import numpy as np
import datetime as dt
import json
import sqlalchemy

#turn off false positive from pandas
pd.options.mode.chained_assignment = None  # default='warn'

#make pandas show all on print
pd.set_option('display.max_columns', None)

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

#gives json.dump a default function if it encounters some unknown type
def dtConvert(o):
    if isinstance(o, dt.datetime):
        return "{}-{}-{}".format(o.year, o.month, o.day)
  

#makes pandas dataframe into .csv and .js file and also prints the data headers
#Note: there is also a way to convert straight from pandas to json filetype but format not guaranteed as jsarray
#Currently csv version disabled otherwise takes script too long to run
#Note: when running script make sure to already have data/csv and data/js subdirectories in the folder the script is running
def Convert2Files(filename,df):
    df.to_csv("./data/csv/"+filename+".csv") #.csv
    #df.to_json(filename+".csv") #Json
    with open("./data/js/"+filename+".js", "w") as fp:  
        json.dump(df.to_dict("records"), fp, default=dtConvert) #.js
        
    print("\nThe following columns were saved to"+filename+".csv and jsarrays in .js:")
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

#There are only 10 distinct industries
indus = [
    "Basic Materials",
    "Consumer Goods",
    "Consumer Services",
    "Financials",
    "Health Care",
    "Industrials",
    "Oil & Gas",
    "Technology",
    "Telecommunications",
    "Utilities"
    ]
    
    
#again for error checking
mktC = ["J203", "J200", "J250", "J257", "J258"]
month=[3,6,9,12]
year=[2017,2021]

#set boundary dates for function default
boundary1=dt.datetime(2017,9,1) #sql database boundary for first date
boundary2=dt.datetime(2021,3,1) 

#rDate is a datetime object, datetime library has been imported to support this
#dbo.tbl_Index_Constituents required to be used as table insert
#I've made it a fixed variable to avoid syntax mistakes, call T6
#Function returns pandas dataframe containing column of index constituents and corresponding weight in index by gross market cap
def GetICsAndWeights(table, rDate, indexCode):
    try:
        cNm = cNMS[indexCode]
        assert table == 'dbo.tbl_Index_Constituents'
        assert rDate.month in month
        
        start = dt.datetime(rDate.year, rDate.month, 1)
        end = dt.datetime(rDate.year,(rDate.month+1)%12,1)
        if (rDate.month==12):
            end=dt.datetime(rDate.year+1,1,1)
        
        sql_query = pd.read_sql_query('SELECT Alpha, "Gross Market Capitalisation" as Weight, "ICB Sub-Sector", Industry, "Super Sector", Sector, "Sub-Sector" FROM AIFMRM_ERS.'+T7+', AIFMRM_ERS.'+T6+' WHERE Date>\''+str(start)+'.000\' AND Date<\''+str(end)+'.000\' AND ("'+cNm+'"=\''+indexCode+'\') AND AIFMRM_ERS.'+T6+'."ICB Sub-Sector"=AIFMRM_ERS.'+T7+'."Sub-Sector Code" ORDER BY Alpha',conn)
        #temp=sum(sql_query['Weight'])
        #print(temp)
        #sql_query['Weight']=sql_query['Weight']/temp
        return sql_query
    except KeyError as e:
        print("error: please enter a indexCode that is in the database")
        print(e)
        return 0
    except AssertionError as e:
        print("error: incorrect table field or month does not exist") #how do you handle multiple errors?
        print(e)


#dbo.tbl BA Beta Output
#Assume that ICs is passed in as a pandas dataframe or list type
#If pandas type, will be converted within function into list type anyways
def GetBetasMktAndSpecVols(table, rDate, ICs, mktIndexCode):
    try:
        start = dt.datetime(rDate.year, rDate.month, 1)
        
        end = dt.datetime(rDate.year,(rDate.month+1)%12,1)
        if (rDate.month==12):
            end=dt.datetime(rDate.year+1,1,1)
        
        assert mktIndexCode in mktC
        sql_query = pd.read_sql_query('SELECT Instrument, Beta, "Unique Risk" as specVols FROM AIFMRM_ERS.'+table+' WHERE Date>\''+str(start)+'.000\' AND Date<\''+str(end)+'.000\' AND Instrument IN ('+str(list(ICs))[1:-1]+') AND "Index"=\''+mktIndexCode+'\' ORDER BY Instrument' ,conn)
        mktVol = pd.read_sql_query('SELECT DISTINCT "Total Risk" FROM AIFMRM_ERS.'+table+' WHERE Date>\''+str(start)+'.000\' AND Date<\''+str(end)+'.000\' AND Instrument=\''+ mktIndexCode +'\'' ,conn).values[0][0]
        return sql_query, mktVol
    except AssertionError as e:
        print("Market code not in database")
        print(e)
    except:
        print("ohno, ohno, oh no no no no")
        print("the table, date or lists of index constituents is not in the correct form, please try again")




#all values entered except mktVol (require scalar) can be a list or numpy array or pandas dataframe
#the first convert everything to numpy arrays
#direct call to numpy array constructor to make either pandas or list or numpy data structures into array
#calling constructor on numpy array makes a copy it seems (will need to look at whether numpy has copy constructor)
#weights,betas,specvols all column vectors
#mktVols is a scalar
#returns all statistics in a dictionary of numpy arrays
def CalcStats(weights, betas, mktVol,specVols):
    try:
        assert (len(weights)==len(betas) & len(weights)==len(specVols))
        w = np.array(weights).reshape(len(weights),1)
        b = np.array(betas).reshape(len(betas),1)
        m = mktVol
        s = np.array(specVols)
        pfBeta = w.T@b #Portfolio Beta
        sysCov = (b@b.T)*(m**2) #Systematic Covariance Matrix
        pfSysVol = (w.T@b@b.T@w)*(m**2) #Portfolio Systematic Variance
        specCov = np.diag(s)**2 #Specific Covariance Matrix
        pfSpecVol = w.T@specCov@w #Portfolio Specific volatility
        totCov = sysCov + specCov #total covariance matrix
        pfVol = pfSysVol + pfSpecVol #portfolio total volatility
        
        b=np.diag(totCov)**0.5
        a=np.ones(len(b))
        D_ = np.diag(np.divide(a , b, out=np.zeros_like(a), where=b!=0))
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
    except AssertionError:
        print("length of list/matrix type inputs do not match up.")
        print(len(weights))
        print(len(betas))
        print(len(specVols))
        print(len(weights)==len(betas) & len(weights)==len(specVols))


def Synthetic(start=boundary1, end=boundary2, indexCode="TOPI", mktIndexCode="J203"):
    n=0
    byQuarter={}
    #print(pd.DataFrame({'Industry': pd.Series(indus)}))
    breakdown={ 'weight': pd.DataFrame({'Industry': pd.Series(indus)}),
                'beta': pd.DataFrame({'Industry': pd.Series(indus)}),
                'sysVol': pd.DataFrame({'Industry': pd.Series(indus)}),
                'specVar': pd.DataFrame({'Industry': pd.Series(indus)})
        }
    #print(breakdown["weight"])
    All=None
    
    for y in range(start.year,end.year+1):
        for i in range(0,4,1):
            #print("#################QUARTER TEST######################")
            pot=dt.datetime(y,month[i],1)
            #Must check pot in acceptable range
            if(pot<start or pot>end):
                continue
            print(pot) #show the quarter ref date
            n=n+1 
            print("Quarter ",n) #counter for number of quarters
            A = GetICsAndWeights(T6, pot, indexCode)
            B,C = GetBetasMktAndSpecVols(T1, pot, A['Alpha'], mktIndexCode)
            
            #Cleaning the data, if there is missing betas or missing market cap
            #Cleaning for prep to CalcStats
            is_Nan1 = A.isnull().any(axis=1)
            is_Nan2 = B.isnull().any(axis=1)
            Cleaned=~(is_Nan1|is_Nan2)
            A=A[Cleaned]
            B=B[Cleaned]
            
            #Checking for null values again
            is_Nan1 = A.isnull().any(axis=1)
            is_Nan2 = B.isnull().any(axis=1)
            #print(sum((is_Nan1|is_Nan2))) #should show zero if no Nans
            
            #constructing bespoke breakdown
            bespoke=A[['Industry','Weight']] #copy A - I want to preserve the original for returning the quarter output
            
            bespoke[str(n)+'weight']=bespoke['Weight']/sum(bespoke['Weight'])
            bespoke[str(n)+'betas']=bespoke[str(n)+'weight']*B['Beta'] 
            bespoke[str(n)+'sysVol']=bespoke[str(n)+'betas']*C
            bespoke[str(n)+'specVar']=(bespoke[str(n)+'weight']*B['specVols'])**2
            
            #print(bespoke)
            grp=bespoke.groupby('Industry') #groupby function
            sgrp=grp.sum().reset_index()
            sgrp['Year']=np.ones(sgrp.shape[0])*y
            sgrp['Quarter']=np.ones(sgrp.shape[0])*(i+1)
            
            
            #constructing the sythetic index statistics tables directly
            breakdown['weight']=pd.merge(breakdown['weight'], sgrp[['Industry',str(n)+'weight']] , how="left", on=['Industry'])
            breakdown['beta']=pd.merge(breakdown['beta'], sgrp[['Industry',str(n)+'betas']] , how="left", on=['Industry'])
            breakdown['sysVol']=pd.merge(breakdown['sysVol'], sgrp[['Industry',str(n)+'sysVol']] , how="left", on=['Industry'])
            breakdown['specVar']=pd.merge(breakdown['specVar'], sgrp[['Industry',str(n)+'specVar']] , how="left", on=['Industry'])
            
            sgrp.rename(columns={str(n)+'weight':'weight', str(n)+'betas':'betas', str(n)+'sysVol': 'sysVol', str(n)+'specVar': 'specVar'}, inplace=True)
            if (All is None):
                All=sgrp
                #print(0)
            else:
                #print(1)
                All=All.append(sgrp)
            #print(sgrp)
            
            D = CalcStats(A['Weight'], B['Beta'], C, B['specVols'])
            key='Y'+str(y)+'Q'+(str(i+1))
            byQuarter[key]={'A':A,
                            'B':B,
                            'C':C,
                            'D':D
                            }
    for key in breakdown:
        breakdown[key]["IC"]=np.repeat(indexCode, 10)
        breakdown[key]["MktIC"]=np.repeat(mktIndexCode,10)
        breakdown[key]['Metric']=np.repeat(key,10)
    All["IC"]=np.repeat(indexCode, All.shape[0])
    All["MktIC"]=np.repeat(mktIndexCode,All.shape[0])
    return byQuarter, breakdown, All
    

print("###################STARTING TEST##########################")
start=dt.datetime(2017,9,1)
end=dt.datetime(2021,3,1)

everything={}
weight={}
betas={}
sysVol={}
specVar={}
everything2={}
for i in mktC:
    for j in cNMS.keys():
        q, bd, ever=Synthetic(start,end, j, i)
        everything[i+j]=ever
        everything2[i+j]=pd.concat(bd.values(),axis=0, ignore_index=True)
        weight[i+j]=bd['weight']
        betas[i+j]=bd['beta']
        sysVol[i+j]=bd['sysVol']
        specVar[i+j]=bd['specVar']
        


print(dt.datetime.now())
q, bd, ever=Synthetic(start,end, "TOPI", "J203")

print(dt.datetime.now())

print("everything")
Convert2Files("allBreakdownsview1", pd.concat(everything.values()))

print("by quarter and metric")
Convert2Files("weights", pd.concat(weight.values()).replace(np.nan,0))
Convert2Files("betas", pd.concat(betas.values()).replace(np.nan,0))
Convert2Files("sysVol", pd.concat(sysVol.values()).replace(np.nan,0))
Convert2Files("specVar", pd.concat(specVar.values()).replace(np.nan,0))
"""
# running some tests and checking construction of synthetic index  
x = dt.datetime(2017, 12, 18)
funstuff = GetICsAndWeights(T6, x, "TOPI")
print(funstuff)
print(sum(funstuff['Weight']))
Mofun, mktVol = GetBetasMktAndSpecVols(T1, x, funstuff['Alpha'], "J200")
print(Mofun)
print(mktVol)


funstuff['Beta']=Mofun['Beta']
funstuff['SpecVols']=Mofun['specVols']
funstuff['w']=funstuff['Weight']/sum(funstuff['Weight'])
funstuff['wb']=funstuff['w']*funstuff['Beta']
funstuff['ws']=funstuff['w']*funstuff['SpecVols']
funstuff['ws2']=funstuff['ws']**2
funstuff['wbm']=funstuff['wb']*mktVol
#print(funstuff)
grp=funstuff.groupby('Industry')
sgrp=grp.sum()

print(sgrp)
print("beta sum: ",sum(sgrp['wb']))
print("m sum: ",sum(sgrp['ws']))
print("SpecVar sum: ",sum(sgrp['ws2']))
print("sysvol sum: ", sum(sgrp['wbm']))
be=0
sv=0
scv=0
tv=0
for k in funstuff['Industry'].unique():
    smpl=grp.get_group(k)
    stats=CalcStats(smpl['w'], smpl['Beta'], mktVol,smpl['SpecVols'])
    be+=stats['pfBeta'][0][0]
    sv+=stats['pfSysVol'][0][0]**0.5
    scv+=stats['pfSpecVol'][0][0]
    
print(be, sv , scv, tv)
print('mktvol: '+str(mktVol))

lastfun = CalcStats(funstuff['Weight']/sum(funstuff['Weight']), Mofun['Beta'], mktVol, Mofun['specVols']) 

print("pfBeta: ",lastfun['pfBeta'][0][0])
print("pfSysVar: ",lastfun['pfSysVol'][0][0]**0.5)
print("pfSpecVar: ",lastfun['pfSpecVol'][0][0])
print("pfVar: ",lastfun['pfVol'][0][0])

for k in funstuff['Industry'].unique():
    temp=funstuff['Industry']==k
    temp2=funstuff
    temp2['w']

is_NaN = Mofun.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = Mofun[row_has_NaN]
print(Mofun[~row_has_NaN]) 
  
test1=row_has_NaN
test1[4]=True
test2=row_has_NaN
print(test2|test1)
print(sum(test2))
print(Mofun[~test1])

   
#print(lastfun)
for key in lastfun:
    print(key)
    temp=lastfun[key]
    print(temp)
    print(type(temp))
    print(temp.shape)
    print("\n")



testfun=CalcStats(list([1,2,3]),list([1,2,3]),2,list([1,2,3]))

for key in testfun:
    print(key)
    print(testfun[key])
    print('\n')
"""
