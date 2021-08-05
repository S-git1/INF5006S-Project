import http from "../http-common";

//class that provides api routes
//requires wrapping within async await call
class TutorialDataService{

    gettest(){
        return http.get(`/orders`);
    }

    getbreakdown(){
        return http.get(`/breakdown`);
    }

    getSpecBreakdown4Q(IC, mktIC, y, q){
        return http.get(`/breakdown/${mktIC}/${IC}/${y}/${q}`);
    }

    getSpecBreakdown(IC,mktIC){
        return http.get(`/breakdown/${mktIC}/${IC}`);
    }

    getSharetable(){
        return http.get(`/Sharetable`);
    }

    getSharetableByMKT_YQ(mktIC,Y,Q){
        return http.get(`/Sharetable/${mktIC}/${Y}/${Q}`);
    }


    getIndextable(){
        return http.get(`/Indextable`);
    }

    getIndextableByMKT_YQ(mktIC,Y,Q){
        return http.get(`/Indextable/${mktIC}/${Y}/${Q}`);
    }

    getBABetaOutput(){
        return http.get(`/BABeta`);
    }

    getbetaOutput(){
        return http.get(`/beta`);
    }
    
    getEODEquityData(){
        return http.get(`/EODeqData`);
    }

    getEODEquity(Instrument){
        return http.get(`/EODeqData/${Instrument}`);
    }

    getEODinterestRate(){
        return http.get(`/EODinRate`);
    }

    getFTSEIndexSeries(){
        return http.get(`/FtseJse`);
    }

    getindexConstituents(){
        return http.get(`/IC`);
    }

    getavailableTickers(){
        return http.get(`/Names`);
    }

    getNmByTk(ticker){
        return http.get(`/Names/${ticker}`);
    }

    getICB(){
        return http.get(`/ICB`);
    }


    
}

export default new TutorialDataService();