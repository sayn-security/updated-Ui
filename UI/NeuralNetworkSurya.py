#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Import the required libraries.
import pandas as pd  
import numpy as np   
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import shuffle
from pandas import ExcelFile
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#import seaborn as sns
import warnings
def bla(abc,defg):
    warnings.filterwarnings('ignore')  # "error", "ignore", "always", "default", "module" or "once"
    # Excel file name.
    fileName = "bigDataFile copy.xlsx"
    fn = "DataCollect.xlsx"
    data1 = pd.read_excel(fn, sheetname='Sheet1')
    #validationFileName = "prediction_sheet.xlsx"
    # Read the dataset using pandas library.
    #data = pd.read_csv(fileName, names = colnames, sep=';')
    data = pd.read_excel(fileName, sheetname='Sheet1', usecols="A:AK")
    #validationData = pd.read_excel(validationFileName, sheetname='Sheet1', usecols="A:D")
    #data = shuffle(data)
    # Divide the dataset into x-data and y-data.
    # The drop() method drops this column.
    X = data.drop(['subject'], axis=1)
    y = data['subject']
    X1 = data1.drop(["subject"], axis=1)
    #print (X1)
    y1 = data1["subject"]
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    # conver subject column to numirical value
    #y= labelencoder.fit_transform(data['subject'])
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X_1 = LabelEncoder()
    onehotencoder = OneHotEncoder(categorical_features = [1])
    X = onehotencoder.fit_transform(X).toarray()
    X = X[:, 1:]
    X1 = onehotencoder.fit_transform(X1).toarray()
    X1 = X1[:, 1:]
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1, random_state = 0)
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    # training algorithm
    from sklearn.neural_network import MLPClassifier
    # model prameters
    """
    MLPClassifier(activation='relu', alpha=1e-05, batch_size=200, beta_1=0.9,
           beta_2=0.999, early_stopping=False, epsilon=1e-08,
           hidden_layer_sizes=(15,), learning_rate='constant',
           learning_rate_init=0.0001, max_iter=200, momentum=0.9,
           n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
           random_state=0, shuffle=True, solver='lbfgs', tol=0.0001,
           validation_fraction=0.1, verbose=False, warm_start=False)
    """
    clf = MLPClassifier(solver='adam', alpha=0.00001,batch_size=128,learning_rate_init=0.01, 
                        activation='relu',
                        hidden_layer_sizes=(abc,defg)
                        ,random_state=0)

    clf.fit(X_train, y_train)  
    y_pred = clf.predict(X1)
    print(y_pred)
    #making confusing matrix
    '''from sklearn.metrics import confusion_matrix 
    from sklearn.metrics import accuracy_score 
    from sklearn.metrics import classification_report 
    results = confusion_matrix(y_test, y_pred) 
    '''
    #sns.heatmap(results,annot=True,fmt='2.0f') 
    #print (abc,defg)
    '''from ann_visualizer.visualize import ann_viz;
    ann_viz(clf, title="My first neural network")'''

    '''print ('Report : ')
    print (classification_report(y_test, y_pred) )
    print ('Confusion Matrix :')
    print (results)
    print("Done")'''
    return y_pred
def runner():
    i = 1
    j = 200
    max=0
    count=-1
    count1=-1
    while i < 200:
        a = bla(i,j)
        if(a>max):
            max=a
            count=i
            count1=j
        i+=1
    print (count,count1,a)
def main():
    #print (bla(109,200))
    print (bla(194,186))
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




