
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from pandas import ExcelFile

filename1 = "DataCollected.xlsx"
filename = "SuryaData.xlsx"

pred = KNeighborsClassifier(1)

dataset1= pd.read_excel(filename1, sheetname = "Sheet1", usecols="A:AK")
dataset = pd.read_excel(filename, sheetname = "Sheet1", usecols="A:AK")
x1 = dataset.drop(["subject"], axis = 1)
y1 = dataset["subject"]
from sklearn.preprocessing import LabelEncoder
labelencode = LabelEncoder()
y1 = labelencode.fit_transform(dataset["subject"])

pred.fit(X=x1,y=y1)
xa = dataset1.drop(["sub00"], axis = 1)
ya = dataset1["sub00"]

coef = pred.predict_proba
print(coef)
x_train,x_test,y_train,y_test=train_test_split(x1,y1,random_state=1,test_size=1)

sc_x=StandardScaler()
x_train = sc_x.fit_transform(x_train)
print(x_train)
x_test=sc_x.transform(x_train)


sqa= int(math.sqrt(len(x1)))
print (sqa)
classifier=KNeighborsClassifier(n_neighbors=1,p=2,metric='euclidean')
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_train)

cm= confusion_matrix(y_train,y_pred)
print(cm)

cl=classification_report(y_train,y_pred)
print(cl)

acc=accuracy_score(y_train,y_pred)
print(acc)


