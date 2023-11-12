import pandas as pd
import numpy as np


with open('data/uster_data.csv') as f:
    encoding = f.encoding
u_df_1 = pd.read_csv("data/modified/uster_1.csv", encoding = encoding)
u_df_2 = pd.read_csv("data/modified/uster_2.csv", encoding = encoding)
u_df_3 = pd.read_csv("data/modified/uster_3.csv", encoding = encoding)
u_df_4 = pd.read_csv("data/modified/uster_4.csv", encoding = encoding)
u_df_5 = pd.read_csv("data/modified/uster_5.csv", encoding = encoding)
u_df_6 = pd.read_csv("data/modified/uster_6.csv", encoding = encoding)

c = ["inflow [l/s]","NO2 [gN/m3]", "O2 [gO2/m3]", "Time []", "NH4 [gN/m3]", "N20 [gN/h]"]

# due to not wanting to exclude any data set, we use a very simple set of variables. We take the inflow, N2O value and O_2 value.
u_df_1_mod = u_df_1.rename(columns = {"inflow_SB1 [l/s]" : "inflow [l/s]", "NO2_SB1 [gN/m3]": "NO2 [gN/m3]" , "DO_SB1 [gO2/l]" : "O2 [gO2/m3]",
                                       "Time [-]":"Time []"                                      ,"N2O_SB1 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB1 [gN/m3]":"NH4 [gN/m3]"})
u_df_1_mod["O2 [gO2/m3]"] = u_df_1_mod["O2 [gO2/m3]"]*1000
u_df_1_mod["N20 [gN/h]"] = u_df_1_mod["N20 [gN/h]"]*1000
u_df_1_mod["Time []"] = pd.to_datetime(u_df_1_mod["Time []"])
u_df_1_mod = u_df_1_mod[c]

u_df_2_mod = u_df_2.rename(columns = {"inflow_SB2 [l/s]" : "inflow [l/s]", "NO2_SB2 [gN/m3]": "NO2 [gN/m3]" , "DO_SB2 [gO2/l]" : "O2 [gO2/m3]","Time [-]":"Time []"   
                                                                         ,"N2O_SB2 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB2 [gN/m3]":"NH4 [gN/m3]"})
u_df_2_mod["O2 [gO2/m3]"] = u_df_2_mod["O2 [gO2/m3]"]*1000
u_df_2_mod["N20 [gN/h]"] = u_df_2_mod["N20 [gN/h]"]*1000
u_df_2_mod["Time []"] = pd.to_datetime(u_df_2_mod["Time []"])
u_df_2_mod = u_df_2_mod[c]

u_df_3_mod = u_df_3.rename(columns = {"inflow_SB3 [l/s]" : "inflow [l/s]", "NO2_SB3 [gN/m3]": "NO2 [gN/m3]" , "DO_SB3 [gO2/l]" : "O2 [gO2/m3]","Time [-]":"Time []"                                     
                                       ,"N2O_SB3 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB3 [gN/m3]":"NH4 [gN/m3]"})
u_df_3_mod["O2 [gO2/m3]"] = u_df_3_mod["O2 [gO2/m3]"]*1000
u_df_3_mod["N20 [gN/h]"] = u_df_3_mod["N20 [gN/h]"]*1000
u_df_3_mod["Time []"] = pd.to_datetime(u_df_3_mod["Time []"])
u_df_3_mod = u_df_3_mod[c]

u_df_4_mod = u_df_4.rename(columns = {"inflow_SB4 [l/s]" : "inflow [l/s]", "NO2_SB4 [gN/m3]": "NO2 [gN/m3]" 
                                      , "DO_SB4 [gO2/l]" : "O2 [gO2/m3]","Time [-]":"Time []"                                      ,"N2O_SB4 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB4 [gN/m3]":"NH4 [gN/m3]"})
u_df_4_mod["O2 [gO2/m3]"] = u_df_4_mod["O2 [gO2/m3]"]*1000
u_df_4_mod["N20 [gN/h]"] = u_df_4_mod["N20 [gN/h]"]*1000
u_df_4_mod["Time []"] = pd.to_datetime(u_df_4_mod["Time []"])
u_df_4_mod = u_df_4_mod[c]

