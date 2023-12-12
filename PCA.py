import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



def preform_pca(df,col = [],n = 2):
    if(col == []):
        df_in_use = df
    else:
        df_in_use = df.iloc[:,col]
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_in_use)
    pca = PCA(n_components=n)
    pca.fit(df_scaled)
    return pca

## Perform pca

dfs = []

# get encoding for dataframe
with open('data/added_error/uster_1.csv') as f:
    encoding = f.encoding

for i in range(1,7):
    dfs.append(pd.read_csv("data/modified_uster/uster_"+str(i)+".csv", encoding = encoding))


#for i in range(1,8):
 #   df["d"+str(i)] = np.zeros(df.shape[0])
  #  df["d"+str(i)] = (df["Day"] == i)*1
   # days.append("d"+str(i))


#for i in range(0,24):
 #   df["h"+str(i)] = np.zeros(df.shape[0])
  #  df["h"+str(i)] = (df["Hour"] == i)*1
   # hours.append("h"+str(i))
# test_df = dfs.pop()
# train_df = pd.concat(dfs)
df = pd.concat(dfs)

df["Month"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.month)
df["Day"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.day)
df["Hour"] = pd.to_datetime(df["Time [-]"],dayfirst=True).apply(lambda x: x.hour)

   


df.drop(["Unnamed: 0"], axis = 1,inplace = True)

df.drop(["Time [-]","tank_nr","N2O [kgN/h]"] ,axis = 1,inplace = True)
pca = preform_pca(df,n=None)
print(pca.components_)
print(pca.explained_variance_ratio_)