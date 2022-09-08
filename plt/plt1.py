import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
# #plt.plot([1,2,3,4])
# #            x값     y값
# #plt.plot([1,2,3,4],[1,4,9,16])
# #                            점찍는 옵션
# #plt.plot([1,2,3,4],[1,4,9,16],"ro-")
#
#
# #t = np.arange(0,5,0.2)
#                             #모양
# #plt.plot( t , t ,"r--",t**2, "bs",t**3,"g^" )
#
# #도표를 찍을려면 리스트가 되어야한다.
# data_dic={"data x":[1,2,3,4,5], "data y":[2,4,6,8,10]}
# plt.plot("data x","data y",data=data_dic, label="Price")
#
# #라벨 폰트
# font1 ={
#     "family" : "serif",
#     "color"  : "b",
#     "weight" : "bold",
#     "size" : 14
#     }
# font2 = {
#     "family" : "fantasy",
#     "color"  : "deeppink",
#     "weight" : "normal",
#     "size" : "xx-large"
#     }
#
# #데이터 라벨 붙이기     #라벨 간격 조절  #폰트지정        #위치
# plt.xlabel("data_x", labelpad=15 ,fontdict=font1 , loc="right")
# plt.ylabel("data_y", labelpad=20 ,fontdict=font2 , loc="top")
#
#
# plt.plot([1,2,3,4,5],[-1,-2,-3,-4,-5],"r",label="count")
# #라벨이 있어야한다#위치
# #plt.legend(loc=(0.5,0.5))
# #plt.legend( loc="best" )
# #plt.legend(loc="upper right")
#
# #레전드    한줄에 하나씩 ncol=1 한줄에 두개씩 찍어라 ncol=2 
# #plt.legend(ncol=2)
#
# #폰트
# #plt.legend(fontsize=14,frameon=False,shadow=True)
# plt.legend(shadow=True)
#
# # 도표 보여주는 도표의 값을 보여주는것
# # plt.xlim([0,10])
# # plt.ylim([-10,20])
# #plt.axis([0,10,-10,20])
#
# #
# #plt.axis("equal")













#line style
# plt.plot([1,2,3],[4,4,4], linestyle="solid", label="solid")
# plt.plot([1,2,3],[3,3,3], linestyle="dashed", label="dashed")
# plt.plot([1,2,3],[5,5,5], linestyle="dotted", label="dotted")
# plt.plot([1,2,3],[6,6,6], linestyle="dashdot", label="dashdot")

# plt.plot([1,2,3],[4,4,4], linestyle="-", label="solid")
# plt.plot([1,2,3],[3,3,3], linestyle="--", label="dashed")
# plt.plot([1,2,3],[5,5,5], linestyle=":", label="dotted")
# plt.plot([1,2,3],[6,6,6], linestyle="-.", label="dashdot")

# plt.plot([1,2,3],[4,4,4], linestyle=(0,(1,1)), label="solid")
# plt.plot([1,2,3],[3,3,3], linestyle=(0,(1,5)), label="dashed")
# plt.plot([1,2,3],[5,5,5], linestyle=(0,(5,1)), label="dotted")
# plt.plot([1,2,3],[6,6,6], linestyle=(0,(3,5,1,5)), label="dashdot")


#                                두깨                        #각지게 ,둥글게 
# plt.plot([1,2,3],[4,4,4], "-", linewidth=10 , solid_capstyle="butt")
# plt.plot([1,2,3],[3,3,3], "-", linewidth=10 , solid_capstyle="round" )
# plt.plot([1,2,3],[5,5,5], "--", linewidth=10 , dash_capstyle="butt" )
# plt.plot([1,2,3],[6,6,6], "--", linewidth=10 , dash_capstyle="round")

# plt.plot([1,2,3],[4,4,4], "-", marker="o")
# plt.plot([1,2,3],[3,3,3], "-", marker="^" )
# plt.plot([1,2,3],[5,5,5], "--", marker="v" )
# plt.plot([1,2,3],[6,6,6], "--", marker="<")


#                        마커에 모든기능 다 넣어버리기
# plt.plot([1,2,3],[4,4,4], "bo-")
# plt.plot([1,2,3],[3,3,3], "g^-" )
# plt.plot([1,2,3],[5,5,5], "rv--" )
# plt.plot([1,2,3],[6,6,6], "y<--")
#
# plt.plot([1,2,3],[4,4,4], marker="H",color="limegreen")
# plt.plot([1,2,3],[3,3,3], marker="d" )
# plt.plot([1,2,3],[5,5,5], marker="x")
# #plt.plot([1,2,3],[6,6,6], marker="11")
# plt.plot([1,2,3],[6,6,6], marker="$Z$")


