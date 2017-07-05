
'''This is just a basic python console app that uses the request module of query the site in the url and generate
json which is printed on the console.It also generates a txt and csv file for the generated json and saves them as
two files'''

import requests
import csv
import json

response = requests.get('https://www.metaweather.com/api/location/44418/2013/4/27/')
json_data_received=response.json()
# print(json_data_received)
#print(json_data_received)
csv_str = "Maximum_temperature\t, Visibility\t,the_temp\t,applicable_date\t \n"
for x in json_data_received:
    csv_str += "{},    {},   {},    {}".format(x['max_temp'], x['visibility'],x['the_temp'],x['applicable_date'])
    csv_str += "\n"
    print(csv_str)
    exit()

with open('output.txt', 'w') as text_file:
    text_file.write(str(json_data_received))

output=r'output.txt'
csv_file=r'mycsv.csv'
in_txt = csv.reader(open(output, "r"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'w'))
