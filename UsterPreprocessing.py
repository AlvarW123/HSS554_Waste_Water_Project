import numpy as np
import pandas as pd

np.random.seed(10)

dfs = []

# get encoding for dataframe
with open('data/modified/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/modified/uster_"+str(i)+".csv", encoding = encoding))

# index of variable we add error to
index = 14

# drop data points with zero measurement for error, motivate later

count = 1

for df in dfs:
    #df.drop(df[np.array(df.iloc[:,[index]])==0].index, inplace = True)
    df["tank_nr"] = np.zeros(df.shape[0])+count
    count+=1


col_names = [c.replace("_SB1","") for c in dfs[0].columns]

for df in dfs:
    df.columns = col_names
    df.drop('Unnamed: 0', axis = 1, inplace = True)


for i in range(6):
    dfs[i].to_csv("data/modified_uster/uster_"+str(i+1)+".csv")

print(dfs[2].describe())

