from sklearn.naive_bayes import GaussianNB 

def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
            
    ### your code goes here!
    clf = GaussianNB()  # clf is classifier
    clf.fit(features_train, labels_train)
    
    return clf
