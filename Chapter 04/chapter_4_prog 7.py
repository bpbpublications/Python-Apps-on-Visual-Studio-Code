import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import pandas as pd
# put y-axis in bold
rc('font', weight='bold')
# Values of each group
Y22Q1 = [11, 14, 10, 18, 13]
Y22Q2 = [17, 21, 19, 8, 11]
Y22Q3 = [36, 22, 3, 16, 34]
# Heights of bars1 + bars2
bars = np.add(Y22Q1, Y22Q2).tolist()
# Creating 5 positions for the bars on x-axis
r = [0, 1, 2, 3, 4]
# Names of group and bar width
names = ['Mumbai', 'Delhi', 'Hyderabad', 'Kolkata', 'Chennai']
barWidth = 1
# Create brown bars
plt.bar(r, Y22Q1, color='#7f6d5f', edgecolor='white', width=barWidth)
# Creating green bars (middle), on top of the first bar
plt.bar(r, Y22Q2, bottom=Y22Q1, color='#557f2d',
        edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, Y22Q3, bottom=bars, color='#2d7f5e',
        edgecolor='white', width=barWidth)
# Custom X axis

plt.xticks(r, names, fontweight='bold')
plt.xlabel("Cities")
plt.ylabel("in thousand Crores")
plt.title("Quarterly Average GST Collection")
plt.suptitle("Top 5 Cities in India")
# Show graphic
plt.show()