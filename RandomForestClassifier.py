import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler


dfs = []

# get encoding for dataframe
with open('data/added_error/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/added_error/uster_"+str(i)+".csv", encoding = encoding))

# test_df = dfs.pop()
# train_df = pd.concat(dfs)
df = pd.concat(dfs)
train_df, test_df = train_test_split(df,test_size=0.1)

test_df.drop(["Unnamed: 0" ], axis = 1,inplace = True)
train_df.drop(["Unnamed: 0"], axis = 1,inplace = True)

X_train = train_df.iloc[:,range(train_df.shape[1]-2)]
X_train["Month"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.month)
X_train["Day"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.day)
X_train["Hour"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.hour)

X_train.drop(["Time [-]"], axis = 1,inplace = True)


Y_train = train_df.modified

X_test = test_df.iloc[:,range(train_df.shape[1]-2)]
X_test["Month"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.month)
X_test["Day"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.day)
X_test["Hour"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.hour)


X_test.drop(["Time [-]"], axis = 1,inplace = True)

Y_test = test_df.modified

scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)

rfs = []

for i in range(7,8):
    print("start iteration for i = "+str(i))
    rf = RF(max_features=i)
    rfs.append(rf.fit(X_train, Y_train))
    print("iteration complete")
    

for rf in rfs:
    y_pred = rf.predict(X_test)
    print(confusion_matrix(Y_test,y_pred))

