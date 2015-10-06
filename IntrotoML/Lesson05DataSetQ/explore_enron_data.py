# EY : 20151005 run this in /ud120-projects-master/datasets_questions

#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#####################################################################################
##### How many data points (people) are in the dataset?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3004808717/m-3005648570
len(enron_data) # 146

##### For each person, how many features are available?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3035498566/m-3010518798
len( enron_data["SKILLING JEFFREY K"].keys()) # 21

##### The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3021858558/m-3011778732
len( [1 for person in enron_data if enron_data[person]['poi'] ] ) # 18

##### What is the total value of the stock belonging to James Prentice?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3025828584/m-3010568605

[s for s in enron_data.keys() if "PRENTICE" in s] # ['PRENTICE JAMES']
enron_data['PRENTICE JAMES'].keys()
enron_data['PRENTICE JAMES']['total_stock_value'] # 1095040

##### How many email messages do we have from Wesley Colwell to persons of interest?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3018078550/m-3014558607
[s for s in enron_data.keys() if "WESLEY" in s] # ['COLWELL WESLEY']
enron_data['COLWELL WESLEY']['from_this_person_to_poi'] # 11

##### What’s the value of stock options exercised by Jeffrey Skilling?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3013308702/m-3007818802
[s for s in enron_data.keys() if "SKILLING" in s] # ['SKILLING JEFFREY K']
enron_data['SKILLING JEFFREY K']['exercised_stock_options'] # 19250000

##### Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
##### How much money did that person get?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3017538609/m-3005068624
execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s) ] 
max( [(enron_data[person]['total_payments'],person) for person in execs] ) # (103559793, 'LAY KENNETH L')

##### How many folks in this dataset have a quantified salary? What about a known email address?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3003098655/m-3003048586
len([enron_data[person]['salary'] for person in enron_data if enron_data[person]['salary'] != 'NaN']) # 95
len([enron_data[person]['email_address'] for person in enron_data if enron_data[person]['email_address'] != 'NaN' ] # 111

##### How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
#### https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3033088677/m-3013038717

float(len([enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] == 'NaN' ]) ) / float( len( enron_data.keys() ) )*100. # 14.383561643835616

##### How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
#### https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3005138679/m-3029558686

poi_names_f =  open("../final_project/poi_names.txt", "r")
poi_names = poi_names_f.readlines()
poi_names_f.close()
poi_names = poi_names[2:]
poi_names = [ name.split(' ',1)[1].strip('\n') for name in poi_names]
poi_names2 = [name.split(', ') for name in poi_names]
len(poi_names) # 35

len([ enron_data[person]['total_payments'] for person in enron_data if (enron_data[person]['poi']) ] # 18

##### If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change. 
##### What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3005888615/m-3026198572

len( [ enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] =='NaN' ] ) # 21 
len(enron_data) # 146

##### What is the new number of POI’s in the dataset? What percentage of them have “NaN” for their total stock value?
#### https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3052468536/m-3010158775


