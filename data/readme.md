
# Data description
Data_Description.pdf contains detailed information on the data and graphical overviews of the WWTPs.

## Altenrhein WWTP

The data was collected during a monitoring campaign at Altenrhein WWTP from 2015-12-04 to 2017-03-16.

Altenrhein_MonitoringData.csv contains data with a 20 minute resolution of variables assessed for the N2O monitoring campaign.The data was either acquired either via the plants SCADA system or during the monitoring campaign by the study&#39;s authors. Weekly control measurements were conducted by the plant operators for the sensors connected to the SCADA system.

Altenrhein_LabData.csv contains daily average values measured by the plants by the plant operators at least twice a week.

_Table 1 Data description of Altenrhein WWTP monitoring campaign_

| **Code** | **Description** | **Unit** | **Origin of data** | **Sensor** |
| --- | --- | --- | --- | --- |
| **Altenrhein_MonitoringData.csv** |
| N2O\_1 | N<var><sub>2</sub></var>O emissions on lane 1 | _gN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| N2O\_2 | N<var><sub>2</sub></var>O emissions on lane 2 | _gN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| Exp\_mode | Experiment with no dosage of reject water on lane 1 (0= normal operation, 1= experiment active) | _-_ | Monitoring campaign |
 |
| O2\_1 | Dissolved oxygen concentration in lane 1 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| O2\_2 | Dissolved oxygen concentration in lane 2 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| Inflow\_1 | Influent flow rate to lane 1 | _l/s_ | SCADA system | - |
| Inflow\_2 | Influent flow rate to lane 2 | _l/s_ | SCADA system | - |
| Temperature | Wastewater temperature in the inflow | _°C_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| **Altenrhein_LabData.csv** |
| Influent\_tot| Total influent to the Wastewater treatment plant | _m<var><sup>3</sup></var>/d_ | SCADA system | - |
| Influent\_Bio| Influent to the activated sludge reactors (rest goes to the fixed bed) | _m<var><sup>3</sup></var>/d_ | SCADA system | - |
| COD\_in | COD concentration in the wastewater after primary sedimentation | _gCOD/m__3_ | Lab Measurement | Hach, LDO sc |
| Ntot\_in | Total nitrogen concentration in the wastewater after primary sedimentation | _gN/m__3_ | Lab Measurement | Hach, LCK314 |


## Lucerne WWTP

The data was collected during a monitoring campaign at Lucerne WWTP from 2014-03-07 to 2015-10-31.

Lucerne_MonitoringData.csv contains daily average, sum and maximum values of variables assessed for the N2O monitoring campaign. The data was either acquired via the plants SCADA system, through lab measurements by the operators or during the monitoring campaign by the study&#39;s authors. Weekly control measurements were conducted by the plant operators for the sensors connected to the SCADA system.

Lucerne_LabData.csv contains daily average values measured by the plants by the plant operators at least twice a week.

_Table 2 Data description Lucerne WWTP monitoring campaign_

| **Code** | **Description** | **Unit** | **Origin of data** | **Sensor** |
| --- | --- | --- | --- | --- |
| **Lucerne_MonitoringData.csv** |
| F\_N2O\_lane\_1 | N<var><sub>2</sub></var>O emissions on the main aeration of lane 1 | _gN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| F\_N2O\_ post\_1 | N<var><sub>2</sub></var>O emissions on the post aeration of lane 1 | _gN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| Qin\_1 | Influent to lane 1 | _l/s_ | SCADA system | - |
| NH4\_1 | Ammonium concentration in the main aeration of lane 1 | _gNH<var><sub>4</sub><sup>+</sup></var>-N/m<var><sup>3</sup></var>_  | SCADA system | Endress+Hauser, ISEmax CAS40D |
| NO2\_1 | Nitrite concentration in the main aeration of lane 1 | _gNO<var><sub>2</sub></var><var><sup>-</sup></var>-N/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Liquiline System CA80NO |
| O2\_mid\_1 | Dissolved oxygen concentration in the main aeration of lane 1 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| O2\_post\_1 | Dissolved oxygen concentration in the post aeration of lane 1 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| TSS\_1 | Total solids concentration of lane 1 | _kgTS /m__3_ | SCADA system | Endress+Hauser, Turbimax CUS51D |
| F\_N2O\_lane\_2 | N<var><sub>2</sub></var>O emissions on lane 2 | _gN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| Qin\_2 | Influent to lane 2 | _l/s_ | SCADA system | - |
| NH4\_2 | Ammonium concentration in the main aeration of lane 2 | _gNH<var><sub>4</sub><sup>+</sup></var>-N/m<var><sup>3</sup></var>_  | SCADA system | Endress+Hauser, ISEmax CAS40D |
| NO2\_2 | Nitrite concentration in the main aeration of lane 2 | _gNO<var><sub>2</sub></var><var><sup>-</sup></var>-N/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Liquiline System CA80NO |
| O2\_mid\_2 | Dissolved oxygen concentration in the main aeration of lane 2 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| O2\_post\_2 | Dissolved oxygen concentration in the post aeration of lane 2 | _gO<var><sub>2</sub></var> /m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Oxymax COS61D |
| TSS\_2 | Total solids concentration of lane 2 | _kgTS /m<var><sup>3</sup></var>_ | SCADA system | Endress+Hauser, Turbimax CUS51D |
| **Lucerne\_Data\_Lab.csv** |
| Influent\_tot| Total influent to the Wastewater treatment plant | _m<var><sup>3</sup></var>/d_ | SCADA system | - |
| Influent\_lane1| Influent to lane 1 | _m<var><sup>3</sup></var>/d_ | SCADA system | - |
| COD\_in | COD concentration in the wastewater after primary sedimentation | _gO<var><sub>2</sub></var>_/m<var><sup>3</sup></var> | Lab Measurement | Hach, LDO sc |
| Ntot\_in | Total nitrogen concentration in the wastewater after primary sedimentation | _gN/m<var><sup>3</sup></var>_ | Lab Measurement | Hach, LCK314 |
| NH4\_in | Ammonium concentration in the wastewater after primary sedimentation | _gN/m<var><sup>3</sup></var>_ | Lab Measurement | Hach, LCK303 |


