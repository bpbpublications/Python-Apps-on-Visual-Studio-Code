import numpy as np
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr

#Let’s read the data into Pandas dataframe:
data = pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/JobStressData.csv")
#https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/JobStressData.csv
print(data.shape)  # shows number of rows, columns

summary = data.describe()
print(summary)

# Filter the data for job role = MANAGER
manager_df = data.loc[data['Role'] == "MANAGER"]
manager_df = manager_df.drop('Role',axis=1)
print(manager_df.corr())

# plotting the heatmap for correlation
ax = sns.heatmap(manager_df.corr(), annot=True)
plt.show()

# Scatterplot
ax = sns.scatterplot(x="WorkFamilyConflict", y="JobStress", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict")
ax.set_xlabel("Work-Family Conflict")
plt.show()

# Let's use .loc to restrict values of 'WorkFamilyConflict' displayed
manager_df = manager_df.loc[manager_df['WorkFamilyConflict'].between(0, 70)]
ax = sns.scatterplot(x="WorkFamilyConflict", y="JobStress", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict")
ax.set_xlabel("Work-Family Conflict")
plt.show()

# Adding a best fit line
sns.lmplot(x="WorkFamilyConflict", y="JobStress", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict")
ax.set_xlabel("Work-Family Conflict")
plt.show()

# Adding FamilySupportScore as a third dimension
sns.lmplot(x="WorkFamilyConflict", y="JobStress",
           hue="FamilySupportScore", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict")
ax.set_xlabel("Work-Family Conflict")
plt.show()

# Coefficient of correlation
from scipy.stats import pearsonr
corr, _ = pearsonr(manager_df['JobStress'], manager_df['WorkFamilyConflict'])
print('Pearsons correlation: %.3f' % corr)