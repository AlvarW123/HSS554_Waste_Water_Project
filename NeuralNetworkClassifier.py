import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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
train_df, test_df = train_test_split(df,test_size=0.2)

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

# Define the model
model = Sequential()
model.add(Dense(128, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(56, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, Y_train, epochs=50, batch_size=16, validation_split=0.2) 

# Make predictions
y_pred = model.predict(X_test_scaled)

y_pred_mod = 1-(y_pred < 0.5)*1 

print(confusion_matrix(Y_test,y_pred_mod))