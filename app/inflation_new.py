# inflation.py

# FOR IMPORTING DATA
import requests
import json
import csv
import datetime

# FOR API
from dotenv import load_dotenv
import os
import pandas as pd

# FOR CHARTS
import matplotlib.pyplot as plt

## Loading the data into the environment

load_dotenv() #loads contents of the .env file into the script's environment
api_key = os.environ.get("BLS_API_KEY") 

### USER INPUTS

#Present series available
# based on data from BLS: https://download.bls.gov/pub/time.series/cu/cu.item

list_url = "https://download.bls.gov/pub/time.series/cu/cu.item"
r = requests.get(list_url) # create HTTP response object 

#file creation

list_name = 'lists.csv'
list_path = os.path.join(os.path.dirname(__file__), "..", "data", list_name)

with open(list_path,'wb') as f:   
    f.write(r.content) 

data_list = pd.read_csv(list_path, delimiter="\t")

data_list.values.tolist()

#List filtering

code = data_list["item_code"]
name = data_list["item_name"]

#Printing the list
pd.options.display.max_rows = 500 #https://stackoverflow.com/questions/23388810/ipython-notebook-output-cell-is-truncating-contents-of-my-list

fmt = '{:<8}{:<20}{}'

print(fmt.format('', 'Code', 'Name'))  #https://stackoverflow.com/questions/27663924/printing-2-evenly-populated-lists-side-by-side-evenly
for i, (code2, name2) in enumerate(zip(code, name)):
    print(fmt.format(i, code2, name2))

print("---------------------------------------------------------")

print("PLEASE CHOOSE THE CODE OF THE ITEMS IN THE LIST ABOVE")

print("Example: SSHJ031 (for Infants' furniture) ")

print("---------------------------------------------------------")

##Selecting the group

# codes
data_dict = data_list.set_index('item_code').T.to_dict('item_name')

input_code = input("Please input code: ")


try:
    name_series = data_dict["item_name"][f"{input_code}"]
except:
    print("-------------------------------------")
    print("\n")
    print("Non-existent code. Please try again.")
    print("\n")
    print("-------------------------------------")
    exit()

download_list = [f"CUUR0000{input_code}"] 

name_series = data_dict["item_name"][f"{input_code}"]

series_dict = {
    f"CUUR0000{input_code}": name_series} 

########## ---> TODO: selection of the series (more than one as optional)


# dates
init_date = input("Please input initial year (Example: 2000): ")
end_date = input("Please input final year (Example: 2019): ")

dates_list = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

if init_date not in dates_list:
    print("-------------------------------------")
    print("\n")
    print("Non-existent dates. Please try again.")
    print("\n")
    print("-------------------------------------")
    exit()
else:
    pass


dates = (init_date, end_date)  

## Transform series (original, mom or yoy)

list_mom = ["mom", "MoM", "MOM"]
list_yoy = ["yoy", "YoY", "YOY"]
list_df = ["original", "Original", "ORIGINAL"]
transf_list = list_mom + list_yoy + list_df


input_transf = input("Please input transformation (Original, MoM, YoY): ")
if input_transf not in transf_list:
    print("-------------------------------------")
    print("\n")
    print("Unknown transformation. Please try again.")
    print("\n")
    print("-------------------------------------")
    exit()
else:
    pass


### DATA DOWNLOAD TO FILE

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": download_list,"startyear":dates[0], "endyear":dates[1],"catalog":False, "calculations":False, "annualaverage":False, "registrationkey":api_key})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers).json()['Results']['series']


## Importing data into the program (https://www.bd-econ.com/blsapi.html)

# Date index from first series
date_list_unformatted = pd.to_datetime([f"{i['year']}-{i['period'][1:]}-01" for i in p[0]['data']])

date_list = (datetime.datetime.strftime(i, "%m/%d/%Y") for i in date_list_unformatted)

# Empty dataframe to fill with values
df = pd.DataFrame()

# Build a pandas series from the API results, p
for s in p:
    df[series_dict[s['seriesID']]] = pd.Series(
        index = date_list,
        data = [i['value'] for i in s['data']]
        ).astype(float).iloc[::-1]

### SAVING FILE
for series in p:
    seriesId = series['seriesID']
    file_name = seriesId + '.xlsx'
    save_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)

    df.to_dict("records")
    df.values.tolist()
    df.to_excel(save_path)

### TRANSFORMING SERIES

#monthly

monthly_return = df.pct_change(periods=1)*100

#yearly 

yearly_return = df.pct_change(periods=12)*100

### GENERATING CHART
fig, ax = plt.subplots() # enables us to further customize the figure and/or the axesW

ax.xaxis.set_major_locator(plt.MaxNLocator(4)) #editing number of ticks in the axis (https://stackoverflow.com/questions/6682784/reducing-number-of-plot-ticks/6682846#6682846)
   
#plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)

y_label = input_transf

ax.set_xlabel("Dates")
ax.set_ylabel(y_label) 

# Choosing the correct series

if input_transf in list_df:
    df.plot(title=name_series, ax=ax)
    plt.show()
else:
    if input_transf in list_mom:
        monthly_return.plot(title=name_series, ax=ax)
        plt.axhline(y=0.0, color='black', linestyle='-')
        plt.show()
    else:
        yearly_return.plot(title=name_series, ax=ax)
        plt.axhline(y=0.0, color='black', linestyle='-')
        plt.show()

exit()
