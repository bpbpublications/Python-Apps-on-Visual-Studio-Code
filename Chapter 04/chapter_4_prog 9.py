import numpy as np
arr = np.loadtxt("https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/HistogramData.csv",
                 delimiter=",", dtype=float)
print(arr)


import matplotlib.pyplot as plt
#create bin
bin = [10 * i for i in range(13)]
# plot histogram
plt.hist(arr, bin)
plt.show()