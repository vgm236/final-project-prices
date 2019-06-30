# inflation.py

# FOR IMPORTING DATA
import requests
import json
import csv
import prettytable
import datetime

# FOR API
from dotenv import load_dotenv
import os
import pandas as pd

# FOR CHARTS
import matplotlib.pyplot as plt
import numpy as np


########## ---> TODO: present list of series
########## ---> TODO: selection of the series (more than one as optional)
########## ---> TODO: return error if series do not exist
########## ---> TODO: select beginning and end dates
########## ---> TODO: return error if series do not exist
########## ---> TODO: transform series (original, mom or yoy)
########## ---> TODO: return error if series do not exist
########## ---> TODO: Name axis of charts
########## ---> TODO: Compare series


### USER INPUTS

#Present series available



#Lists selected

download_list = ['CUUR0000SA0'] #TODO:

series_dict = {
    'CUUR0000SA0': 'Inflation'}

dates = ('2000', '2019')  #TODO:

### DATA DOWNLOAD

## Loading the data into the environment

load_dotenv() #loads contents of the .env file into the script's environment
api_key = os.environ.get("BLS_API_KEY") 

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": download_list,"startyear":dates[0], "endyear":dates[1],"catalog":False, "calculations":False, "annualaverage":False, "registrationkey":api_key})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers).json()['Results']['series']


## Importing data into the program (https://www.bd-econ.com/blsapi.html)

# Date index from first series
date_list_unformatted = pd.to_datetime([f"{i['year']}-{i['period'][1:]}-01" for i in p[0]['data']])

date_list = (datetime.datetime.strftime(i, "%m-%Y") for i in date_list_unformatted)

# Empty dataframe to fill with values
df = pd.DataFrame()

# Build a pandas series from the API results, p
for s in p:
    df[series_dict[s['seriesID']]] = pd.Series(
        index = date_list,
        data = [i['value'] for i in s['data']]
        ).astype(float).iloc[::-1]

# Defining and saving file
for series in p:
    seriesId = series['seriesID']
    file_name = seriesId + '.xlsx'
    save_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)

    df.to_dict("records")
    df.values.tolist()
    df.to_excel(save_path)

# Creating a chart
fig, ax = plt.subplots() # enables us to further customize the figure and/or the axesW

ax.xaxis.set_major_locator(plt.MaxNLocator(4)) #editing number of ticks in the axis (https://stackoverflow.com/questions/6682784/reducing-number-of-plot-ticks/6682846#6682846)
   
plt.tight_layout() # ensures all areas of the chart are visible by default (fixes labels getting cut off)

ax.set_xlabel("x label") #TODO:
ax.set_ylabel("y label") #TODO:

df.plot(title='Inflation data', ax=ax) #TODO:

plt.show()

exit()




