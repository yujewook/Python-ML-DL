import numpy as np
import pandas as pd

df = pd.DataFrame(
    [["you",89,92,95],
     ["kim",46,np.NaN,65],
     ["lee",32,np.NaN,30],
     ["park",np.NaN,np.NaN,30],
     ["kang",np.NaN,10,np.NaN]
     ] , columns=["name","kor","eng","mat"]
    
    )

print(df.info())
print(df.describe())
print(df.count(axis=1))
print(df.sum)
print(df[["kor","eng","mat"]].sum(axis=1))
print(df)

print (df.min())
print(df.min(axis=1)) # 숫자중에서 계산해야 한다
print(df.max()) 
print(df.max(axis=1)) 

print(df.mean()) #평균구하는 것
print(df.mean(axis=1)) #평균구하는 것 열끼리


print("-"*50)

#세로 한줄 다 구하기 합을 구해주기
df["tot"] = df.sum(axis=1)
#몇과목 합
df["tot1"] = df[["kor","eng","mat"]].sum(axis=1)

#평균 구하기
df["avg"] = df.loc[:,"kor":"mat"].mean(axis=1)

print(df.median()) #전체 중간값
print("-"*50)
print(df.median(axis=1))
print("-"*50)
print(df.mad())                #편차
print("-"*50)
print(df.var())                #분산 (제곱의 합)
print("-"*50)
print(df.var(axis=1))
print("-"*50)
print(df.std())                #표준편차
print("-"*50)
print(df.cumsum)               #누적값 구하는것
print("-"*50)
print(df.loc[:,"kor":"mat"].cumprod())            #누적곱 다계산하면 에러
print("-"*50)
print(df.loc[:,"kor":"mat"].idxmax())
print("-"*50)
print(df.loc[:,"kor":"mat"].idxmin())
print("-"*50)

print(df["kor"].corr(df["eng"]))
print(df["kor"].corr(df["avg"]))
print(df["mat"].corr(df["avg"]))
print(df["eng"].corr(df["avg"]))

print(df["kor"].cov(df["avg"])) #높은 술자 일수록평균에 영향을 미치는 것이 가장 높다
print(df["mat"].cov(df["avg"]))
print(df["eng"].cov(df["avg"]))

print("-"*50)

#sort하는 방법
print(df.sort_index(ascending=False)) #인덱스로 내림차순
print("-"*50)
print(df.sort_index(axis=1 )) #열로 정렬

print("-"*50)
#sort values는 정렬이 꼭들어 가야한다(by="kor") 이게 들어 가야한다.
print(df.sort_values(by="kor"))
#print(df.sort_values(by="kor", axis=1)) #에러

print(df["kor"].unique() )
print(df["kor"].value_counts() )
print(df["kor"].isin([40,50,60,70]) ) # 이 값이 포함되어 있냐?

#열을 골라내는 것을 하면됨
print(df.loc[df["kor"].isin([46,56,66,76]),"kor":"mat"])



print("-"*50)
print(df)

print("-"*50)

df = pd.DataFrame(np.random.rand(4,3),columns=["A","B","C"], 
                  index=["kim","lee","hong","park"])
print(df)


print("-"*50)

#데이터 프레임에 전부 다 적용하고 싶을때  -> 함수로 만든다
def func(x): #데이터 한줄씩 받는다 행이던 열이던 한줄 씩 데이터 여러개
    return x.max() - x.min()
    
print(df.apply(func))           # 행끼리 연산해서 계산값 나오게 하기
print("-"*50)
print(df.apply(func,axis=1))    #열끼리 계산해라
print("-"*50)
#람다 함수로 구해보기
print(df.apply( lambda x : x.max() - x.min() , axis=1))


###pandas Plot ###
np.random.seed(0)
df = pd.DataFrame(np.random.rand( 100,3 ) , index=pd.date_range("9/1/2022",periods=100),
                  columns=["A","B","C"] ).cumsum()

#맨밑에 5개를 나오게하는 함수 tail()
print(df.tail())
print("-"*50)
import matplotlib.pyplot as plt

# df.plot()
#
# #표에서 라벨 붙이는 것
# plt.xlabel("TIME")
# plt.ylabel("Value")
# plt.title("PLOT")
#
# plt.show()

import seaborn as sns

iris = sns.load_dataset("iris") #북꽃의 데이터
titanic = sns.load_dataset("titanic")

#print(iris)
#iris["sepal_length"].plot(kind="bar",rot=0) #전체
#iris["sepal_length"][:20].plot(kind="bar",rot=0) #부분
#plt.show()

#iris[:5].plot(kind="bar")
# iris[:5].plot.bar()
# plt.show()

#iris[:5].plot(kind="barh") #옆으로 나오는 바
#plt.show()


#   타이타닉데이터 pclass의 데이터 
#df = titanic.pclass.value_counts()
#print(df)
#            자동퍼센트 만들기 .2f 소수점 둘쨰 %% %를 찍히게 하기 
#df.plot.pie( autopc="%.2f%%")
#plt.show()

#iris.hist()
#plt.show()

#밀도
# iris.plot.kde()
# plt.show()

iris.plot.box()
plt.show()





