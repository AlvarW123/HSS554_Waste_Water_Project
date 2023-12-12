import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

selected_features = ['NO2 [gN/m3]',
'NO3 [gN/m3]',
'airflow [m3/h]',
'level [m]',
'NH4 [gN/m3]',
'temp [Ã‚Â°C]',
'inflow [l/s]',
'NH4_load [gN/h]',
'DO [gO2/l]',
'O2_Offgas [%]',
]

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

for i in range(1,13):
    df["m"+str(i)] = np.zeros(df.shape[0])
    df["m"+str(i)] = (df["Month"] == i)*1
    selected_features.append("m"+str(i))

df.drop(["Month"], axis = 1,inplace = True)


train_df, test_df = train_test_split(df,test_size=0.25)


# X_train = train_df.drop(["N2O [kgN/h]","Time [-]","tank_nr"], axis = 1)

X_train = train_df[selected_features]

Y_train = train_df[["N2O [kgN/h]"]].values

#X_test = test_df.drop(["N2O [kgN/h]","Time [-]","tank_nr"], axis = 1)
X_test = test_df[selected_features]

print(Y_train.shape)


scaler = MinMaxScaler()

X_test_scaled = scaler.fit_transform(X_test)
X_train_scaled = scaler.fit_transform(X_train)
Y_test = test_df[["N2O [kgN/h]"]].values
# Define the model
model = Sequential()
model.add(Dense(256, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(128, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='MSE', metrics=['MSE'])
# Train the model
model.fit(X_train_scaled, Y_train, epochs=25, batch_size=16, validation_split=0.2) 

y_pred_test = model.predict(X_test_scaled)

print("r2: "+str(r2_score(Y_test,y_pred_test)))
print("mean absolute error: "+str(mean_absolute_error(Y_test,y_pred_test)))
print("Root of mean squared error: "+str(mean_squared_error(Y_test,y_pred_test,squared=False)))

y_pred_train = model.predict(X_train_scaled)

print("r2_train: "+str(r2_score(Y_train,y_pred_train)))
print("mean absolute error_train: "+str(mean_absolute_error(Y_train,y_pred_train)))
print("Root of mean squared error_train: "+str(mean_squared_error(Y_train,y_pred_train,squared=False)))

for i in range(1,7):
    index = test_df.tank_nr == i
    plt.cla()
    plt.plot( Y_test[index],label = "y_test")
    plt.plot(y_pred_test[index], label = "y_pred")
    plt.ylabel("N2O emissions [kgN/h]")
    plt.xlabel("index")
    plt.legend()
    plt.savefig("figures/ANN/ann_tank_"+str(i)+".png")
    plt.cla()

    plt.plot( np.abs(Y_test[index]-y_pred_test[index]),label = "|y_test-y_pred|")
    plt.ylabel("N2O emissions [kgN/h]")
    plt.xlabel("index")
    plt.legend()
    plt.savefig("figures/ANN/ann_abs_diff_tank_"+str(i)+".png")

