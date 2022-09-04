import numpy as np

# a=[[1,2,3,4,6],[5,6,7,8]]
# print(a)
# a = np.arange( 15 ).reshape(3,5)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize) #4byte이다.
# print(a.size)
#
# #함수 호한 
# t = (10,20,30,40,50)
# print(type(t))
#
# tt = np.array(t)
# print =( type(tt) )
#
# #s ={10,20,30,40,50}
# #print(type(s))
# #ss =np.array(s)
# #print(type(ss))
#
# m=[10,20,30,40,50]
# #print(type(m))
#
# mm = np.array(m)
# print(mm.shape)

#
# w = [1,2,3,4,5,6,7,8]
# print(np.shape(w))
# print(np.abs(w))
# #음수는 마이너스 루트가 안됨
# #print(np.square(w))
#
# #print(np.isnan(w))


# w=[[1,3,5],[2,4,6]]   
# print( w )


m =[10,20,30,40,50]
#print(m+2) 에러 리스트는
m=np.array(m)
print(m+2) # element wise

w =[1,2,3,4,6]
print(m+w) # mw가 똑같은 갯수이면 된다 다른갯수이면 된다.


print(np.sin(m)*10)

a = np.array([[1,1],[1,1]]) # 행렬 연산
b = np.array([[1,2],[3,4]])
print(np.add(a,b))
print(a+b)
print(np.subtract(a,b))
print(a-b)
print(np.multiply(a,b))
print(a*b)
print(np.divide(a,b))
print(a//b)
         
print(a@b)
print(a.dot(b)) 

print(np.zeros(10))
print(np.zeros( (3,3,) )) #튜플로 줘야한다.   
       

#랜덤
x = np.random.randn( 10 )
print(x)

y= np.random.randn(10)
print(np.maximum(x,y))


#인덱싱 / 슬라이싱
s="ABCDEFG"
print(s[1])
print(s[1:4])
a= [ i for i in range(10,20)]
print(a[0]) #인덱싱
print(a[0:5]) #슬라이싱
print(a[0:-1]) #슬라이싱
print(a[:6])
print(a[6:])

b= np.arange(10,20)
print(b[0])
print(b[0:5])
print(b[0:-1]) #슬라이싱
print(b[:6])
print(b[6:])


#이차원 리스트
a = [[1,2,3,4],[6,7,8,9,10],[11,12,13,14,15]]
print(a[2][2])
print(a[:][:])
print(a[0:2][1]) #앞에 나온 [0:2] -> 결과에서 뒤에나온 [1]를 인덱싱해라
#print(a[0:2,0:2]) 에러

b = np.arange( 1, 16 ).reshape( 3, 5 )
print( b )
print( b[2][2] )
print( b[:][:] )
print( b[:] )
print( b[2][:] )
print("==")

print( b[0:2][0:2]) #np에서는 된ㅇㅇ
print( b[:-1, :-1] )
print( b[1:2, :] )
print( b[2, 2] )

a = np.empty((8,4))
for i in range(8):
    a[i] = i
print(type(a))
print(a)

b = np.arange(32).reshape(8,4)
print(type(b))
print(b)
print(b[[5,7,2]]) # 행의 인덱스
print(b[[5,7,2],[1,2,3]])

print(b)
print(b.T) # 행하고 열을 바꾸는 것

#반올림하는 함수
a =np.floor( np.random.rand( 2,2 )*10)
print(a) 
b = np.floor(np.random.rand(2,2)*10)
print(b)
print(np.hstack((a,b)) )
print(np.vstack((a,b)) )


c = np.floor(np.random.rand(2,12)*10)
print(c) 
print(np.hsplit(c,3))
print(np.hsplit(c,(3,5))) #위치값 대로 짜른다

d = np.floor(np.random.rand(12,2)*10)
print(d)
print(np.vsplit(d,3))













