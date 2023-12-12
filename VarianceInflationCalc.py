import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
# Assuming 'data' is your dataset containing predictors
# 'X' contains predictor variables for which VIF needs to be calculated
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

df.drop(["Time [-]","tank_nr","N2O [kgN/h]"], axis = 1, inplace=True)

# Calculate VIF for each predictor

X = add_constant(df)
vif_data = pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
              index=X.columns)

print(vif_data)