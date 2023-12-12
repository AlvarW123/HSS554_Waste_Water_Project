import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor as RF
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, mean_absolute_error, r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler

np.random.seed(10)

dfs = []

# get encoding for dataframe
with open('data/added_error/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/modified_uster/uster_"+str(i)+".csv", encoding = encoding))

# test_df = dfs.pop()
# train_df = pd.concat(dfs)
df = pd.concat(dfs)
df.drop(["Unnamed: 0"], axis = 1,inplace = True)

df["Month"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.month)
df["Day"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.day)
df["Hour"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.hour)

months = []
days = []
hours = []

for i in range(1,13):
    df["m"+str(i)] = np.zeros(df.shape[0])
    df["m"+str(i)] = (df["Month"] == i)*1
    months.append("m"+str(i))

for i in range(1,8):
     df["d"+str(i)] = np.zeros(df.shape[0])
     df["d"+str(i)] = (df["Day"] == i)*1
   # days.append("d"+str(i))


for i in range(0,24):
     df["h"+str(i)] = np.zeros(df.shape[0])
     df["h"+str(i)] = (df["Hour"] == i)*1
   # hours.append("h"+str(i))

df.drop(["Month","Day","Hour"], axis = 1,inplace = True)


train_df, test_df = train_test_split(df,test_size=0.1)


#X_train = train_df.copy()
X_train = df.copy()
Y_train = np.array(X_train[["N2O [kgN/h]"]])

X_train.drop(["Time [-]","N2O [kgN/h]"], axis = 1,inplace = True)



#Y_train = np.array(train_df[["N2O [kgN/h]"]])

X_test = test_df.copy()

time = X_test["Time [-]"]
X_test.drop(["Time [-]","N2O [kgN/h]"], axis = 1,inplace = True)

scaler = StandardScaler()

X_test_scaled = scaler.fit_transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)

Y_test = np.array(test_df[["N2O [kgN/h]"]])

rfs = []

for i in range(10,11):#range(5,X_train.shape[1]):
    print("start iteration for i = "+str(i))
    rf = RF(max_features=i)
    rfs.append(rf.fit(X_train_scaled, Y_train))
    print("iteration complete")
    

importance = dict()
for i in range(rf.feature_importances_.shape[0]):
    importance[X_train.columns[i]] = rf.feature_importances_[i]

print(dict(sorted(importance.items(), key=lambda item: item[1])))

covered_prob = 0

sorted_importance = sorted(importance.items(), key=lambda item: item[1])
sorted_importance.reverse()

for p in sorted_importance:
    if(covered_prob>0.8):
        break
    print(p)
    covered_prob += p[1]
    
print(covered_prob)

y_pred_test = RF.predict(X_train_scaled)
print("r2: "+str(r2_score(Y_test,y_pred_test)))
print("mean absolute error: "+str(mean_absolute_error(Y_test,y_pred_test)))
print("Root of mean squared error: "+str(mean_squared_error(Y_test,y_pred_test,squared=False)))