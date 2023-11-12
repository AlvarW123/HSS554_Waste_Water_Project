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
    principal_components = pca.fit_transform(df_scaled)
    return principal_components

## Perform pca

# for non weather

## Check result using plot
for i in range(1,9):
    name = ""
    if(i < 7):
        name = "uster_" + str(i)
        df = pd.read_csv("data/with_selected_variables/uster_"+(str(i))+".csv")
    else:
        name = "lucerne_" + str(i-6)
        df = pd.read_csv("data/with_selected_variables/lucerne_"+(str(i-6))+".csv")


    df = df.drop("Time []", axis = 1)

    principal_components = preform_pca(df = df,col = range(0,5))
    plt.cla()
    plt.scatter(principal_components[:, 0], principal_components[:, 1])
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.savefig("figures/pca_plot_"+name)

    ## Plot as time series to look for trends, possible issue with 0 values. Likely due to repairs etc, we are going to treat thoose days as nan

    plt.cla()


for j in np.linspace(1,7,num=4,dtype=int):
    name = ""
    if(j < 7):
        name = "uster_" + str(j)
        df_1 = pd.read_csv("data/with_selected_variables/uster_"+(str(j))+".csv")
    else:
        name = "lucerne_" + str(j-6)
        df_1 = pd.read_csv("data/with_selected_variables/lucerne_"+(str(j-6))+".csv")

    if(j+1 < 7):
        name = name + " combined_with_uster_" + str(j+1)
        df_2 = pd.read_csv("data/with_selected_variables/uster_"+(str(j))+".csv")
    else:
        name = name + " combined_with_lucerne_" + str(j-5)
        df_2 = pd.read_csv("data/with_selected_variables/lucerne_"+(str(j-5))+".csv")

    df_1 = df_1.drop("Time []", axis = 1)
    df_2 = df_2.drop("Time []",axis = 1)
    df = pd.concat([df_1,df_2],axis = 1)
    principal_components = preform_pca(df = df,col = range(0,10))
    plt.cla()
    plt.scatter(principal_components[:, 0], principal_components[:, 1])
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.savefig("figures/pca_plot_"+name)

    ## Plot as time series to look for trends, possible issue with 0 values. Likely due to repairs etc, we are going to treat thoose days as nan

    plt.cla()

