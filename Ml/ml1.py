#분류 classifiter

#붓꽃 품종 분류
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from sklearn.datasets import load_iris



iris = load_iris()
#print(iris.DESCR)

#데이터 뽑기
data = iris.data
label = iris.target
# print(data.shape)
# print(label.shape)
# print(label)

name = iris.target_names
#print(name)
train_data, test_data, train_label, test_label =\
    train_test_split(data,label,test_size=0.3,random_state=0)
    
svc=SVC()
# model= svc.fit(train_data,train_label)
# print(model.score(train_data,train_label))
# print(model.score(test_data,test_label))
#
# fig = plt.figure(figsize=(10,5))
# colors = np.array(["red","green","blue"])
# ax1 = fig.add_subplot(1,2,1)
# ax1.scatter(data[:,2],data[:,3],color=colors[label],alpha=0.5)
#
# predicts = model.predict(data)
# ax2 = fig.add_subplot(1,2,2)
# ax2.scatter(data[:,2],data[:,3], color=colors[predicts], alpha=0.5)
# plt.show()


#k겹 교차 검증
from sklearn.model_selection import cross_val_score
scores = cross_val_score(svc,data, label, cv=3)
print(scores)
print(scores.mean())

#데이터가 쏠려있는 것을 방지하기위해 쓰는것
# K겹 교차 검증
from sklearn.model_selection import cross_val_score
scores = cross_val_score( svc, data, label, cv=3 )
print( scores )
print( scores.mean() )

# K-Fold
from sklearn.model_selection import KFold
kfold = KFold( n_splits=3, shuffle=True, random_state=0 )
scores = cross_val_score( svc, data, label, cv=kfold )
print( scores )
print( scores.mean() )

# 모델 최적화
from sklearn.model_selection import GridSearchCV
params = [
    { "C":[1, 10, 100, 1000], "kernel":["linear"] },
    { "C":[1, 10, 100, 1000], "kernel":["rbf"], "gamma":[0.001, 0.0001] }
    ]
gs = GridSearchCV( SVC(), params, n_jobs=1 )
models = gs.fit( data, label )
# print( models.cv_results_ )
print( models.best_score_ )
print( models.best_params_ )
model = models.best_estimator_ 
predict = model.predict( [[2.3, 2.5, 4.7, 5.5]] )
print( name[ predict ] )


from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
params = { "C": randint(1, 100) }
rs =RandomizedSearchCV( SVC(), param_distributions=params, cv=5, n_iter=100, return_train_score=True )
models = rs.fit( data, label )
# print( models.cv_results_ )
print( models.best_score_ )
print( models.best_params_ )


#로지스틱 회귀
data = np.array( [[8,8], [7,5], [6,8], [9,3], [7,2],
        [5,4], [5,6], [7,3], [9,7], [7,8],
        [6,6], [6,9], [3,2], [3,6], [5,3],
        [6,1], [5,4], [5,5], [9,7], [9,9],
        [9,9], [9,6], [8,4], [8,8], [7,7],
        [9,3], [3,9], [8,1], [8,7], [7,9]] )
label = np.array( [ 1, 0, 0, 0, 0, 
          0, 0, 0, 1, 1,
          0, 1, 0, 0, 0, 
          0, 0, 0, 1, 1,
          1, 1, 0, 1, 0,
          0, 0, 0, 1, 1] )

train_data, test_data, train_label, test_label = \
    train_test_split( data, label, test_size=0.3, random_state=1 )

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
model = lr.fit( train_data, train_label )
print( model.score( train_data, train_label ) )
print( model.score( test_data, test_label ) )    

print(model.predict([[7,8]]))
print(model.predict([[6,8]]))

from sklearn import metrics
predicts = model.predict(data)

score = metrics.accuracy_score(predicts, label)
print("정답률 :" , score)

score = metrics.accuracy_score(predicts, label)
print("정밀도 :", score)   #양성 맞춘 개수 / 전체 양성 개수
score = metrics.recall_score(predicts, label)
print("재현율 :", score)   #양성 맞춘 개수 / 전체 양성 개수

score = metrics.f1_score(predicts, label)
print("f1-score :", score)

score = metrics.roc_auc_score(predicts, label)
print("auc : ", score)

score = metrics.classification_report(predicts, label)
print("classification :", score)
