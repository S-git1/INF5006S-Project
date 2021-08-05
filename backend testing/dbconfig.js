const config = {
    user: 'testing',
    password: '1234',
    server: 'DESKTOP-Q0H6UCN',
    database: 'AIFMRM_ERS',
    options:{
        trustedconnection: true,
        enableArithPort: true,
        instancename: 'SQLEXPRESS',
        trustServerCertificate: true,
    },
    port : 1433
}

module.exports = config;

//REQUIRED for mssql to access server
//1. must configure sql server authentication on SSMS: connect via windows authentication, 
//      on left tab: security->login->rightclick to make new login
//      set login type to SQL server authentication, enter pass word +login
//      untick enforce password exploration
//      on window left pane, select server roles and tick sysadmin, apply
//      on window left pane, select status and enable both access and login credentials
//2. Condigure tcp/ip port
//      open sql server configurations manager
//      on left pane, select sql server configurations -> protocols for sqlexpress
//      for tcp/ip rightclick and select properties, in first tab protocol ensure it is enabled, in Ipaddress set tco port number for IPALL to 1433 
//3. restart services: open services interface (start-> services ) and restart SQL Server(some instanc name) + SQK Server Browser. Make sure startup on both is automatic.