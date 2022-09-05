import numpy as np
from unittest.mock import inplace
#where
x = np. array([1, 2 , 3 , 4 ,5])
y = np. array( [6,7,8,9,10] )
z = np.array([True,False,True,False])
#     참일때결과 a 아니면 b를 쓴다.
print([ a if c else b for a,b,c in zip(x,y,z)]) # 이차원이상일땐 이렇게 안되고

#2차원 이상일때 numpy where를 사용한다
#               조건
#print( np.where( z , x , y) ) 
# True인걸 골라내서 사용한다

a = np.random.rand(4,4)
#print (a)
            # a가 0보다크면 1로 작으면 0 으로 바뀐다
print(np.where( a >0 ,1,0))
            # a가 0보다크면 1로 작으면  a로 바뀐다
print(np.where( a >0 ,1,a))

#파일 입출력
#리스트를 넣었다 뺐다하기
a = np.arange(10)
np.save("np1.npy",a)#저장 -> 새로운 파이 이 생간다
arr = np.load("np1.npy" ) #파일 사용하기
print(arr)

b = np.arange(10,20) #여러개 파일
#여러개 파일 저장하고 리스트이름 결정해놓기
np.savez("np2.npz",arr1=a,arr2=b)
c = np.load("np2.npz")
print(c["arr1"])
print(c["arr2"])




#### pandas
import pandas as pd

#series 1차원
#리스트와 numpy 호한이 된다
s= pd.Series( [1,0,8,-3,-6,9,3,-2,6,7 ] )
print(type(s))
#print(s)

print(s.index)

#자료형이 numpy가 된다 
print(s.values) 
print(type(s.values)) 
print(s.dtype)

s.index = ["a","b","c","d","e","f","g","h","i","j"]
print(s)

print(s.index)
print(s["a"])
print(s.a)
print(s[0:5]) # 인덱스 슬라이싱 데이터 까지 짤린다.
print(s["a":"e"]) #이름으로 슬라이싱 하기

#딕셔러리로 series 사용하기
#딕셔러리는 슬라이싱 , print(s.a) 불가하다. 
d = {"A":65,"B":66,"C":67,"D":68}
print(type(d))

print(d["A"])
#ERROR
#print(d.A)
#print(d[0:3])
#print(d["A":"C"])


for key, value in d.items():
    print(key,value)
#시리즈로 바꿔서 딕셔너리를 사용하게 하기
s = pd.Series(d)
print(s.index)
print(s.values)
print(s[0:3])
print(s["A":"C"])

# DataFrame
d = {
    "name":["kim","park","hong","lee"],
    "age":[20,30,40,25],
    "tel":["1111-1111","2222-2222","3333-3333","3333-1111"],
    }

df = pd.DataFrame(d)
print(df)

#여기서 출력해 볼 수 있는것

#인덱스
print(df.index)
#columns 컬럼
print(df.columns)
#valu es 값 numpy로 꺼낸다
print(df.values)

df.index.name="Num" #전체에다 이름을 붙인다
df.columns.name="User"
print(df)

print(df.index)
print(df.columns)


#np로 만들어주기
#컬럼도 없고 데이터만 있는 상태 -> 컬럼이 숫자로 나온다
n = np.array(
    [["kim",20,"1111-2222"],
     ["you",32,"2222-2222"],
     ["hong",26,"2222-2222"]]
    
)

#출력
df = pd.DataFrame(n)
print(df)
print(df.index)
print(df.columns)

#컬럼에 이름을 주는 방법 index랑 컬럼스 주는것
df.index = ["A","B","C"]
df.columns = ["name","age","tel"]
print(df)

df1 = pd.DataFrame(n,index=["a","b","c"],columns=["name","age","tel"])
print(df1)


print(df.info)
#전체적인 통계값을 나오게 하는것
print(df.describe())

result = df.describe()
print(result.index)
print(result.columns)


print("-"*50)


print(df)
print(df["name"])
#name에 a번째 값 
print(df1["name"]["a"])
print(df1["name"].a)
print(df1["name"][:2])

print("-"*50)

print(df1)

print("-"*50)
print(df1[["name","age"]])

print("-"*50)
#따로 따로 출력하기 원하면
print(df1.name,df1.age)

#데이터 잘라보기
print(df1[:][:])
print(df1[:2])
#print(df1[:2, :2]) 에러

#2행의 2열 numpy
print(df.values[:2,:2])

#데이터 추가하기 
#원래 값에 컬럼의 수는 맞춰야한다
df["address"] =["서울","수원","인천"]
df["adult"] =df["age"]>="30"
#데이터를 바꾸기
df["age"][0] =40
df["adult"][2] = True

#지울때
del(df["adult"])

#인덱스 이름 바꾸기
df.index=["A","B","C"]

print(df)


#데이터 프레임 정렬하기 sort하는 방법
print()

s = pd.Series(range(4),index=["b","d","a","c"])
s = s.sort_index(ascending=False) # 내림차순
s = s.sort_values() # 오름차순으로 값을 받아오는 것
print(s)

df = pd.DataFrame( np.arange(12).reshape( 3 , 4 ),
                  index=["b","c","a"],columns=["B","A","D","C"])
print("-"*50)
print(df)

df = df.sort_index()
print("-"*50)
print(df)

df = df.sort_index(axis=1)
print("-"*50)
print(df)
print("-"*50)

# 기준 값이 존재해야한다. 값을 기준으로 바꾼다
df =df.sort_values(by="A")
print(df)
print("-"*50)
# 기준 값이 존재해야한다. 값을 기준으로 바꾼다
df =df.sort_values(by="A" , ascending=False)
print(df)
print("-"*50)


df = df.sort_values(axis=1,by="a")
print(df)
print("-"*50)

