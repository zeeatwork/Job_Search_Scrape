import pandas as pd
import json
import os
from firebase import Firebase

folder = r'/Users/zenziali/Desktop/Phlask/JSWebScraping/treeOutput'

li = []

for f in os.listdir(folder) : 
  data = pd.read_csv(folder + '/' + f)
  li.append(data)

final = pd.concat(li)  

final = final[['Point X', 'Point Y', 'Street Address', 'City', 'Postal Code',
       'Planting Site Id', 'Updated At', 'Tree Id', 'Genus', 'Species', 'Common Name'
       ]]
# final.to_csv('/Users/zenziali/Desktop/Phlask/treeMap.csv', index = False)

final.reset_index(drop=True, inplace=True)
data1 = json.loads(final.to_json(orient="records"))
# final[final['Tree Present'] != True]

config = {
    'apiKey': "AIzaSyABw5Fg78SgvedyHr8tl-tPjcn5iFotB6I",
    'authDomain': "phlask-web-map.firebaseapp.com",
    'databaseURL': "https://phlask-web-map-forage.firebaseio.com",
    'projectId': "phlask-web-map",
    'storageBucket': "phlask-web-map.appspot.com"
}

firebase = Firebase(config)

auth = firebase.auth()

db = firebase.database()

data = db.get().val()   

def save_data(data):
    db.child('').set(data)

save_data(data1)    