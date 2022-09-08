import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


## 파이 차트 ##
# ratio = [32, 34, 16, 18]
# fruits = ["apple", "banana", "melon", "grape"]
# # plt.pie( ratio, labels=fruits, autopct="%.1f%%" )
# # plt.pie( ratio, labels=fruits, autopct="%.1f%%", startangle=260, counterclock=False )
#
# explode = [0, 0.1, 0, 0.1]
# # plt.pie( ratio, labels=fruits, autopct="%.1f%%", explode=explode, shadow=True )
#
# colors = ["silver", "gray", "lightgray", "darkgray"]
# # plt.pie( ratio, labels=fruits, autopct="%.1f%%", colors=colors )
#
# wedgeprops = {"width":0.7, "edgecolor":"w", "linewidth":5}
# plt.pie( ratio, labels=fruits, autopct="%.1f%%", wedgeprops=wedgeprops )


## 히트맵 ##
# a = np.random.standard_normal( ( 30, 40 ) )
# # plt.matshow( a )
# # plt.colorbar( shrink=0.8, aspect=10 )
# # plt.clim( -3, 3 )
#
# # cmap = plt.get_cmap( "PiYG" )
# cmap = plt.get_cmap( "BuGn" )
# plt.matshow( a, cmap=cmap )
# plt.colorbar()
# plt.show()


## 여러 그래프 ##
# x1 = np.linspace( 0, 5 )
# x2 = np.linspace( 0, 2 )
# y1 = np.cos( 2 * np.pi * x1 ) * np.exp( -x1 )
# y2 = np.cos( 2 * np.pi * x2 )
#
# plt.subplot( 2, 1, 1 )
# plt.plot( x1, y1, "o-" )
# plt.title( "Graph 1" )
# plt.xlabel( "x1" )
# plt.ylabel( "y1" )
#
# plt.subplot( 2, 1, 2 )
# plt.plot( x2, y2, ".-" )
# plt.title( "Grape 2" )
# plt.xlabel( "x2" )
# plt.ylabel( "y2" )
#
# plt.yticks( visible=False )


## 컬러맵 ##
# from matplotlib import cm
# cmaps = plt.colormaps()
# for cmap in cmaps :
#     print( cmap, end=" " )
#
# np.random.seed( 0 )
# arr = np.random.standard_normal( ( 8, 100 ) )
#
# plt.subplot( 2, 2, 1 )
# # plt.scatter( arr[0], arr[1], c=arr[1], cmap="spring" )
# plt.scatter( arr[0], arr[1], c=arr[1] )
# plt.spring()
# plt.title( "spring" )
#
# plt.subplot( 2, 2, 2 )
# # plt.scatter( arr[2], arr[3], c=arr[3], cmap="summer" )
# plt.scatter( arr[2], arr[3], c=arr[3] )
# plt.viridis()
# plt.title( "summer" )
#
# plt.subplot( 2, 2, 3 )
# # plt.scatter( arr[4], arr[5], c=arr[5], cmap="autumn" )
# plt.scatter( arr[2], arr[3], c=arr[3] )
# plt.plasma()
# plt.title( "autumn" )
#
# plt.subplot( 2, 2, 4 )
# # plt.scatter( arr[6], arr[7], c=arr[7], cmap="winter" )
# plt.scatter( arr[2], arr[3], c=arr[3] )
# plt.gray()
# plt.title( "winter" )

# from matplotlib.colors import LinearSegmentedColormap
# colors = [ "#FF5A5A", "#F361A6", "#0100FF", "#000000" ]
# cmap = LinearSegmentedColormap.from_list( "my_cmap", colors, gamma=2 )
# plt.scatter( [1, 2, 3, 4, 5], [1, 3, 5, 7, 9], c=[8, 6, 5, 3, 2], cmap=cmap )


## 텍스트 삽입 ##
# a = 2.0 * np.random.randn( 10000 ) + 1.0
# b = np.random.standard_normal( 10000 )
# c = 20.0 * np.random.rand( 5000 ) - 10.0
# plt.hist( a, bins=100, density=True, alpha=0.7, histtype="step" )
# plt.hist( b, bins=50, density=True, alpha=0.5, histtype="stepfilled" )
# plt.hist( c, bins=100, density=True, alpha=0.9, histtype="step" )
#
# font1 = {
#     "family" : "serif",
#     "color" : "darkred",
#     "weight" : "normal",
#     "size" : 16
#     }
# font2 = {
#     "family" : "Times New Roman",
#     "color" : "blue",
#     "weight" : "bold",
#     "size" : 14,
#     "alpha" : 0.7    
#     }
# font3 = {
#     "family" : "Arial",
#     "color" : "forestgreen",
#     "style" : "italic",
#     "size" : 14
#     }
#
# box1 = {
#     "boxstyle" : "round",
#     "ec" : (1.0, 0.5, 0.5),
#     "fc" : (1.0, 0.8, 0.8)
#     }
# box2 = {
#     "boxstyle" : "square",
#     "ec" : "black",
#     "fc" : "lightgray",
#     "linestyle" : "--"    
#     }
# box3 = {
#     "boxstyle" : "square",
#     "linestyle" : "-",
#     "linewidth" : 2
#     }
#
# plt.text( 1.0, 0.35, "A", fontdict=font1, rotation=85, bbox=box1 )
# plt.text( 2.0, 0.25, "B", fontdict=font2, rotation=-50, bbox=box2 )
# plt.text( 5.0, 0.08, "C", fontdict=font3, bbox=box3 )

