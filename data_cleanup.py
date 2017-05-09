import csv
import sys
import json
import codecs

f=open("Idsandnames.csv","rt")
p=1
csv.field_size_limit(500 * 1024 * 1024)

looplength = 100
cfr= ""
number = 1
integerslist=[]
listofInt=[]
jsondata=[]
links = dict()
listofnodes=[]
try:
    reader = csv.reader(f)
    for row in reader:
        listofInt.append(row)
finally:
    f.close()
listofinttohun = listofInt[0:1000]

for row in listofinttohun:
    cfr=(str(row[1]))[:-2]
    if cfr:
        #listofnodes.append({'id':cfr, 'name':row[4]})
        integerslist.append(cfr)
        

for row in integerslist:
    cfr=row
    #print cfr
    if cfr >0:
        number =1
        for row1 in listofinttohun:
            if str(cfr) in row1[3]:
                number =number +1
                jsondata.append({'source':integerslist.index(cfr),'target':integerslist.index((str(row1[1]))[:-2])})
        links[cfr]=number


for row in integerslist:
    listofnodes.append({'id':str(row), 'size': links[row]})

with codecs.open('data2.json', 'w', 'utf-8') as f:
    f.write(json.dumps(listofnodes, ensure_ascii=False))

with codecs.open('data1.json', 'w', 'utf-8') as f:
    f.write(json.dumps(jsondata, ensure_ascii=False))
