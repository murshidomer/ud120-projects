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
import re
from time import time

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
# not doing anything witH this list, unnecessary
# poicount = [enron_data["name"]for data in enron_data if enron_data[data]["poi"] == 1]
# print(len(poicount))
# next(item for item in enron_data if enron_data[item]["poi"] == "1")
poiCount = 0;
for data in enron_data:
    if enron_data[data]["poi"] == 1:
        poiCount += 1;

print(poiCount)

# how many POIs Exist?
totalPoi = 0;
with open('../final_project/poi_names.txt', 'r') as f:
    while (f.readline()):
        totalPoi += 1
print(totalPoi)

print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

totalPayments = [(name, enron_data[name]["total_payments"]) for name in enron_data if
                 (re.search('^LAY|^SKILLING|^FASTOW', name))]
# maxKey = max(keyFound)[1]
# print(maxKey)
totalPayments.sort(reverse=True, key=lambda a: a[1])
print(totalPayments[0])
for name in enron_data:
    for key in enron_data[name]:
        print(key)
    break

knownEmail = [name for name in enron_data if enron_data[name]["email_address"] != 'NaN']
quantifiedSalary = [name for name in enron_data if enron_data[name]["salary"] != 'NaN']
print(len(knownEmail))
print(len(quantifiedSalary))
