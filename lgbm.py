import sklearn
import lightgbm as lgb
from sklearn.metrics import f1_score
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
#无缺失数据
print(11111)
#超参数1
lgb_ne = lgb.LGBMClassifier(loss_function='MultiClass',class_weight={0:1,1:2.7,2:4.3})
param_dist={'n_estimators':[100,200,500,1000],
            'learning_rate':[1,0.1,0.01,0.001,0.0001]} 

grid_search = GridSearchCV(lgb_ne, param_grid=param_dist, cv = 5,verbose=10, 
                           n_jobs=-1,scoring='f1_macro')

grid_search.fit(traindfscale,ship_type)
grid_search.best_estimator_
grid_search.best_score_
#超参数2
lgb_ne = lgb.LGBMClassifier(class_weight={0:1,1:2.7,2:4.3},loss_function='MultiClass',n_estimators=1000,learning_rate=0.1)
param_dist={'max_depth':[-1,5,10,15,20],
            'num_leaves':[10,30,50,100]}

grid_search = GridSearchCV(lgb_ne, param_grid=param_dist, cv = 5,verbose=10, 
                           n_jobs=-1,scoring='f1_macro')

grid_search.fit(traindfscale,ship_type)
grid_search.best_estimator_
grid_search.best_score_
 
################
lgb_ne = lgb.LGBMClassifier(class_weight={0:1,1:2.7,2:4.3},loss_function='MultiClass',
                            n_estimators=1000,learning_rate=0.1,
                            max_depth=-1,num_leaves=31)

lgb_ne.fit(traindfscale,ship_type)

ship_type_test=lgb_ne.predict(testdfscale)
ship_type_test=list(ship_type_test)

for i in range(len(ship_type_test)):
    if ship_type_test[i]==0:ship_type_test[i] = '拖网'
    if ship_type_test[i]==1:ship_type_test[i] = '围网'
    if ship_type_test[i]==2:ship_type_test[i] = '刺网'

result=pd.DataFrame(ship_type_test,columns=['type'])
shipidtest=pd.DataFrame(ship_id_test,columns=['id'])
final=pd.concat([shipidtest,result],axis=1)
final.to_excel(r'C:\Users\MR\Desktop\resultscale.xlsx',index=False)
##################################################################################
