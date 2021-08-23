const config = {
    user: 'testing',
    password: '1234',
    server: 'DESKTOP-Q0H6UCN', // changed to whatever your server name is
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
//1. must configure sql server authentication on (M)SSMS: connect via windows authentication, 
//      on left tab (Object Explorer): right click on server (ususally named somthing like DESKTOP-XXXXXX), then click on 'properties'
//      on window left pane (Select a page), select 'Security', then under 'Server authentication', select 'SQL Server and Windows Authentication mode'
//      click 'OK' to confirm settings and exit window.

//      on left tab (Object Explorer): security->login->rightclick to make new login
//      set login type to SQL server authentication, enter Login name and Password 
//      untick enforce password exploration
//      Set default database set to AIFMRM_ERS
//      on window left pane (Select a page), select Server Roles and tick sysadmin, apply
//      on window left pane (Select a page), select Status and enable both access and login credentials
//2. Condigure TCP/IP port
//      open SQL server configurations manager (or SQL Server Network Configuration)
//      on left pane, select sql server configurations -> protocols for sqlexpress (or TEW_SQLEXPRESS)
//      for TCP/IP rightclick and select properties, in first tab 'Protocol' ensure it is enabled, in 'IP Addresses' set TCP port number for IPALL to 1433 
//3. restart services: open services interface (windows start menu-> services ) and restart SQL Server(some instanc name) + SQL Server Browser. Make sure startup on both is automatic.
