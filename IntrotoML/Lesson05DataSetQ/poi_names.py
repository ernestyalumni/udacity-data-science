##### Udacity
####   Intro to Machine Learning
###     Lesson 5--Datasets and Questions
##       cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3035018557/m-3021038710

##### run this from your local copy of /ud120-projects-master/final_project

##### We compiled a list of all POI names (in ../final_project/poi_names.txt) and associated email addresses (in ../final_project/poi_email_addresses.py).
##### How many POI’s were there total? (Use the names file, not the email addresses, since many folks have more than one address and a few didn’t work for Enron, so we don’t have their emails.)
#### cf. https://www.udacity.com/course/viewer#!/c-ud120/l-2291728537/e-3035018557/m-3021038710

txtnames = open("poi_names.txt")
txtnames = txtnames.readlines()
len(txtnames)-2 # 35

