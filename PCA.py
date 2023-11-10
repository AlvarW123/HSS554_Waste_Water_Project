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

plt.cla()
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig("figures/principal_uster")

principal_components = preform_pca(df = df,col = range(8,18))
## Check result using plot, weather related
print(df.columns[8:17])

plt.cla()
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig("figures/principal_weather")

## full
principal_components = preform_pca(df = df,col = range(0,18))
## Check result using plot
print(df.columns[1:17])

plt.cla()
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig("figures/principal_all")

## No clear outliers

## Look for duplicate dates, no values detected.

duplicate = df["Datetime"].duplicated()
duplicate_index = duplicate[duplicate].index
print(duplicate_index.size)

## Plot as time series to look for trends, possible issue with 0 values. Likely due to repairs etc, we are going to treat thoose days as nan

plt.cla()

# min max feature normalization
#for c in df.columns:
    #if(c not in ["Year", "Month", "Day" , "Datetime"]):
        # df[[c]] = (df[[c]] - df[[c]].min())/(df[[c]].max() - df[[c]].min())



for c in df.columns:
    if(c not in ["Year", "Month", "Day" , "Datetime"]):
        x = np.array(range(0,df.shape[0]))
    #calculate equation for trendline
        z = np.polyfit(x,np.array(df[[c]]).reshape(-1),1)
        p = np.poly1d(z)

    #add trendline to plot
        plt.plot(df[[c]], label = c)
        plt.plot(x, p(x))

        plt.title(c)
        plt.savefig("figures/"+c)
        plt.xlabel("index")
        plt.ylabel("scale")
        plt.legend()
        plt.cla()
