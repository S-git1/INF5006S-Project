var config = require('./dbconfig');
const sql=require('mssql');

//async and await is for promised based
async function getOrders(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.post");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}


async function getOrder(orderID){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
            .input('input_parameter',sql.Int,orderID)
            .query("SELECT * from dbo.post where Id=@input_parameter");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block 2");
    }
}

async function getallBreakdowns(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.allBreakdownsview1");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

async function getSpecBreakdown4Q(mktIC, IC, Year, Q){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
            .input('year',sql.NVarChar,Year)
            .input('quarter', sql.NVarChar, Q)
            .input('mkt', sql.NVarChar,mktIC)
            .input('IC', sql.NVarChar,IC)
            .query("SELECT * from dbo.allBreakdownsview1 where Year=@year and Quarter=@quarter and IC=@IC and MktIC=@mkt");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block 2");
    }
}

async function getSpecBreakdown(mktIC, IC){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
            .input('mkt', sql.NVarChar,mktIC)
            .input('IC', sql.NVarChar,IC)
            .query("SELECT * from dbo.allBreakdownsview1 where IC=@IC and MktIC=@mkt");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block 2");
    }
}

async function getindexTableView(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.indexTableView");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

async function getIndexTablebyMktYandQ(mktIC,Y,Q){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
        .input('mkt', sql.NVarChar,mktIC)
        .input('Y', sql.NVarChar,Y)
        .input('Q', sql.NVarChar,Q)
        .query("SELECT * from dbo.indexTableView WHERE MarketID=@mkt and Year=@Y and Quarter=@Q");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

async function getshareTableView(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.shareTableView");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}
async function getShareTablebyMktYandQ(mktIC,Y,Q){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
        .input('mkt', sql.NVarChar,mktIC)
        .input('Y', sql.NVarChar,Y)
        .input('Q', sql.NVarChar,Q)
        .query("SELECT * from dbo.shareTableView WHERE MarketID=@mkt and Year=@Y and Quarter=@Q");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}
//BA beta output
async function getBAbetaOutput(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_BA_Beta_Output");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

// beta output
async function getbetaOutput(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_Beta_Output");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

// EOD equity data
async function getEODEquityData(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_EOD_Equity_Data");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

//get equity data by instrument
async function getEODEquity(Instrument){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request()
            .input('input_parameter',sql.VarChar,Instrument)
            .query("SELECT * from dbo.tbl_EOD_Equity_Data where Instrument=@input_parameter");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block 2");
    }
}

// EOD interest rate data
async function getEODinterestRate(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_EOD_Interest_Rate_Data");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

//ftsejse index series
async function getFTSEJSEIndexSeries(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_FTSEJSE_Index_Series");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

async function getIndexTypes(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT Distinct([Index Type]) as IT from dbo.tbl_FTSEJSE_Index_Series");
        var size= 0;
        for (key in products.recordsets[0]){
          //console.log(size);
          products.recordsets[0][size]["id"]=size+1;
          console.log(products.recordsets[0][size]);
          size++;
        }
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

//get index constituents
async function getindexConstituents(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_Index_Constituents");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

//get all available ticker data on  of stocks and index constituents
async function getavailableTickers(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT DISTINCT Instrument FROM dbo.tbl_EOD_Equity_Data");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}

//get instrument name ny ticker
// need to check that this isn't an index type which would return null
async function getNmByTk(ticker){
    try{
        if (ticker.length==4){
            return [[{"Name": "Index"}]];
        }
        let pool=await sql.connect(config);
        let products = await pool.request()
            .input('input_parameter',sql.NVarChar,ticker)
            .query("SELECT Top 1 Instrument as Name from dbo.tbl_Index_Constituents where Alpha=@input_parameter Order by Instrument ASC");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block 2");
    }
}


//industry classification benchmark
async function getICB(){
    try{
        let pool=await sql.connect(config);
        let products = await pool.request().query("SELECT * from dbo.tbl_Industry_Classification_Benchmark");
        return products.recordsets;
    }
    catch (error){
        console.log(error);
        console.log("something went wrong in this block");
    }
}


module.exports={
    getOrders : getOrders,
    getOrder : getOrder,
    getallBreakdowns : getallBreakdowns,
    getindexTableView : getindexTableView,
    getshareTableView : getshareTableView,
    getBAbetaOutput : getBAbetaOutput,
    getbetaOutput : getbetaOutput,
    getEODEquityData : getEODEquityData,
    getEODinterestRate : getEODinterestRate,
    getFTSEJSEIndexSeries : getFTSEJSEIndexSeries,
    getIndexTypes : getIndexTypes,
    getindexConstituents : getindexConstituents,
    getICB : getICB,
    getEODEquity : getEODEquity,
    getAll : getavailableTickers,
    getNmByTk : getNmByTk,
    getSpecBreakdown : getSpecBreakdown,
    getSpecBreakdown4Q : getSpecBreakdown4Q,
    getShareTablebyMktYandQ : getShareTablebyMktYandQ,
    getIndexTablebyMktYandQ : getIndexTablebyMktYandQ
}