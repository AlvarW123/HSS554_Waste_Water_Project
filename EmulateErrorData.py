import numpy as np
import pandas as pd

np.random.seed(10)

dfs = []

# get encoding for dataframe
with open('data/modified/uster_1.csv') as f:
    encoding = f.encoding

# load dataframes
for i in range(1,7):
    dfs.append(pd.read_csv("data/added_delay/uster_"+str(i)+".csv", encoding = encoding))

# index of variable we add error to
index = 14

# drop data points with zero measurement for error, motivate later


def random_error():
    r = np.random.random()-0.5
    if r<0:
        return r-0.5
    else:
        return r+0.5

# add error, column with percentage change in range [-1,1], and column with 0,1 bool showing whether the variable was modified
for df in dfs:
    # randomly select points to modify
    ind = np.random.randint(0,df.shape[0], size = int(np.floor(df.shape[0]*0.3)))
    # add change cplumn
    df["percent_change"] = np.zeros(df.shape[0])
    df.iloc[ind,[df.shape[1]-1]] = df.iloc[ind,[df.shape[1]-1]].applymap(lambda x: x + random_error())
    # add fault, distributed around actual value
    df.iloc[ind,[index]] += np.array(df.iloc[ind,[df.shape[1]-1]])*np.array(df.iloc[ind,[index]])
    # add modified
    df["modified"] = np.zeros(df.shape[0])
    df.iloc[ind,[df.shape[1]-1]] += 1

# standardize column names

for df in dfs:
    df.drop('Unnamed: 0', axis = 1, inplace = True)


for i in range(6):
    dfs[i].to_csv("data/added_error/uster_"+str(i+1)+".csv")

print(dfs[2].describe())