## Uster WWTP

The data was collected during a monitoring campaign at Uster WWTP from 2018-04-01 to 2019-06-01.

Uster_MonitoringData.csv contains data with a 20 minute resolution of variables assessed for the N2O monitoring campaign. The data was either acquired either via the plants SCADA system or during the monitoring campaign by the study&#39;s authors. Bi-weekly control measurements were conducted by the plant operators for the sensors connected to the SCADA system.

Uster_LabData.csv contains daily average values measured by the plants by the plant operators at least twice a week.

In the following table, &quot;\_SBX&quot; is a substitute for &quot;\_SB1&quot; to &quot;\_SB6&quot;. The endings indicate which sequencing batch reactor (SBR) the data is assigned to.

_Table 3 Data description Uster WWTP monitoring campaign_

| **Code** | **Description** | **Unit** | **Origin of data** | **Sensor** |
| --- | --- | --- | --- | --- |
| **Uster_MonitoringData.csv** |
| inflow\_SBX | Influent flow rate to SBR 1-6 | _l/s_ | _SCADA_ | _-_ |
| NH4\_load\_SBX | Ammonium load in the influent to SBR 1-6 | _gNH<var><sub>4</sub><sup>+</sup></var>-N/h_ | _SCADA_ | Endress+Hauser, ISEmax CAS40D |
| NH4\_SBX | Ammonium concentration in SBR 1-6 | _gNH<var><sub>4</sub><sup>+</sup></var>-N/m<var><sup>3</sup></var>_ | _SCADA_ | Endress+Hauser, ISEmax CAS40D |
| NO3\_SBX | Nitrate concentration in SBR 1-6 | _gNH<var><sub>4</sub><sup>+</sup></var>-N/m<var><sup>3</sup></var>_| _SCADA_ | Endress+Hauser, ISEmax CAS40D |
| NO2\_SBX | Nitrite concentration in SBR 1-6 | _gNO<var><sub>2</sub></var>-N/m<var><sup>3</sup></var>_ | _SCADA_ | Opus, Trios, Rastede, DE |
| TS\_SBX | Total solids concentration in SBR 1-6 | _kgTS /m<var><sup>3</sup></var>_ | _SCADA_ | Endress+Hauser, Turbimax CUS51D |
| DO\_SBX | Dissolved oxygen concentration in SBR 1-6 | _gO<var><sub>2</sub></var>/m<var><sup>3</sup></var>_ | _SCADA_ | Endress+Hauser, Oxymax COS61D |
| airflow\_SBX | Airflow into SBR 1-6 | _m<var><sup>3</sup></var>/h_ | _SCADA_ | _-_ |
| level\_SBX | Water level in SBR 1-6 | _m_ | _SCADA_ | Endress+Hauser, Oxymax COS61D |
| temp\_SBX | Water temperature in SBR 1-6 | _°C_ | _SCADA_ | Endress+Hauser, Oxymax COS61D |
| pH\_SBX | pH value in SBR 1-6 | _-_ | _SCADA_ | Endress+Hauser, Orbisint CPS11D |
| O2\_Offgas\_SBX | Dissolved oxygen concentration in offgas from SBR 1-6 | _%_ | Monitoring campaign | Emerson Xstream |
| N2O\_SBX | Nitrous oxide emissions from SBR 1-6 | _kgN<var><sub>2</sub></var>O-N/h_ | Monitoring campaign | Emerson Xstream |
| **Uster_LabData.csv** |
| Influent | Total influent to the SBR reactors | _m<var><sup>3</sup></var>/d_ | SCADA system | - |
| COD\_in | COD concentration in the wastewater after primary sedimentation | _gO<var><sub>2</sub></var>_/m<var><sup>3</sup></var> || Lab Measurement | Hach, LDO sc |
| Ntot\_in | Total nitrogen concentration in the wastewater after primary sedimentation | _gN/m<var><sup>3</sup></var>_ | Lab Measurement | Hach, LCK303 |
| NH4\_in | Ammonium concentration in the wastewater after primary sedimentation | _gN/m<var><sup>3</sup></var>_ | Lab Measurement | Hach, LCK314 |



