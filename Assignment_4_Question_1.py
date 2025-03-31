import csv
import datetime
from collections import defaultdict
columns = defaultdict(list) # each value in each column is appended to a list

with open('ApplicationLog.csv','r') as file:

    reader = csv.DictReader(file) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}c
     
        if row.get("Source")=='Universal Print' and row.get("Date and Time") is not None:
            x=datetime.datetime.strptime(row.get("Date and Time"),'%Y-%m-%d %H:%M:%S %p')
            hours=x.strftime("%H")
            seconds=x.strftime("%S")
            day=x.strftime("%d")
            month=x.strftime("%m")
            year=x.strftime("%Y")
            print(f"{hours:>6}:{seconds:>6}\t{day:>6}:{month:>6}:{year:>6}")


