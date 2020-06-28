#importing required libraries
from sklearn.cluster import KMeans
import panda as pd
from numpy np
from collections import Counter
import csv
import os
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#reading dataset
data = pd.read_csv('/root/task5/pro.csv')
#dropping the unusefull
data = data.dropna()
data = data.drop(['url'], axis='columns',implace=True)
ip= data['IP']
count=Counter(ip)

#scalling the dataset
sc = StandardScaler()
data_scaled = sc.fit_transform(dataset)
model = KMeans(n_clusters=4)
#fitting the model
model.fit(data_scaled)
pred  = model.fit_predict(data_scaled)
dataset_scaled = pd.DataFrame(data_scaled, columns=['IP', 'c'])
pred=dataset_scaled['cluster']

#plotting the clusters 
f1 = data[data.cluster==0]
f2 = data[data.cluster==1]
f3 = data[data.cluster==2]
f4 = data[data.cluster==3]
plt.scatter(f1.count,f1['IP'],color='green')
plt.scatter(f2.count,f2['IP'],color='red')
plt.scatter(f3.count,f3['IP'],color='black')
plt.scatter(f4.count,f4['IP'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],km.cluster_centers_[:,2],color='purple',marker='*',label='centroid')
plt.xlabel('Count')
plt.ylabel('IP')
plt.legend()

#Main part of code taking out anamoly from data and store it into array
block = []
for i, r in pred.iterrows():
    if pred['Count'].loc[i] > 200:
          block.append(pred['Cluster'].loc[i])
block = max(set(block), cou = block.count)

#this part will check the values in array
for ip in block:
    #this will check for number in this format
    ip==r'\d{1,3}\,\d{1,3}\,\d{1,3}\,\d{1,3}'
    #this command will put that paticular IP in blacklist(block)
    os.system("ip route add blackhole {}".format(ip))
    
#After blocking it will store blocked IP into CSV file 
for ips in block:
    ips=ips.split('.')
file=open('blocked_list.csv','w')
file.write('blocked'+'\n')
for x in ips:
    print(ips[0]+'.'+ips[1]+'.'+ips[2]+'.'+ str(x))
    file.write(ips[0]+'.'+ips[1]+'.'+ips[2]+'.'+ str(x) + '\n')
file.close()
