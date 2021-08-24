# INF5006S-Project
Code for the INF5006S dashboard project


# Installation Instructions

## 1 Backend initialization

In the root folder, run the following code and dependencies to set up environment. Require installation of node js. For example, use the script:

**npm init backend**

Initiates node modules and name the project backend (or some variation) once the project name is asked for in the initializing step, and use the following inputs to the questions asked in the shell:

**? What's your project name ? (This will be the project folder) backend**

**? Would you like to use Aliases? Yes**

**? Should we include a User endpoint example? No**

**? Which database engine would you like to use? MSSQL**

**? Would you like to use Typescript? No**

**? Which license would you like to use? UNLICENSED**

Then install the express MSSQL component in the project folder you just created:

**cd backend**

**npm install express mssql tedious body-parser cors vue-multiselect --save**
**npm install vuetable-2@next --save**

Installed dependencies after npm init. Not sure if we require tedious for ms server, and mssql library required for sake of access. body-parser for use of json and cors for api communication accross different sources and express for something I can't remember. write out a proper explanation

**npm install nodemon**

Install node demon and spec/insert new script in package.json:

**"start": "nodemon api.js"**

Nodemon automatically refreshes the build each there is a change in the file. For ease of testing sake. it's annoying to start and restart build each time there is an issue.

## 2 Frontend initialization

In the root folder, create a vue project called frontend using zinggrid. To do so, run the following command:

**vue create --preset zingsoftinc/vue-dashboard#starter frontend**

Stop after installation complete.

Now add the router component to the vue project using:

**vue add router**

Then for the history mode choose "No": (I don't know what this is so I just chose "No")

**? Use history mode for router? (Requires proper server setup for index fallback in production) No**

Next, manually create a folder with name "services" inside frontent/src:

**cd src**

**md services**

## 3 Copy in source files

Backend files will be found in Backend Testing folder and front end in Vue-app folder. Copy in files in the following structure:

    **'backend'**

    |---node_modules

    |---api.js

    |---dbconfig.js

    |---dboperations.js    

    |---package-lock.json

    |---package.json



    **'Frontend'**

    |---node_modules

    |---public

            |---index.html

    |---src

      |---assets

      |---components

            |---allBreakdownsView.vue

            |---indexTableView.vue

            |---shareTableView.vue
            
            |---shareTabAlt.vue
            
            |---LatestTransactionsChart.vue

            |---IndexTabAlt.vue

            |---TabAlt2.vue

       |---router

       |---services

            |---DataService.js

       |---views
       
       |---App.vue
       
       |---http-common.js
       
       |---main.js


## 4 Edit the dbconfig.js

Required to edit the file to local specifications, follow instructions to setup mssql server and ports in dbconfig.js file

# Notes

This backend only processes get requests, as we don't expect changes to the data

# Improvements
Looking to setup visualisations and configure a better backend for accessing reduced set of data.
Possibly exploring stored procedures
