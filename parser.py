import re
import csv
from collections import Counter
data='/root/task5/data.txt'
def reader(filename):
    with open (filename) as f:
        data=f.read()
        #print(data)
        #Reading all number of size 1 to 3 in given dataset
        ip =r'\d{1,3}\,\d{1,3}\,\d{1,3}\,\d{1,3}'
        #Getting all status 
        st=r'\d{1,3}'
        #finding all IP in dataset
        ips=re.findall(ip, data)
        #finding status 
        st=re.findall(st,data)
        return ips
#this function is to count number of IP
def count(ips):
    return Counter(ips)
#To parse data and save in CSV file     
def write(counter):
    with open('pro.csv','w') as csvfile:
        writer=csv.writer(csvfile)
        #Giving header to dataset
        header=['IP','Frequency','Status','url']
        writer.writerow(header)
        for item in counter:
            writer.writeout((item,counter[item]))
#this will take all required credential from dataset            
write(count(reader('data')))
