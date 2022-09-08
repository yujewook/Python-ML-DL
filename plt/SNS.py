import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset( "iris" )
titanic = sns.load_dataset( "titanic" )
tips = sns.load_dataset( "tips" )
flights = sns.load_dataset( "flights" )

# print( iris.head() )
# x = iris.petal_length.values
# sns.rugplot( x )
# sns.rugplot( data=iris, x="petal_length" )
# sns.kdeplot( data=iris, x="petal_length" )

# x = iris["petal_length"].values
# sns.distplot( x, kde=True, rug=True )

# sns.countplot( data=titanic, x="class")
# sns.countplot( data=tips, x="day")
# plt.hist( tips["day"] )

# sns.jointplot( iris["petal_length"], iris["petal_width"], alpha=0.5 )
# plt.suptitle( "Jointplot" )
# sns.jointplot( data=iris, x="petal_length", y="petal_width", kind="scatter" )
# sns.jointplot( data=iris, x="petal_length", y="petal_width", kind="kde" )

# sns.pairplot( iris )
# sns.pairplot( iris, hue="species", markers=["o", "s", "D"] )

# print( titanic.head() )
# titanic_size = titanic.pivot_table( index="class", columns="sex", aggfunc="size" )
# # print( titanic_size )
# sns.heatmap( titanic_size, cmap=sns.light_palette( "gray", as_cmap=True ), 
#              annot=True, fmt="d" )

# sns.barplot( data=tips, x="day", y="total_bill", hue="sex" )

# sns.boxplot( data=tips, x="day", y="total_bill", hue="sex" )

# sns.violinplot( data=tips, x="day", y="total_bill", hue="sex", split=True )

# sns.stripplot( data=tips, x="day", y="total_bill", jitter=True, alpha=0.5, hue="sex", dodge=True )

sns.swarmplot( data=tips, x="day", y="total_bill", size=3, hue="sex", dodge=True )



plt.show()





















