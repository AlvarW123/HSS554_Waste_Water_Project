import numpy as np
import pandas as pd

dfs = []

# get encoding for dataframe
with open('data/added_error/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/modified_uster/uster_"+str(i)+".csv", encoding = encoding))

delay = 5

variables_to_change = [14]

for df in dfs:
    for j in variables_to_change:
        name = df.columns[j]
        for k in range(1,delay+1):
            vector = np.zeros(df.shape[0])
            for i in range(delay, df.shape[0]):
                vector[i] = df.iloc[i-k,j]
            df[name+"_delay_"+str(k)] = vector



for df in dfs:
    df.drop('Unnamed: 0', axis = 1, inplace = True)
    df.drop(index=df.index[:delay], axis=0, inplace=True)


for i in range(6):
    dfs[i].to_csv("data/added_delay/uster_"+str(i+1)+".csv")
