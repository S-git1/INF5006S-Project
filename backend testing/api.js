
const dboperations=require('./dboperations');

var express =require('express');
var bodyParser = require('body-parser');
var cors=require('cors'); //seems like redundancy
var app=express();
var router=express.Router();

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(cors());
app.use('/api', router);

//middleware
// called first in case of any authentication requirements
router.use((request,response,next)=>{
    console.log('middleware');
    next();
})

//get only no response input expected
//notice this is all get requests
router.route('/orders').get((_request,response)=>{
    dboperations.getOrders().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//expects an input from the request
//again this is a get request
//access the request parameters via request.params
router.route('/orders/:id').get((_request,response)=>{
    dboperations.getOrder(_request.params.id).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//Getting generated tables as defined in spec
router.route('/breakdown').get((_request,response)=>{
    dboperations.getallBreakdowns().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//Returns set of breakdown data associated with a certain quarter and year
//For particular mkt and base index
router.route('/breakdown/:iC/:mktIC/:y/:q').get((_request,response)=>{
    dboperations.getSpecBreakdown4Q(_request.params.iC,_request.params.mktIC,_request.params.y,_request.params.q).then(result=>{
        console.log(result);
        response.json(result[0]);
    })
})


//Returns set of breakdown data for particular mkt and base index
//for all quarters
router.route('/breakdown/:iC/:mktIC').get((_request,response)=>{
    dboperations.getSpecBreakdown(_request.params.iC,_request.params.mktIC).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})


//getting sharetables shown in examples
router.route('/Sharetable').get((_request,response)=>{
    dboperations.getshareTableView().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/Sharetable/:mktID/:Y/:Q').get((_request,response)=>{
    dboperations.getShareTablebyMktYandQ(_request.params.mktID,_request.params.Y,_request.params.D).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//getting index tables shown in examples
router.route('/Indextable').get((_request,response)=>{
    dboperations.getindexTableView().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/Indextable/:mktID/:Y/:Q').get((_request,response)=>{
    dboperations.getIndexTablebyMktYandQ(_request.params.mktID,_request.params.Y,_request.params.Q).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/BABeta').get((_request,response)=>{
    dboperations.getBAbetaOutput().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/beta').get((_request,response)=>{
    dboperations.getbetaOutput().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/EODeqData').get((_request,response)=>{
    dboperations.getEODEquityData().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/EODeqData/:id').get((_request,response)=>{
    dboperations.getEODEquity(_request.params.id).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})


router.route('/EODinRate').get((_request,response)=>{
    dboperations.getEODinterestRate().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/FtseJse').get((_request,response)=>{
    dboperations.getFTSEJSEIndexSeries().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/FtseJseIndexTypes').get((_request,response)=>{
    dboperations.getIndexTypes().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/IC').get((_request,response)=>{
    dboperations.getindexConstituents().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})
//returns list of tickers in the EOD table
router.route('/Names').get((_request,response)=>{
    dboperations.getAll().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//Returns single name associated with the ticker
//Requires checking for Index types
router.route('/Names/:id').get((_request,response)=>{
    dboperations.getNmByTk(_request.params.id).then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

router.route('/ICB').get((_request,response)=>{
    dboperations.getICB().then(result=>{
        //console.log(result);
        response.json(result[0]);
    })
})

//mote https://www.youtube.com/watch?v=Uvy_BlgwfLI specifies how to use a post request to get data from the user and mess with it in sql
//consider from 34 minutes onwards
//https://www.youtube.com/watch?v=l8WPWK9mS5M specifies a post as well checking 

//configure the port and listener
var port =process.env.PORT || 8090;
app.listen(port, () => console.log(`Order API is running at port: http://localhost:${port}`));

/*
//checking db operations return appropriate data
dboperations.getOrders().then(result=>{
    console.log(result);
})

//by modifying route eg: /api/orders/1 you get the first entry with id =1
dboperations.getOrder(1).then(result=>{
    console.log(result);
})
*/