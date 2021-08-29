Dear Reader

These are 3 bugs that may occur during the installation. The dashboard requires these fixes to work exactly as it did in the demo.

## 1 Python scripts

Configuration instructions and detailed docs are in the python scripts. Please read through to generate any required data or just run for default data
An issue that can occur is a 'folder not found error'

### To fix

The script assumes there is a folder named 'data' with subfolders 'csv' and 'js'. The data folder needs to be in the same directory as the python files.
![image](https://user-images.githubusercontent.com/80747408/131233498-3765fcb2-0257-4b84-b37d-ba2c63167263.png)
*expected folders by script*

## 2 Loading the .csv data into the SQL server correctly

After the restoration of the AIFFRM database to SSMS, flat files .csv files 'allBreakdownsview1.csv', 'shareTableView.csv', 'indexTableView.csv' in data/csv folder need to be imported as flat files into existing server. The import process may change the data columns imported depending on your SSMS settings. 

### To fix

During import
- Data types can be varchar or numerical for values, we were careful in the front-end to be robust by type-casting. 
- Null types need to be allowed for all files during import
- after importing flat files, ensure that the names of the columns for each imported match the below images:
![image](https://user-images.githubusercontent.com/80747408/131234168-51f889dd-a907-4925-91cd-50a770604002.png)
*dbo.allBreakdwonsview1* table

![image](https://user-images.githubusercontent.com/80747408/131234181-420db8f2-c559-481f-8362-29f9b4ffc06c.png)
*dbo.indexTableView* table

![image](https://user-images.githubusercontent.com/80747408/131234201-659c119c-c6ce-46fb-ac84-8f218e35e9bf.png)
*dbo.shareTableView* table


## 3 Bug that was introduced during the last App.vue commit for the breakdown charts

A line of code was commented during the last commit resulting in the breakdown charts not updating when changing the Index type in the breakdown set of charts. The charts will only update to the correct index breakdown set once you change the market proxy or the type of statistic 

### To fix

Uncomment line 875 in App.vue.

![image](https://user-images.githubusercontent.com/80747408/131232759-63c17318-b1d0-4b67-82d7-32851e51289f.png)
*App.vue currently*
