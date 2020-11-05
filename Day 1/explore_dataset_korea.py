import numpy as np
import pandas as pd
import matplotlib as plt

# data loading
# %% code
data_path="C:\\100daysOfMLcode\south_korea_dataset\\"
names=["Case.csv" ,"patientInfo.csv","Policy.csv","Region.csv","SearchTrend.csv","SeoulFloating.csv","Time.csv","TimeAge.csv","TimeGender.csv","TimeProvince.csv","Weather.csv"]
caseName,patientInfo,policy,region,searchTrend,seoulFloating,time,timeAge,timeGender,timeProvince,weather=names[0],names[1],names[2],names[3],names[4],names[5],names[6],names[7],names[8],names[9],names[10]
# %% code

df_case=pd.read_csv(data_path+caseName)
df_case.head()
# %% code
df_patient_info=pd.read_csv(data_path+patientInfo)
df_patient_info.head()
# %% code
df_policy=pd.read_csv(data_path+policy)
df_policy.head()
# %% code
df_region=pd.read_csv(data_path+region)
df_region.head()

# %% code
df_search_trend=pd.read_csv(data_path+searchTrend)
df_search_trend.head()
# %% code
df_seoul_floating=pd.read_csv(data_path+seoulFloating)
df_seoul_floating.head()
# %% code
df_time=pd.read_csv(data_path+time)
df_time.head()
# %% code
df_time_age=pd.read_csv(data_path+timeAge)
df_time_age.head()
# %% code
df_time_gender=pd.read_csv(data_path+timeGender)
df_time_gender.head()
# %% code
df_time_province=pd.read_csv(data_path+timeProvince)
df_time_province.head()
# %% code
df_weather=pd.read_csv(data_path+weather)
df_weather.head()
all_dfs=[df_case,df_patient_info,df_policy,df_region,df_search_trend,df_seoul_floating,df_time,df_time_age,df_time_gender,df_time_province,df_weather]
for i in range(len(all_dfs)):
    df=all_dfs[i]
    no_of_rows=df.count()
    print("Some random stats from each df \n \n ")
    print("df no : " + str(i) + "   name:   " + names[i])
    print('no of rows: ' + str(no_of_rows))
