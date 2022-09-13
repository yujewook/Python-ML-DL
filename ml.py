#반증법에 의한 증명


#대립가설 -> 증명하고 싶은게 가설 
#학생들의 키는 평균키는 175다 -> 증명 하고 싶은 가설


#귀무가설
#학생들의 평균키는 175가 아니다.


import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection._split import train_test_split

np.random.seed( 1 ) 

np.random.seed(1)
#height = [180  + np.random.normal(0,5) for i in range(10000)]    #0.05 이하 귀무가설 채택 ->  대립가설 기각 평균이 180인 데이터이다
# height = [175  + np.random.normal(0,5) for i in range(10000)]   #0.05 이상  귀무가설 기각 대립가격 채택
# result=stats.ttest_1samp(height,175)                            # 현재 175인지 증명 하는 것
#
# print(result)

#피어슨 상관관계 분석 
# df = pd.DataFrame(
#         {
#             "a" : [i*100 for i in range(100)],
#             "b" : [i*-100 for i in range(100)],
#             "c" : [i*np.random.randint(1,100) for i in range(100)]
#
#         }
#     )
# # df.plot()
# # plt.show()
#
# corr = df.corr( method="pearson" )
# print( corr )
# sns.heatmap( corr, annot=True, annot_kws={"size":20}, fmt=".2f" )
# plt.show()



#머신러닝 분석
from sklearn import svm
#지도 학습 정답을 주고 분석해야한다

# # 정답은 무조건 2차원
# data =[[0,0],[0,1],[1,0],[1,1]]
# #라벨은 일차원
# label = [0,1,1,0]
#
# #알고리즘
# svc = svm.SVC()
#
# #학습시키는 함수
# model = svc.fit( data,label ) 
# print(model.predict([[0,1]])) # 답이 일 
#
# label = [0,0,0,1]
# model = svc.fit(data,label)
# print(model.predict([[0,1]]))
#
# label = [0,1,1,1]
# model = svc.fit(data,label)
# print(model.predict([[0,1]]))
#
# data=[[0,0],[0,1],[1,0],[1,1],[0,0],[0,1],[1,0],[1,1]]
# label=[0,0,0,1,0,0,0,1]
# svc= svm.SVC()
#
# model=svc.fit(data,label)
# print(model.score(data,label))




# 회귀Regression 
# x = [2.42,2.56,3.31,4.62,3.98,4.9,3.67,3.7,3.45,2.5]        #생산량(독립변수)
# y = [2.56,4.5,3,4.2,3.54,4.78,4.59,3.71,2.65,3.98]      #소비량(종속변수)
#
# # 가장 적합한 선 찾아주기
# result = stats.linregress(x, y)
# #print(result)
#
# slope , intercept , rvalue, pvalue , stderr = result
#
# # xx = np.array(x)
# # plt.scatter(xx, y)
# # plt.plot(xx, slope * xx + intercept,"r" ) #일차 함수 구하기 => 선형에 가장 가까운것
# # plt.show()
#
# print(slope*4.0 + intercept)

# 오존량 분석
ozone = pd.read_csv( "ozone.csv" )
#데이터 확인
#print( ozone.describe() )
#print( ozone.count() )
#print(ozone.shape)
#print(ozone.head())

#기본값이 any 
ozone = ozone.dropna(axis=0) #행단위로 지워라
#print(ozone.count()) na값 없애기

#독립변수 알고 있는것
#x = ozone["Temp"].values #오존과 바람의 선형(y값은 안함)
#x = ozone["Wind"].values # 오존과 바람 
x =ozone["Solar.R"].values # 오존과 태양광
#종속변수 알고 싶은것
y = ozone["Ozone"].values

result = stats.linregress(x, y)

#예측하기 
#print(80*result.slope + result.intercept)


# plt.scatter(x,y)
# plt.plot(x,result.slope*x+result.intercept,"r")
# plt.show()

# sns.heatmap( ozone.loc[:,"Ozone":"Temp"].corr(), annot=True )
# plt.show()

#다중 선형회귀 분석
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston = load_boston()

#print(boston)
data = boston.data
label = boston.target
# print(data.shape)
# print(label.shape)


train_data, test_data, train_label, test_label = \
    train_test_split(data, label, test_size=0.3, random_state=0)


lr = LinearRegression()

model = lr.fit(train_data,train_label)
print(model.score(train_data,train_label))
print(model.score(test_data,test_label))




















                                                        
                                                                                    