# x=[1,2,3,4,5]
# y=[2,4,6,8,11]
#
# plt.plot(x,y)
# # 범위를 주어서 채우는 방법
# #plt.fill_between(x[1:4],y[1:4],alpha=0.5)
# #y좌표 채우는 방법 plt.fill_between( y[1:4], x[1:4], alpha=0.5)
#
# z = [4,5,8,11,14]
# plt.plot(x,z)
# #plt.fill_between(x[1:4],y[1:4],z[1:4], alpha=0.5, color="lightgray")
#
# plt.fill([1.9,1.9,3.1,3.1],[1.0,4.0,6.0,3.0], color="magenta" ,alpha=0.5)


# x = np.linspace(-10,10,100)
# y=x**3
# plt.plot(x,y)
# plt.xscale("symlog")
# plt.yscale("log")
#
# plt.grid(True, axis="y", color="red",alpha=0.5,linestyle="--")

#plt.legend()
#                    갯수
# x= np.arange(0,2, 0.2)
# plt.plot(x,x,"bo")
# plt.plot(x,x**2,"r*")
#
# # plt.xticks([0,1,2])
# # plt.yticks(np.arange(0,5))
#
# plt.xticks(np.arange(0,2,0.5), labels=["Jan","Feb","April","May"])
# plt.xticks(np.arange(0,5), labels=["0GB","1GB","2GB","3GB","4GB"])
#
# plt.tick_params( axis="both", direction="inout", length=10, pad=6, labelsize=12, labelcolor="green",
#                  top=True )
#
# plt.axhline(1.8, 1,3 ,color="red",linestyle=":",linewidth=2)
#
#
# plt.tight_layout()
# plt.show()

# 막대 그래프
x = np.arange(3)
y = [100,300,700]
years = ["2020","2021","2022"]
#plt.bar(x,y)
#plt.xticks(np.arange(3), years)
#plt.bar(x,y, color="y")
colors= ["y","b","g"]
#plt.bar(x,y,color=colors)
#plt.bar(x,y,color=colors, width=0.8)
#plt.bar(x,y, align="edge",linewidth=5, tick_label = years)


#plt.barh(x,y)
#plt.yticks(np.arange(3), years)
#plt.barh(x,y,align="edge",edgecolor="#eee",linewidth=5,tick_label=years)


##산전도
np.random.seed(0)
n =100
x = np.random.rand(n)
y = np.random.rand(n)
#plt.scatter(x,y)

# area = (30 *np.random.rand(n))**2
# plt.scatter(x,y , s=area, alpha=0.5)

# plt.plot([1],[1],'o',markersize=20, c="r")
# plt.scatter([2],[1],s=400,c="b")
# plt.text(1,1.01,"plot", fontdict={"size":14})
# plt.text(2.0,1.01,"Scatter",fontdict={"size":14})
# plt.axis([0.5,2.5,0,2])

# colors =np.random.rand(n)
# plt.scatter(x, y,  c=colors, alpha=0.5)
# plt.colorbar()


from mpl_toolkits.mplot3d import Axes3D
# n = 100
# xmin, xmax, ymax, ymin , zmin,zmax = 0,20,20,0,0,50
# cmin, cmax= 0, 2
# x = np.array( [ (xmax-xmin) * np.random.random_sample() + xmin for i in range(n) ]) 
# y = np.array( [ (ymax-ymin) * np.random.random_sample() + ymin for i in range(n) ]) 
# z = np.array( [ (zmax-zmin) * np.random.random_sample() + zmin for i in range(n) ]) 
# color = np.array([(cmax-cmin)*np.random.random_sample()+ cmin for _ in range(n)])
# fig =plt.figure(figsize=(6,6))
# ax=fig.add_subplot(111,projection="3d")
# ax.scatter(x,y,z,c=color, marker="o" , s=15)

#히스토그램
weights = np.array( [ (150-40) * np.random.random_sample() + 40 for _ in range( n ) ] )
# plt.hist( weights ) # 범위를 알아서 정함 
# plt.hist( weights, bins=20 ) # 막대기 20개
# plt.hist( weights, bins=20, cumulative=True )

weights1 = np.array( [ (150-40) * np.random.random_sample() + 40 for _ in range( n*10 ) ] )
# plt.hist( (weights, weights1 ), label=("weights", "weights1") ) # 2개 출력
# plt.hist( (weights, weights1 ), label=("weights", "weights1"), histtype="bar" ) # 2개 출력
# plt.hist( (weights, weights1 ), label=("weights", "weights1"), histtype="barstacked" ) # 위에 쌓음
# plt.hist( ( weights, weights1), label=("weights", "weights1"), histtype="step" )
# plt.hist( ( weights, weights1), label=("weights", "weights1"), histtype="stepfilled", alpha=0.5 )

plt.hist( ( weights, weights1), label=("weights", "weights1"), histtype="step", density=True ) #정규화 두개의 값이 비슷하게 나옴

plt.legend()

plt.tight_layout()
plt.show()






































plt.legend()


plt.show()



