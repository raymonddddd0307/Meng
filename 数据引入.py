import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
df=pd.DataFrame()
speed_mean=[]
speed_25=[]
speed_75=[]
speed_var=[]
speed_max=[]
direction_mean=[]
direction_var=[]
x_ave=[]
x_max=[]
x_min=[]
x_range=[]
x_var=[]
y_ave=[]
y_max=[]
y_min=[]
y_range=[]
y_var=[]
xy_cov=[]
time=[]
ship_id=[]
ship_type=[]

for i in range(len(os.listdir(r'C:\Users\MR\Desktop\train'))):#文件名
    domain = os.path.abspath(r'C:\Users\MR\Desktop\train') #获取文件夹的路径
    info=os.listdir(r'C:\Users\MR\Desktop\train')[i]
    info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径
    data = pd.read_csv(info)
    speed_mean.append(data.iloc[:,3].mean())
    speed_25.append(data.iloc[:,3].quantile(0.25))
    speed_75.append(data.iloc[:,3].quantile(0.75))
    speed_var.append(data.iloc[:,3].var())
    speed_max.append(data.iloc[:,3].max())
    direction_mean.append(data.iloc[:,4].mean())
    direction_var.append(data.iloc[:,4].var())
    x_ave.append(data.iloc[:,1].mean())
    x_max.append(data.iloc[:,1].max())
    x_min.append(data.iloc[:,1].min())
    x_range.append(data.iloc[:,1].max()-data.iloc[:,1].min())
    x_var.append(data.iloc[:,1].var())
    y_ave.append(data.iloc[:,2].mean())
    y_max.append(data.iloc[:,2].max())
    y_min.append(data.iloc[:,2].min())
    y_range.append(data.iloc[:,2].max()-data.iloc[:,2].min())
    y_var.append(data.iloc[:,2].var())
    xy_cov.append(np.correlate(data.iloc[:,1],data.iloc[:,2]))
    time.append(data.shape[0])
    ship_id.append(data.iloc[0,0])
    ship_type.append(data.iloc[0,6])
    
   # df=pd.concat([df,data],axis=0)
    print(i)

for i in range(len(ship_type)):
    if ship_type[i] == '拖网':ship_type[i]=0
    if ship_type[i] == '围网':ship_type[i]=1
    if ship_type[i] == '刺网':ship_type[i]=2

shiptrain={'speed_max':speed_max,
           'speed_25':speed_25,
           'speed_75':speed_75,
           'speed_mean':speed_mean,
           'speed_var':speed_var,
           'direction_mean':direction_mean,
           'direction_var':direction_var,
           'x_ave':x_ave,
           'x_max':x_max,
           'x_min':x_min,
           'x_range':x_range,
           'x_var':x_var,
           'y_ave':y_ave,
           'y_max':y_max,
           'y_min':y_min,
           'y_range':y_range ,
           'y_var':y_var,
           'xy_cov':xy_cov,            
           'time':time
           }
      
index=pd.Index(data=ship_id,name='ship_id')
traindf=pd.DataFrame(shiptrain,index=index) 
traindfscale= preprocessing.scale(traindf)  
ship_type    


####################################测试集#####################################

speed_mean_test=[]
speed_25_test=[]
speed_75_test=[]
speed_var_test=[]
speed_max_test=[]
direction_mean_test=[]
direction_var_test=[]
x_ave_test=[]
x_max_test=[]
x_min_test=[]
x_range_test=[]
x_var_test=[]
y_ave_test=[]
y_max_test=[]
y_min_test=[]
y_range_test=[]
y_var_test=[]
xy_cov_test=[]
time_test=[]
ship_id_test=[]
ship_type_test=[]

for i in range(len(os.listdir(r'C:\Users\MR\Desktop\test'))):#文件名
    domain = os.path.abspath(r'C:\Users\MR\Desktop\test') #获取文件夹的路径
    info=os.listdir(r'C:\Users\MR\Desktop\test')[i]
    info = os.path.join(domain,info) #将路径与文件名结合起来就是每个文件的完整路径
    data = pd.read_csv(info)
    speed_mean_test.append(data.iloc[:,3].mean())
    speed_25_test.append(data.iloc[:,3].quantile(0.25))
    speed_75_test.append(data.iloc[:,3].quantile(0.75))
    speed_var_test.append(data.iloc[:,3].var())
    speed_max_test.append(data.iloc[:,3].max())
    direction_mean_test.append(data.iloc[:,4].mean())
    direction_var_test.append(data.iloc[:,4].var())
    x_ave_test.append(data.iloc[:,1].mean())
    x_max_test.append(data.iloc[:,1].max())
    x_min_test.append(data.iloc[:,1].min())
    x_range_test.append(data.iloc[:,1].max()-data.iloc[:,1].min())
    x_var_test.append(data.iloc[:,1].var())
    y_ave_test.append(data.iloc[:,2].mean())
    y_max_test.append(data.iloc[:,2].max())
    y_min_test.append(data.iloc[:,2].min())
    y_range_test.append(data.iloc[:,2].max()-data.iloc[:,2].min())
    y_var_test.append(data.iloc[:,2].var())
    xy_cov_test.append(np.correlate(data.iloc[:,1],data.iloc[:,2]))
    time_test.append(data.shape[0])
    ship_id_test.append(data.iloc[0,0])
    
   # df=pd.concat([df,data],axis=0)
    print(i)

shiptraintest={'speed_max_test':speed_max_test,
               'speed_25_test':speed_25_test,
               'speed_75_test':speed_75_test,
               'speed_mean_test':speed_mean_test,
               'speed_var_test':speed_var_test,
               'direction_mean_test':direction_mean_test,
               'direction_var_test':direction_var_test,
               'x_ave_test':x_ave_test,
               'x_max_test':x_max_test,
               'x_min_test':x_min_test,
               'x_range_test':x_range_test,
               'x_var_test':x_var_test,
               'y_ave_test':y_ave_test,
               'y_max_test':y_max_test,
               'y_min_test':y_min_test,
               'y_range_test':y_range_test,
               'y_var_test':y_var_test,
               'xy_cov_test':xy_cov_test,
               'time_test':time_test
               }
      
index_test=pd.Index(data=ship_id_test,name='ship_id_test')
testdf=pd.DataFrame(shiptraintest,index=index_test)    
testdfscale=preprocessing.scale(testdf)
   


