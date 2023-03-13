#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))
# size of enron dataset
print(len(enron_data))

# features per person
count = 0;
for data in enron_data:
    for key in enron_data[data]:
        count += 1
    break
print(count)

# POIs in enron data
poiCount = 0;
for data in enron_data:
    for key in enron_data[data]:
        if key == 'poi' and enron_data[data]['poi'] == 1:
            poiCount += 1;

print(poiCount)

# how many POIs Exist?
totalPoi = 0;
with open('../final_project/poi_names.txt', 'r') as f:
    file_data = f.read()
    while (f.readline()):
        print("reading line")
        totalPoi += 1;
print(totalPoi)
