import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import libsvm
import numpy as np
from getDistances import distance_in_m

train=pd.read_csv('train.csv', parse_dates = ['Dates'])
test=pd.read_csv('test.csv', parse_dates = ['Dates'])

crime_label = preprocessing.LabelEncoder()
crime = crime_label.fit_transform(train.Category)
 
days = pd.get_dummies(train.DayOfWeek)
district = pd.get_dummies(train.PdDistrict)
hour = train.Dates.dt.hour
hour = pd.get_dummies(hour) 

longi = train['X'].tolist()
lat = train['Y'].tolist()
z = zip(lat,longi)
dist = []
for i in range(len(z)) :
	dist.append(distance_in_m(z[i][0],z[i][1]))

dist = pd.DataFrame(dist)

train_data = pd.concat([hour, days, district,dist], axis=1)
train_data['crime']=crime
 
days = pd.get_dummies(test.DayOfWeek)
district = pd.get_dummies(test.PdDistrict)
 
hour = test.Dates.dt.hour
hour = pd.get_dummies(hour) 

longi = test['X'].tolist()
lat = test['Y'].tolist()
z = zip(lat,longi)
dist = []
for i in range(len(z)) :
	dist.append(distance_in_m(z[i][0],z[i][1]))

dist = pd.DataFrame(dist)
test_data = pd.concat([hour, days, district,dist], axis=1)
features = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday','Wednesday', 'BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION','NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']

model = BernoulliNB(alpha = 0.9)
model.fit(train_data[features], train_data['crime'])
predicted = model.predict_proba(test_data[features])

result=pd.DataFrame(predicted, columns=crime_label.classes_)
result.to_csv('NB_Result.csv', index = True, index_label = 'Id' )