## 그래프 스타일 ##
print( plt.style.available )

# plt.style.use( "bmh" )
# plt.style.use( "ggplot" )
# plt.style.use( "classic" )
# plt.style.use( "grayscale" )
# plt.style.use( "Solarize_Light2" )
# plt.style.use( "default" )

# plt.rcParams["figure.figsize"] = (10, 5)
# plt.rcParams["font.size"] = 12
# plt.rcParams["lines.linewidth"] = 3
# plt.rcParams["lines.linestyle"] = "-."
# plt.rcParams["xtick.top"] = True
# plt.rcParams["ytick.right"] = True
# plt.rcParams["xtick.direction"] = "in"
# plt.rcParams["ytick.direction"] = "in"
# plt.rcParams["xtick.major.size"] = 7
# plt.rcParams["ytick.major.size"] = 7
# plt.rcParams["xtick.minor.visible"] = True
# plt.rcParams["ytick.minor.visible"] = True
#
# plt.plot( [1, 2, 3, 4, 5], [2, 4, 6, 8, 10] )
#
# plt.savefig( "save_default.png" )
# plt.savefig( "save_50.png", dpi=50 )
# plt.savefig( "save_100.png", dpi=100 )
# plt.savefig( "save.png", facecolor="#eeeeee", bbox_inches="tight", pad_inches=0.3 )

# 객체지향 인터페이스 
# fig, ax = plt.subplots( 2, 2, sharex=True, sharey=True )
# x = np.arange( 10 )
# ax[0][0].plot( x, np.sqrt( x ), label="graph1" )
# ax[0][1].plot( x, x )
# ax[1][0].plot( x, -x + 5 )
# ax[1][1].plot( x, np.sqrt( x+5 ) )
#
# ax[0][0].set_title( "Graph 1" )
# ax[0][0].legend()


# 이중 Y축
# plt.rcParams["figure.figsize"] = ( 10, 5 )
# plt.rcParams["font.size"] = 12
# x = np.arange( 10 )
# fig, ax1 = plt.subplots()
# ax1.plot( x, x+1, label="y1" )
#
# ax2 = ax1.twinx()
# ax2.plot( x, -x-1, label="y2" )
#
# ax1.set_xlabel( "X" ) 
# ax1.set_ylabel( "Y1" )
# ax2.set_ylabel( "Y2" )
#
# ax1.legend()
# ax2.legend()

# fig, ax1 = plt.subplots()
# x = np.arange( 2020, 2030 )
# y1 = np.array( [1, 3, 5, 7, 9, 10, 12, 14, 16, 20] )
# y2 = np.array( [1, 3, 7, 9, 11, 13, 16, 18, 20, 25] )
# ax1.plot( x, y1, color="g", marker="o", linewidth=5, alpha=0.5, label="Price" )
# ax1.legend( loc="upper left" )
#
# ax2 = ax1.twinx()
# ax2.bar( x, y2, color="r", label="Count", alpha=0.7, width=0.7 )
# ax2.legend( loc="upper right" )
#
# ax1.set_zorder( ax2.get_zorder() + 10 )
# ax1.patch.set_visible( False )
# ax2.patch.set_visible( False )
#
# from matplotlib import font_manager, rc
# for font in font_manager.fontManager.ttflist :
#     print( font )
# font_name = font_manager.FontProperties( fname="C:\\WINDOWS\\Fonts\\HANDotum.ttf" ).get_name()
# rc( "font", family=font_name )
#
# ax1.set_xlabel( "연도", fontproperties=font_name )
# ax1.set_ylabel( "가격", fontproperties=font_name )
# ax2.set_ylabel( "수량", fontproperties=font_name )


# 박스플롯
plt.rcParams["figure.figsize"] = ( 10, 5 )
plt.rcParams["font.size"] = 12
np.random.seed( 0 )
a = np.random.normal( 0, 2.0, 1000 )
b = np.random.normal( -3.0, 1.5, 500 )
c = np.random.normal( 1.5, 1.5, 1500 )
fig, ax = plt.subplots()


#ax.boxplot( [a, b, c] )

box = ax.boxplot([a,b,c], whis=1.5, notch=True)
ax.set_ylim( [-10, 10] )
ax.set_xlabel( "Data" )
ax.set_ylabel( "Value" )


for flier in box["fliers"]:
    print(flier.get_data())

plt.tight_layout()
plt.show()



























