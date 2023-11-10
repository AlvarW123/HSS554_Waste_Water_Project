import pandas as pd
import numpy as np


with open('data/uster_data.csv') as f:
    encoding = f.encoding
#df = pd.read_csv("data/Data-Melbourne_F_fixed.csv")
u_df = pd.read_csv("data/uster_data.csv", encoding = encoding)

with open('data/lucerne_data.csv') as f:
    encoding = f.encoding
l_df = pd.read_csv("data/lucerne_data.csv", encoding = encoding)

with open('data/altenrhein_data.csv') as f:
    encoding = f.encoding
a_df = pd.read_csv("data/altenrhein_data.csv",encoding = encoding)


u_df.dropna(inplace = True)
l_df.dropna(inplace = True)
a_df.dropna(inplace = True)

print(u_df.describe())
print(l_df.describe())
print(a_df.describe())

#Divide the data per lane for uster.

col_1 =[col for col in u_df.columns if '_SB1' in col]
col_1.insert(0,"Time [-]")
u_df_1 = u_df[col_1]

col_2 =[col for col in u_df.columns if '_SB2' in col]
col_2.insert(0,"Time [-]")
u_df_2 = u_df[col_2]

col_3 =[col for col in u_df.columns if '_SB3' in col]
col_3.insert(0,"Time [-]")
u_df_3 = u_df[col_3]

col_4 =[col for col in u_df.columns if '_SB4' in col]
col_4.insert(0,"Time [-]")
u_df_4 = u_df[col_4]

col_5 =[col for col in u_df.columns if '_SB5' in col]
col_5.insert(0,"Time [-]")
u_df_5 = u_df[col_5]

col_6 =[col for col in u_df.columns if '_SB6' in col]
col_6.insert(0,"Time [-]")
u_df_6 = u_df[col_6]

# divide the data per lane for lucerne
col_1 =[col for col in l_df.columns if '_1 ' in col]
col_1.insert(0,"Time []")
l_df_1 = l_df[col_1]

col_2 =[col for col in l_df.columns if '_2 ' in col]
col_2.insert(0,"Time []")
l_df_2 = l_df[col_2]

# divide the data for altenrhein
col_1 =[col for col in a_df.columns if '_1 ' in col]
col_1.insert(0,"Time []")
col_1.insert(1,"Temperature [C]")
a_df_1 = a_df[col_1]

col_2 =[col for col in a_df.columns if '_2 ' in col]
col_2.insert(0,"Time []")
col_2.insert(1,"Temperature [C]")
a_df_2 = a_df[col_2]
print("modified")
print(u_df_1.describe())
print(l_df_1.describe())
print(a_df_1.describe())

u_check = (u_df_1.shape == u_df_2.shape) & (u_df_1.shape == u_df_3.shape) & (u_df_1.shape == u_df_4.shape) & (u_df_1.shape == u_df_5.shape) & (u_df_1.shape == u_df_6.shape)
l_check = l_df_1.shape == l_df_2.shape 
a_check = a_df_1.shape == a_df_2.shape 

print(u_check)
print(l_check)
print(a_check)

print(l_df_1.columns)
print(l_df_2.columns)

l_df_1 = l_df_1[l_df_1.columns.drop(['F_N2O_post_1 [gN2O-N/h]','O2post_1 [gO_2/m^3]'])]
l_check = l_df_1.shape == l_df_2.shape 
print(l_check)

u_df_1.to_csv("data/modified/uster_1.csv")
u_df_2.to_csv("data/modified/uster_2.csv")
u_df_3.to_csv("data/modified/uster_3.csv")
u_df_4.to_csv("data/modified/uster_4.csv")
u_df_5.to_csv("data/modified/uster_5.csv")
u_df_6.to_csv("data/modified/uster_6.csv")

l_df_1.to_csv("data/modified/lucerne_1.csv")
l_df_2.to_csv("data/modified/lucerne_2.csv")

a_df_1.to_csv("data/modified/altenrhein_1.csv")
a_df_2.to_csv("data/modified/altenrhein_2.csv")

