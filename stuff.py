import pandas as pd
import os
import csv

#read the path
# eg"/home/disu/Documents/Dev/pystuff/filess/"
file_path="USE YOUR FILE PATH"

#list all the files from the directory
file_list =  os.listdir(file_path)


mainList=[]
for file in file_list:
    with open(file_path+file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            mainList.append(row)

d = {}    
for dct in mainList:
    d.setdefault(dct['firstName'], {}).update(dct)
res = list(d.values())

# write result to res.csv file 
df = pd.DataFrame(res)
df.to_csv('res.csv', index=False, header=True)
