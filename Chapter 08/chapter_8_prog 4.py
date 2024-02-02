#Import required libraries
import pandas as pd
import numpy as np
import panel as pn
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
from numerize import numerize

pn.extension('tabulator')

import hvplot.pandas
import geopandas as gpd

#Step 2: Reading the datasets (Covid and Vaccines)
# cache data to improve dashboard performance
if 'data' not in pn.state.cache.keys():
    df = pd.read_csv('WHO-COVID-19-global-table-data.csv')
    pn.state.cache['data'] = df.copy()

else: 
    df = pn.state.cache['data']

df_vaccination = pd.read_csv('vaccination-data.csv')
df_vaccination.shape
# Make DataFrame Pipeline Interactive
idf = df.interactive()

#Step 3: Understanding the data and the content
#WHO-Covid 19 data:
df.head(2)
df.describe()

#Vaccines data:
df_vaccination.head(3)
df_vaccination.shape
df_vaccination.describe()

#Step 4: Data Cleaning
#WHO-Covid 19 data:
# Check null values in each column in percentage
(df.isnull().sum() / len(df.index)) * 100

# This heatmap shows us the null columns for WHO Covid 19 data
sns.heatmap(df.isnull(), yticklabels=False, cmap='viridis', cbar=False)

df.drop(columns='Deaths - newly reported in last 24 hours', inplace = True)

#Now, lets drop the rows that has null values. 
df.dropna(inplace=True)
# Check null values in each column in percentage
(df.isnull().sum() / len(df.index)) * 100

#Get the unique list of region names:
country_list = list(set(df.Name))
country_list

#Now columns:
df.columns

#Data cleaning of Vaccines data:
# Check null values in each column in percentage
(df_vaccination.isnull().sum() / len(df_vaccination.index)) * 100
# This heatmap shows us the null columns
sns.heatmap(df_vaccination.isnull(), yticklabels=False, cmap='viridis', cbar=False)

df_vaccination.dropna(inplace = True)
vacinated_country_list = list(set(df_vaccination.COUNTRY))
df_vaccination.columns
# Creating Bar Graph in Hvplot
colors = {
    'Americas': '#1f77b4',
    'Europe': '#ff7f0e',
    'Africa': '#2ca02c',
    'Western Pacific': '#324d67',
    'Eastern Mediterranean': '#ffca3a',
    'South-East Asia': '#ff595e'
}
def plot_bars_1():
    return df.hvplot.bar('Name', 'Cases - cumulative total', c='Name',
     cmap=colors, height=300, width=750, legend=False, rot = 45,
     yformatter='%.0f').aggregate(function=np.sum).opts(xlabel="Regions",
     ylabel="Cumulative Cases",
     title="Covid Cases across Regions")

# Creating Bar Graph in Hvplot
colors = {
    'Americas': '#1f77b4',
    'Europe': '#ff7f0e',
    'Africa': '#2ca02c',
    'Western Pacific': '#324d67',
    'Eastern Mediterranean': '#ffca3a',
    'South-East Asia': '#ff595e'
}
def plot_bars_2():
    return df.hvplot.bar('Name', 'Deaths - cumulative total', c='Name',
   cmap=colors, height=300, width=750, legend=False, rot = 45,
   yformatter='%.0f').aggregate(function=np.sum).opts(xlabel="Regions",
   ylabel="Cumulative Death Cases",
   title="Covid Death Cases across Regions")

plot_bars_2()

columns = list(df.columns[1:-1])

x = pn.widgets.Select(value='Cases - cumulative total', options=columns, name='x')
y = pn.widgets.Select(value='Deaths - cumulative total', options=columns, name='y')

scatter_plot = pn.Row(pn.Column('## Covid Scatter Plot', x, y), pn.bind(df.hvplot.scatter, x, y, by='Name', width = 1190, height = 500))
scatter_plot.show()

# Card 1 - Total Vaccinated person
TOTAL_VACCINATION = df_vaccination.TOTAL_VACCINATIONS.sum()
# Card 2 - Total Vaccinated person
FULLY_VACCINATED_PEOPLE = df_vaccination.PERSONS_FULLY_VACCINATED.sum()

# Card 3 - Total Vaccinated person
TOTAL_BOOSTER_DOSE = df_vaccination.PERSONS_BOOSTER_ADD_DOSE.sum()
# Card 4 - Total Vaccinated person
df['TOTAL_PEOPLE_RECOVERED'] = df['Cases - cumulative total'] - df['Deaths - cumulative total']
TOTAL_PEOPLE_RECOVERED = df.TOTAL_PEOPLE_RECOVERED.sum()
TOTAL_VACCINATION = numerize.numerize(TOTAL_VACCINATION)
FULLY_VACCINATED_PEOPLE = numerize.numerize(float(FULLY_VACCINATED_PEOPLE))
TOTAL_BOOSTER_DOSE = numerize.numerize(TOTAL_BOOSTER_DOSE)
TOTAL_PEOPLE_RECOVERED = numerize.numerize(TOTAL_PEOPLE_RECOVERED)
table = df_vaccination.groupby(['COUNTRY'])['NUMBER_VACCINES_TYPES_USED'].mean().sort_values()

vaccination_vs_country_bar = df_vaccination.hvplot.bar('COUNTRY', 'NUMBER_VACCINES_TYPES_USED', stacked=False, legend='bottom_right', height = 600, width=1510, rot = 90)


#Layout using Template
from panel.template import DarkTheme
template = pn.template.MaterialTemplate(title = 'Covid-19 Dashboard', theme = DarkTheme,
    sidebar=[pn.pane.PNG('Corona_1.png'),
    pn.pane.Markdown("# Total Vaccination Completed : " + f"{TOTAL_VACCINATION}"), 
    pn.pane.Markdown("# Fully Vaccinated People : " + f"{FULLY_VACCINATED_PEOPLE}"),
    pn.pane.Markdown("# Total Booster Dose Completed : " + f"{TOTAL_BOOSTER_DOSE}"),
    pn.pane.Markdown("# Total Recovered Population : " + f"{TOTAL_PEOPLE_RECOVERED}")
             ],
       main =  [
         pn.Row(plot_bars_1(), plot_bars_2()),
         pn.Row(vaccination_vs_country_bar),
         pn.Row(scatter_plot),
       ] )
template.show();