df = df.sort_values(axis=1,by=["a","b"])

# loc iloc
print
m=[[1,2,3],[4,5,6],[7,8,9]]
print(m)
print(m[1][2])
print(m[0:2][0:2])
# print(m[0:2,0:2]) 에러

#numpy로 바꾸기
n = np.array(m)
print(n)
print(n[1][2])
print(n[0:2,0:2])

#dataFrame으로 데이터 꺼내 오기 
w = pd.DataFrame(m,index=["a","b","c"], columns=["A","B","C"])
print(w)
#      행 렬
#print(w[1][2]) # 행렬처럼 꺼내라 [컬럼][인덱스] 에러
print(w["A"][2])# 행렬처럼 꺼내라 [컬럼][인덱스]
print(w[0:2][0:2])# 행렬처럼 꺼내라 [컬럼][인덱스]
#print(w[0:2,0:2]) 에러

#iloc 숫자 loc는 이름
df =pd.DataFrame(np.arange(10,26).reshape(4,4), columns=["A","B","C","D"])
print(df)
# print(df[0][0]) 에러
print(df["A"][0]) #[컬럼][인덱스]
#print(df[["A","D"]]) 에러
print(df[["A","D"]])
print(df[["A","D"]][0:2]) #[컬럼][인덱스]
#print(df[["A",0:2]]) 에러

print("*"*50)
#print(df[1,1])에러
#print(df.loc[1,1]) 에러 loc는 이름을 줘야한다
print(df.iloc[1,1]) # 숫자로 줘도 된다.
#print(df.iloc[1,"A"]) #이름을 받는것은 에러가 난다
#print(df.iloc["A",1]) 에러 이름을 쓰면 그냥 에러

print(df.iloc[:2 , :2])
print(df.iloc[:2 , :-1])
print(df.iloc[:-1 , :-1])

#loc
print("**--**"*50)
print(df)
print(df[0:2]) #컬럼을 의미한다. -> 데이터프레임 자체
print(df[["A","C"]])
print(df.iloc[1,1])
print(df.iloc[2:,2:])

print(df.loc[1][1])

#print(df.loc[1][1])    #에러
#print(df["A",[1]])     #에러
print(df.loc[1]["A"])   #[1] 행렬에 [A]라는 값을 빼온다. [인덱스][컬럼]
print(df["A"][1])       #[컬럼][인덱스]
print(df.iloc[2][1])    #[인덱스][컬럼]

print(df.loc[:2  , :"B"])

print(df.loc["A":"C"])
#print(df.lic[:2]["A":"C"])#에러
print(df.loc[:,"A":"C"])
#print(df.loc[:2]["A":"C"])#에러
print(df.loc[:2][["A","B"]])

print()
df["E"] = [30,31,32,33]
df.loc[:,"F"] = [40,41,42,44]
df.loc[0,"A"] = 99 #위치지정 데이터 바꾸기
df.loc[3,["A","C","E"]] =[50,51,52] #[인덱스][컬럼의 이름] -> 값을 바꿔주기

# 모든컬럼 [인덱스]
#df[:][4]=[60,61,62,63,64,65] 에러
df.loc[4]=[60,61,62,63,64,65] 

del(df["F"])
#df.drop("E",axis=0) #axis=0 행 axis=1 열(컬럼)
df = df.drop("E",axis=1) #axis=1 열 axis=1 열(컬럼)
df = df.drop(1,axis=0) # 행을 지움


print(df)
print(df.loc[::-1]) # 인덱스가 역순으로 
print(df.loc[::-1,::-1]) # 컬럼이 역순으로 출력된다. 인덱스가 역순으로 
print(sorted([4,6,8,2,4])[::-1])

df = pd.DataFrame(
    [["kim",20,"1111-1111"],
     ["lee",30,"2222-1111"],
     ["park",31,"1111-2222"],
     ["you",32,"2222-2222"]], columns=["name","age","tel"]
    )

#boolean indexing
print()
print(df)
print(df.iloc[:,0:2])
print(df.loc[:,"name":"age"])
#print(df.loc[:,0:2])                    에러
#print(df.iloc[:,"name":"age"] )         에러

print("---"*50)
print(df.loc[df["age"]>=30,["name","age"] ])
print(df.loc[df["name"]=="kim" ,["name","age"] ])
print(df.loc[df["tel"]=="1111-2222" ,"name":"tel" ])
print(df.loc[(df["age"]>30) & (df["age"]<=40), ["name","age"] ])

#결축값
print()
df["address"]=""#빈칸 만들어주기
#빈칸에다가 채우기
df.loc[df["address"]=="",["address"]] ="서울"

df.loc[::2,["address"]] = None
df.loc[df["address"]==None , ["address"]] = "수원"
df.loc[df["address"].isnull(),["address"] ] ="수원"

#     전체 인덱싱 
df.loc[:,"income"] = [np.NaN,5000, np.NaN,6000]

df.loc[5,:] =[np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]

#df = df.dropna(how="any") # none인 데이터 모든것을 지운다.
#df = df.dropna(how="all") # 전부다 none인데이터를 지워라

#디비에 적용해라
df.dropna(how="all", inplace=True)

#df["income"].fillna(value=0 , inplace=True)#원본에 적용안됨

#df["income"].fillna(value= np.mean(df["income"]),inplace=True) 원본에 적용되게 하기

print(df.isnull()["income"])
print(df.drop(df.isnull()["income"].index, axis=0))
print(df.drop(["income"],axis=1))
#여러개 지울 수 있다.
print(df.drop(["tel","income"],axis=1))


print(df)

#행하고 열하고 바꿔서 처리 
print(df.T)
print(df.transpose())






