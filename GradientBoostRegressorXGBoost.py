import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
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
train_df, test_df = train_test_split(df,test_size=0.1)

test_df.drop(["Unnamed: 0" ], axis = 1,inplace = True)
train_df.drop(["Unnamed: 0"], axis = 1,inplace = True)

X_train = train_df.copy()
X_train["Month"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.month)
X_train["Day"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.day)
X_train["Hour"] = pd.to_datetime(X_train["Time [-]"]).apply(lambda x: x.hour)

X_train.drop(["Time [-]","N2O [kgN/h]"], axis = 1,inplace = True)


Y_train = np.array(train_df[["N2O [kgN/h]"]])

X_test = test_df.copy()
X_test["Month"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.month)
X_test["Day"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.day)
X_test["Hour"] = pd.to_datetime(X_test["Time [-]"]).apply(lambda x: x.hour)

time = X_test["Time [-]"]
X_test.drop(["Time [-]","N2O [kgN/h]"], axis = 1,inplace = True)

scaler = StandardScaler()

X_test_scaled = scaler.fit_transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)

Y_test = np.array(test_df[["N2O [kgN/h]"]])

scaler = StandardScaler()
X_test_scaled = scaler.fit_transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)
print("start testing")

boost = GBR(n_estimators=1000,
learning_rate=0.01)
boost.fit(X_train_scaled, Y_train)

y_pred = boost.predict(X_test_scaled)

importance = dict()
for i in range(boost.feature_importances_.shape[0]):
    importance[X_train.columns[i]] = boost.feature_importances_[i]

print(dict(sorted(importance.items(), key=lambda item: item[1])))
print(mean_absolute_error(Y_test,y_pred))