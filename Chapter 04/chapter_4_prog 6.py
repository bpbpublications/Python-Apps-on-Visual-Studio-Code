import pandas as pd
#Read the 3 csv files
d1 = pd.read_csv(r'https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/user_usage.csv')
# monthly mobile usage statistics
print(d1.head(5))
d2 = pd.read_csv(r'https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/user_device.csv')
#check the device and OS version for each user
print(d2.head(5))
d3 = pd.read_csv(r'https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/android_devices.csv')
#contains details of all Android devices with model number and manufacturer
print(d3.head(5))

#adding device and platform columns to the user_usage
result = pd.merge(d1,
                  d2[['use_id', 'platform', 'device']],
                  on='use_id')
print(result.head())

#Analyze the dimensions of the dataframes
print("user_usage Dimensions: ",d1.shape)
print("user_device Dimensions: ", d2[['use_id', 'platform',
                                      'device']].shape)
print("result Dimensions: ",result.shape)
#how many values are common
print(d1['use_id'].isin(d2['use_id']).value_counts())

#Changing the merge to a left-merge with the "how" parameter 
result = pd.merge(d1,
                  d2[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left',
                  indicator =True)
result.head()
print("user_usage Dimensions: ",d1.shape)
print("result Dimensions: ",result.shape)
print(f"There are {result['device'].isnull().sum()} missing values in the result.")

# Adding platform and device to the user usage
result = pd.merge(d1,
                  d2[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')
# Merging on the "device" column in result
# match the "Model" column in devices (d3)
d3.rename(columns={"Retail Branding": "manufacturer"},inplace=True)
result = pd.merge(result,
                  d3[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')
print(result.head())