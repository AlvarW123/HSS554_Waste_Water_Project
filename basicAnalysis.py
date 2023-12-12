import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.preprocessing import MinMaxScaler

# Assuming 'data' is your dataset containing predictors
# 'X' contains predictor variables for which VIF needs to be calculated
dfs = []

# get encoding for dataframe
with open('data/added_error/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/modified_uster/uster_"+str(i)+".csv", encoding = encoding))
    print("tank "+str(i)+", datapoints: "+str(dfs[i-1].shape[0]))

# test_df = dfs.pop()
# train_df = pd.concat(dfs)
df = pd.concat(dfs)
print("total: "+str(df.shape[0]))
df.drop(["Unnamed: 0"], axis = 1,inplace = True)

for i in range(1,7):
    index = df.tank_nr == i
    plt.plot( df[index]["N2O [kgN/h]"].values)
    plt.title("tank "+str(i))
    plt.ylabel("N2O emissions [kgN/h]")
    plt.xlabel("index")
    plt.savefig("figures/N2O/tank_"+str(i)+".png")
    plt.cla()


df.drop(["Time [-]","tank_nr"], axis = 1, inplace=True)
scaler = MinMaxScaler()

df_scaled = scaler.fit_transform(df)
sd = dict()
avg = dict()
ratio = dict()
for i in range(df.shape[1]):
    c = df.columns[i]
    sd[c] = np.std(df_scaled[:,i])
    avg[c] = np.average(df_scaled[:,i])
    ratio[c] = sd[c]/avg[c]



temp = pd.DataFrame([sd,avg,ratio])
temp.index = ["std","avg","ratio"]


temp.to_csv("data/metrics_scaled.csv")


sd_scaled = dict()
avg_scaled = dict()
ratio_scaled = dict()
df_matrix = df.values
for j in range(df.shape[1]):
    c = df.columns[j]
    sd_scaled[c] = np.std(df_matrix[:,j])
    avg_scaled[c] = np.average(df_matrix[:,j])
    ratio_scaled[c] = sd_scaled[c]/avg_scaled[c]

    
temp_scaled = pd.DataFrame([sd_scaled,avg_scaled,ratio_scaled])
temp_scaled.index = ["std","avg","ratio"]


temp_scaled.to_csv("data/metrics.csv")


