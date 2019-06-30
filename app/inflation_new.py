# inflation.py

# FOR IMPORTING DATA
import requests
import json
import csv
import prettytable

# FOR API
from dotenv import load_dotenv
import os
import pandas as pd

#Lists selected

download_list = ['CUUR0000SA0']

### INPUTS (get data)

## Loading the data into the environment

load_dotenv() #loads contents of the .env file into the script's environment
api_key = os.environ.get("BLS_API_KEY") 

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": download_list,"startyear":"2000", "endyear":"2019","catalog":False, "calculations":False, "annualaverage":False, "registrationkey":api_key})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)


## Defining file
for series in json_data['Results']['series']:    
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    file_name = seriesId + '.txt'
    save_path = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    output = open(save_path,'w')
    output.write (x.get_string())
    output.close()

imported_data = pd.read_fwf(save_path)


exit()


#Create chart

