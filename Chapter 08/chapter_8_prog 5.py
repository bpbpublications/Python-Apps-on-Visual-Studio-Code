#Step 1: Import Libraries
import folium
from ipywidgets import Layout
import ipywidgets as widgets
import matplotlib.pyplot as plt
from folium import plugins
from ipywidgets import Layout
import pandas as pd
import seaborn as sns
import numpy as np

#Step 2: Check the dataset
df_vaccination = pd.read_csv('https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/vaccination-data.csv')
df_vaccination.shape

df_vaccination.head(3)

df_vaccination.describe()

#Step 3: Perform Data Cleaning
# Check null values in each column in percentage
(df_vaccination.isnull().sum() / len(df_vaccination.index)) * 100

# This heatmap shows us the null columns
sns.heatmap(df_vaccination.isnull(), yticklabels=False, cmap='viridis', cbar=False)

df_vaccination.dropna(inplace = True)

#Step 4: Adding ipywidgets
style = {'description_width': 'initial'}

limit_case = widgets.IntSlider(
    value=10,
    min=1,
    max=100,
    step=1,
    description='FULLY VACCINATED/100',
    disabled=False,
    style=style)

unique_country = df_vaccination.COUNTRY.unique()
unique_region = df_vaccination.WHO_REGION.unique()

country = widgets.SelectMultiple(
    options = unique_country.tolist(),
    value = ['India', 'China','France'],
    #rows=10,
    description='Country',
    disabled=False,
    layout = Layout(width='50%', height='80px')
)

category = widgets.SelectMultiple(
    options = unique_region.tolist(),
    value = ['EURO', 'AFRO', 'SEARO'],
    #rows=10,
    description='Region',
    disabled=False,
    style=style,
    layout = Layout(width='50%', height='80px')
)

#Step 5: Create Update() function
def update_map(country, category, limit):    
    #df_vaccination
    latitude = 60
    longitude = -2.2
    
    df_country = df_vaccination.loc[df_vaccination['COUNTRY'].isin(np.array(country))]
    df_category = df_country.loc[df_country['WHO_REGION'].isin(np.array(category))]
    
    cat_unique = df_category.groupby('WHO_REGION')['PERSONS_FULLY_VACCINATED_PER100'].mean()
    country_unique = df_country.groupby('COUNTRY')['PERSONS_FULLY_VACCINATED_PER100'].mean()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    # create map and display it
    country_map = folium.Map(location=[latitude, longitude], zoom_start=2)
    
    country_count = plugins.MarkerCluster().add_to(country_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, in zip(df_category.lat, df_category.lng, df_category.WHO_REGION):
        folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
        ).add_to(country_count)
    # show map
    display(country_map)

    #Bar graph to show Fully Vaccinated Person per 100
    ax1.bar(df_category['WHO_REGION'],cat_unique)
    ax1.set_title('Fully Vaccinated Person per 100')
    ax2.bar(df_country['COUNTRY'], country_unique)
    ax2.set_title('Fully Vaccinated Person per 100')
    plt.show()

#Step 6: Executing the dashboard
widgets.interactive(update_map, country = country, category = category,limit=limit_case)