import numpy as np
# numpy는 대체로 np로 줄여서 쓴다.

a = [[1, 2, 3, 4], [5, 6, 7, 8]]    # 리스트. numpy 객체와는 다르다.
print(a)

a = np.arange(15).reshape(3, 5)  # 0~14까지 나열. 행 3개 열 5개의 행렬 형태로 나열
print(a)
print(a.shape)  # 행과 열의 갯수 출력. (3, 5)
print(a.ndim)   # 몇 차원인지 출력
print(a.dtype)      # int32
print(a.itemsize)   # dtype이 int32 -> 32bit -> 4byte
print(a.size)       # a의 원소의 갯수

t = (10, 20, 30, 40, 50)
print(type(t))      # tuple
tt = np.array(t)
print(type(tt))     # numpy.ndarray     
s = {10, 20, 30, 40, 50}
print(type(s))      # set
ss = np.array(s)
print(type(ss))     # numpy.ndarray

m = [10, 20, 30, 40, 50]
# print(m.shape)      # error
print(type(m))      # list
mm = np.array(m)
print(mm.shape)     # (5, )
print(type(mm))     # numpy.ndarray

w = [-5, 9, 8, 7, 5, -6, -7, 3, -5, 2]
print(np.shape(w))  # (10, )
print(np.abs(w))    # 리스트 각 요소의 절댓값 출력
print(np.square(w)) # 리스트 각 요소의 제곱 출력
print(np.sqrt(np.abs(w))) # 리스트 각 요소의 절댓값의 제곱근 출력
# np.sqrt()는 제곱근을 구하므로 반드시 모든 요소가 음이 아닌 수야 한다.

# print(help(np.shape))   # help: 함수의 사용법 등을 알려줌

print(np.isnan(w))      # NaN인지 확인
print(np.sum(w))        # 합
print(np.mean(w))       # 평균
print(np.max(w))        # 최대값
print(np.min(w))        # 최소값
print(np.argmax(w))     # 최대값의 인덱스
print(np.cumsum(w))     # 누적합

# w=sorted(w)
# print(w)

print(np.sort(w))
print(np.sort(w)[::-1])


# 2차원 리스트
w = [[1, 3, 5], [2, 4, 6]]
print(w)
w = np.array(w)
print(w)
w = [1, 2, 3, 4, 5, 6]
w = np.array(w).reshape(2, 3)
# w = np.array(w).reshape(3, 3)    # 에러
w = w.reshape(3, 2)
print(w)

# 데이터 분석 시 null 값(결측치)이 많다. 결측치 처리를 위해 아래 함수들을 쓸 수 있다.
print(np.sum(w))            # 합
print(np.sum(w, axis=0))    # 행끼리 계산
print(np.sum(w, axis=1))    # 열끼리 계산
print(np.mean(w))           # 평균
print(np.mean(w, axis=0))   # 행끼리 계산
print(np.mean(w, axis=1))   # 열끼리 계산
print(np.median(w))         # 중간값. 평균보다 중간값이 대표값으로 보다 정확하다.
print(np.median(w, axis=0)) # 행끼리 계산
print(np.median(w, axis=1)) # 열끼리 계산

print(np.var(w))            # 분산        거리 ** 2 값의 평균
print(np.std(w))            # 표준편차     분산의 제곱근
print(np.std(w, axis=0))    # 행끼리 계산
print(np.std(w, axis=1))    # 열끼리 계산

m = [10, 20, 30, 40, 50]
# print(m + 2)    # 에러
m = np.array(m)
print(m + 2)                # element wise

w = [1, 2, 3, 4, 5]
print(m + w)                # element wise

print(np.sin(m) * 10)       # sin
print(m > 20)               # boolean

a = np.array([[1, 1], [1, 1]])
b = np.array([[1, 2], [3, 4]])
print(np.add(a, b))         # 같은 인덱스끼리 덧셈
print(a + b)                # 같은 인덱스끼리 덧셈
print(np.subtract(a, b))    # 같은 인덱스끼리 뺄셈
print(a - b)                # 같은 인덱스끼리 뺄셈
print(np.multiply(a, b))    # 같은 인덱스끼리 곱셈
print(a * b)                # 같은 인덱스끼리 곱셈
print(np.divide(a, b))      # 같은 인덱스끼리 나눗셈(정수)
print(a // b)               # 같은 인덱스끼리 나눗셈(정수)

print(a @ b)                # 행렬곱(내적)
print(a.dot(b))             # 행렬곱(내적)

print(np.zeros(10))         # 모든 원소가 0인 행렬 생성. 1행 10열
print(np.zeros((3, 3)))       # 모든 원소가 0인 행렬 생성. 3행 3열
print(np.ones((3, 3)))        # 모든 원소가 1인 행렬 생성. 3행 3열

x = np.random.randn(10)     # 정규 분포에 맞는 난수 10개 생성
print(x)
y = np.random.randn(10)
print(np.maximum(x, y))     # 각 인덱스끼리 비교해서 값이 더 큰 것을 출력한다.
print(np.minimum(x, y))     # 각 인덱스끼리 비교해서 값이 더 작은 것을 출력한다.

# 인덱싱 / 슬라이싱
s = "ABCDEFG"
print(s[1])
print(s[1:4])

a = [i for i in range(10, 20)]      # list
print(a[0])
print(a[0:5])
print(a[0:-1])
print(a[:6])
print(a[6:])

b = np.arange(10, 20)               # ndarray
print(b[0])
print(b[0:5])
print(b[:-1])
print(b[:6])
print(b[6:])

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# print(a)
print(a[2][2])
print(a[:][:])              # 전체 출력
print(a[:])                 # 전체 출력
print(a[2][:])
print(a[0:2][0:2])          # 앞의 슬라이싱 결과에 대해서 또다시 슬라이싱이 일어난다.
print(a[0:2][1])
# print(a[0:2, 0:2])        # 에러. numpy, pandas에서는 가능한 문법. 앞이 행, 뒤가 열

b = np.arange(1, 16).reshape(3, 5)
print(b)
print(b[2][2])
print(b[:][:])
print(b[:])
print(b[2][:])
print(b[0:2][0:2])
print(b[0:2][1])

print(b[0:2, 0:2])
print(b[:-1, :-1])
print(b[1:2, :])
print(b[2, 2])

a = list(np.empty((8, 4)))  # 쓰레기 값으로 가득한 8행 4열 짜리 리스트 생성
# print(a)
for i in range(8):
    for j in range(4):
        a[i][j] = i
print(type(a))
print(a)
# print(a[[5, 7, 2]])        # 에러

b = np.arange(32).reshape(8, 4)
print(type(b))
print(b)
print(b[[5, 7, 2]])             # 행 단위로 원하는 인덱스로 가져온다.
print(b[[5, 7, 2], [1, 2, 3]])  # 행과 열 단위로 원하는 값을 가져온다.

print(b)
print(b.T)                      # 행과 열이 전치된다.

a = np.floor(np.random.rand(2, 2) * 10)
print(a)
b = np.floor(np.random.rand(2, 2) * 10)
print(b)
print(np.hstack((a, b)))
print(np.vstack((a, b)))

c = np.floor(np.random.rand(2, 12) * 10)
print(c)
print(np.hsplit(c, 3))
print(np.hsplit(c, (3, 5)))     # 0~2 3~4 5~11

d = np.floor(np.random.rand(12, 2)) * 10
print(d)
print(np.vsplit(d, 3))
print(np.vsplit(d, (3, 5)))     # 0~2 3~4 5~11