u_df_5_mod = u_df_5.rename(columns = {"inflow_SB5 [l/s]" : "inflow [l/s]", "NO2_SB5 [gN/m3]": "NO2 [gN/m3]" ,
                                       "DO_SB5 [gO2/l]" : "O2 [gO2/m3]","Time [-]":"Time []", "N2O_SB5 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB5 [gN/m3]":"NH4 [gN/m3]"})
u_df_5_mod["O2 [gO2/m3]"] = u_df_5_mod["O2 [gO2/m3]"]*1000
u_df_5_mod["N20 [gN/h]"] = u_df_5_mod["N20 [gN/h]"]*1000
u_df_5_mod["Time []"] = pd.to_datetime(u_df_5_mod["Time []"])
u_df_5_mod = u_df_5_mod[c]

u_df_6_mod = u_df_6.rename(columns = {"inflow_SB6 [l/s]" : "inflow [l/s]", 
                                      "NO2_SB6 [gN/m3]": "NO2 [gN/m3]" , "DO_SB6 [gO2/l]" : "O2 [gO2/m3]",
                                      "Time [-]":"Time []"
                                      ,"N2O_SB6 [kgN/h]": "N20 [gN/h]",
                                      "NH4_SB6 [gN/m3]":"NH4 [gN/m3]"})
u_df_6_mod["O2 [gO2/m3]"] = u_df_6_mod["O2 [gO2/m3]"]*1000
u_df_6_mod["Time []"] = pd.to_datetime(u_df_6_mod["Time []"])
u_df_6_mod["N20 [gN/h]"] = u_df_6_mod["N20 [gN/h]"]*1000
u_df_6_mod = u_df_6_mod[c]


with open('data/uster_data.csv') as f:
    encoding = f.encoding
l_df_1 = pd.read_csv("data/modified/lucerne_1.csv", encoding = encoding)
l_df_2 = pd.read_csv("data/modified/lucerne_2.csv", encoding = encoding)

l_df_1_mod = l_df_1.rename(columns = {"Qin_1 [l/s]" : "inflow [l/s]", "NO2_1 [mgNO_2^-/m^3]": "NO2 [gN/m3]" , 
                                      "O2mid_1 [gO_2/m^3]" : "O2 [gO2/m3]",
                                      "F_N2O_lane_1 [gN_2O-N/h]":"N20 [gN/h]" ,"NH4mid_1 [gNH_4^+-N/m^3]":"NH4 [gN/m3]" })
l_df_1_mod["NO2 [gN/m3]"] = l_df_1_mod["NO2 [gN/m3]"]*0.001
l_df_1_mod["Time []"] = pd.to_datetime(l_df_1_mod["Time []"])
l_df_1_mod = l_df_1_mod[c]

l_df_2_mod = l_df_2.rename(columns = {"Qin_2 [l/s]" : "inflow [l/s]", "NO2_2 [mgNO_2^-/m^3]": "NO2 [gN/m3]" 
                                      , "O2mid_2 [gO_2/m^3]" : "O2 [gO2/m3]"
                                      ,"F_N2O_lane_2 [gN_2O-N/h]":"N20 [gN/h]" ,"NH4mid_2 [gNH_4^+-N/m^3]":"NH4 [gN/m3]"})
l_df_2_mod["NO2 [gN/m3]"] = l_df_2_mod["NO2 [gN/m3]"]*0.001
l_df_2_mod["Time []"] = pd.to_datetime(l_df_2_mod["Time []"])
l_df_2_mod = l_df_2_mod[c]

u_df_1_mod.to_csv("data/with_selected_variables/uster_1.csv")
u_df_2_mod.to_csv("data/with_selected_variables/uster_2.csv")
u_df_3_mod.to_csv("data/with_selected_variables/uster_3.csv")
u_df_4_mod.to_csv("data/with_selected_variables/uster_4.csv")
u_df_5_mod.to_csv("data/with_selected_variables/uster_5.csv")
u_df_6_mod.to_csv("data/with_selected_variables/uster_6.csv")

l_df_1_mod.to_csv("data/with_selected_variables/lucerne_1.csv")
l_df_2_mod.to_csv("data/with_selected_variables/lucerne_2.csv")

