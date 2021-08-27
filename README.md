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

**npm install express mssql tedious body-parser cors --save**


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

Now you will need to install dependencies

**npm install zingchart**
**npm install vuetable-2@next --save**
**npm install --save @riophae/vue-treeselect**
**npm install vue-slide-bar --save**
**npm install nodemon**

Install node demon and spec/insert new script in package.json:

**"start": "nodemon api.js"**

Next, manually copy and replace the src and public folders in the Vue app with those on the git repo under Vue-app

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
            |---{see other 6 html files}
            |---assets
            |---favicon.ico

    |---src

      |---assets

      |---components

            |---extra
            
            |---LatestTransactionsChart.vue

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

# Bug report and Improvements
- Investigate the efficiencies of map vs filter vs arrays
- Configure a better backend for accessing reduced set of data.
- Possibly exploring stored procedures.
- Better app Structure, Access dataService directly from components to improve speed of rendering. Consider the use of v-show of v-if and performance
- Fix bug preventing double multifilters (YQ set and index codes set) on share and index chart data. Currently results in endless loop. Moving multifilter for codes into App.vue rather than in component may help reduce filtering complexity and also enable filter to persist through tab changing.
- Fix bug in share charts multiselect, seems to be referncing wrong value when constructing
