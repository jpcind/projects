#!/usr/bin/env python
# coding: utf-8

# In this project, we will be looking into 3 years of data, from 2015-2017.
# 
# These 3 years will entail information about the happiness of multiple countries.
# 
# The group expects to find a normal distribution for the Happiness Score. 
# 
# ### Null Hypothesis:
# #### A normal distribution is present within the Happiness Score for all the countries for the collective years of 2015, 2016, and 2017.
# 
# ### Alternate Hypothesis:
# #### A normal distribution is NOT present within the Happiness Score for all the countries for the collective years of 2015, 2016, and 2017.
# 
# The team has extracted information from the data sets, and will use these questions to help prove or disprove the null hypothesis:
#     
#     1. Which happiness factor within our dataframe mostly contributes to a nation's overall happiness? 
#     And which countries exhibits it's highest and lowest scores?
#     
#     2. What are the happiest regions around the world from greatest to lowest?
#     
#     3. Which region harbors the best economy? 
#     And was the economic correlation towards happiness strong enough to propel that region's Happiness Score to 1st place? Why or why not? 
#     
#     4. What are the happiest and unhappiest countries per region? 
#     And which year did they show their highest and lowest score?

# Before we dive into the questions, let's extract some preliminary data to get a better understanding of what we are dealing with. 

# Libraries and miscellaneous code imported to assist in our data analysis:

# In[2]:


# Imports for data 
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
from scipy.stats import normaltest
import scipy.stats as stats
import math

# Imports for vizualization 
import cufflinks as cf
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot

# Miscellaneous code
sns.set()
init_notebook_mode(connected=True)
cf.go_offline()
plt.rcParams['figure.figsize']=[10,6]


# Complete list of variables used:

# In[3]:


# Excel file used for analysis
data=pd.read_excel('data/data.xlsx')

# Global relative happiness from 'data'
# df_RelHap=data.groupby(['Relative Happiness']).count()[['Country']]

# Separating 'data' into the three different years: 2015,2016,2017
df_2015=data[data['Year']==2015]
df_2016=data[data['Year']==2016]
df_2017=data[data['Year']==2017]

# Display the columns in 'data'
columns=data.columns

groupby_country=data.groupby(by=['Country'])
groupby_region=data.groupby(by=['Region'])

# Finding the correlation coefficient between 'Economy','Happiness Score'
EcoVSHap_mat=data[['Economy','Happiness Score']].corr()
EcoVSHap_corr=EcoVSHap_mat['Economy'].loc['Happiness Score']

# Finding the correlation coefficient between 'Family','Happiness Score'
FamVSHap_mat=data[['Family','Happiness Score']].corr()
FamVSHap_corr=FamVSHap_mat['Family'].loc['Happiness Score']

# Finding the correlation coefficient between 'Health','Happiness Score'
HeaVSHap_mat=data[['Health','Happiness Score']].corr()
HeaVSHap_corr=HeaVSHap_mat['Health'].loc['Happiness Score']

# Finding the correlation coefficient between 'Freedom','Happiness Score'
FreVSHap_mat=data[['Freedom','Happiness Score']].corr()
FreVSHap_corr=FreVSHap_mat['Freedom'].loc['Happiness Score']

# Finding the correlation coefficient between 'Trust','Happiness Score'
TruVSHap_mat=data[['Trust','Happiness Score']].corr()
TruVSHap_corr=TruVSHap_mat['Trust'].loc['Happiness Score']

# Finding the correlation coefficient between 'Generosity','Happiness Score'
GenVSHap_mat=data[['Generosity','Happiness Score']].corr()
GenVSHap_corr=GenVSHap_mat['Generosity'].loc['Happiness Score']

# DataFrame of all the Correlation Coefficients 
df_corr=pd.DataFrame({'Happiness Factor':['Freedom','Economy',
                                          'Family','Health',
                                          'Trust','Generosity'],
                      'Hap Corr Coef':[FreVSHap_corr,EcoVSHap_corr,
                                       FamVSHap_corr,HeaVSHap_corr,
                                       TruVSHap_corr,GenVSHap_corr]})
df_corr1=df_corr.groupby('Happiness Factor')

# Pivot table of Region vs. average Happiness Score
piv_RegHap=pd.pivot_table(data,index='Region',values='Happiness Score',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Economy
piv_RegEco=pd.pivot_table(data,index='Region',values='Economy',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Family
piv_RegFam=pd.pivot_table(data,index='Region',values='Family',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Health
piv_RegHea=pd.pivot_table(data,index='Region',values='Health',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Freedom
piv_RegFre=pd.pivot_table(data,index='Region',values='Freedom',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Trust
piv_RegTru=pd.pivot_table(data,index='Region',values='Trust',
               aggfunc='mean',margins=True)

# Pivot table of Region vs. average Generosity
piv_RegGen=pd.pivot_table(data,index='Region',values='Generosity',
               aggfunc='mean',margins=True)

# Countries with the highest ever happiness score per region
df_max=pd.pivot_table(data=data,index='Region', 
                      values=['Country','Happiness Score'],
                      aggfunc='max')
filtered_max=data.loc[data['Happiness Score'].isin(
    df_max['Happiness Score'])].sort_values('Happiness Score',
    ascending=False)[['Country','Happiness Score','Year']]

# Countries with the lowest ever happiness score per region
df_min=pd.pivot_table(data=data,index=['Region'], 
                      values=['Country','Happiness Score'],
                      aggfunc='min')
filtered_min=data.loc[data['Happiness Score'].isin(
    df_min['Happiness Score'])].drop_duplicates(
    'Happiness Score').sort_values('Happiness Score'
    )[['Country','Happiness Score']]
df_min_1=data.loc[data['Happiness Score'].isin(
    df_min['Happiness Score'])].drop_duplicates('Region')

# ECDF
average_scores=groupby_country.mean().sort_values(
    by='Happiness Score',
    ascending=False)[['Happiness Score']]
average_high=((7.587+7.526+7.537)/3)
c_happiness_score=average_scores['Happiness Score']
ecdf_data=[]
df_ecdf=pd.DataFrame(ecdf_data)
x=np.sort(ecdf_data)
n=len(x)
y=np.arange(1,n+1)/n

# 25 random Happiness scores within 'data'
z_rand=[7.278, 6.867, 5.605, 6.81, 6.611, 3.781, 3.34, 7.039 ,5.771, 
5.517, 4.513, 7.212, 7.006, 5.822, 5.272, 4.119, 3.808, 2.693, 6.13,
7.2, 4.571, 4.514, 3.34, 6.778, 3.989,2.693, 5.971, 6.411, 5.389, 
5.335, 3.644, 5.132, 7.286, 5.303, 5.824, 3.989, 5.824, 5.429, 
2.693, 7.006]

# Finding the sum of all the values within z_rand
z_sum=sum(z_rand)

# Finding x-bar
x_bar=z_sum/40

# Number of rows in 'data'
num_pop=len(data.index)

# Finding mu
sum_happiness=sum(data['Happiness Score'])
mu=sum_happiness/num_pop

# STD of population 'Happiness Score'
sigma=data['Happiness Score'].std()

# Number of observations
n=40

# Solving for z-score
z=(x_bar-mu)/(sigma/math.sqrt(40))

# Values for hypothesis testing
alpha=1-0.95
pvalue=0.00000000263


# The data set used was from three CSV files from 
# 
# https://www.kaggle.com/unsdsn/world-happiness
# 
# The team downloaded the files, and compiled them into one, larger set of data.

# It was important to convert every 0 into NaN so that our results would not be skewed.

# In[4]:


# Importing data.xlsx
data=pd.read_excel('data/data.xlsx')

# Convert 0's into NaN 
data.replace(0,np.nan,inplace=True)
data.set_index('Year')


# In[5]:


# 'data' basic statistical details
data[['Happiness Score']].describe()


# In order for the team to grasp a more generalized, objective view of what happiness is, we separated each country into 3 possible categories, 'Relatively Happy', 'Relatively Unhappy', and 'Moderately Happy'. By reviewing the statistical details of 'data', we concluded that every country above 75% Happiness Score should be labeled, 'Relatively Happy'. Any country below 25% should be labeled, 'Relatively Unhappy'. And any nation in between would be labeled as 'Moderately Happy'. 

# In[6]:


# If Happiness Score is at or above 6.23375, 'Relatively Happy'
# If Happiness Score is at or below 4.509, 'Relavetly Unhappy'
# Any score in between, 'Moderately Happy'

def happiness(score):
    if score >= 6.23375:
        return 'Relatively Happy'
    if score <= 4.509:
        return 'Relatively Unhappy'
    else:
        return 'Moderately Happy'

# DataFrame of Happiness Score
happiness_scores=data['Happiness Score']
Relative_Happiness=[]

# Using a for loop to run the function on each Happiness Score
for h_score in happiness_scores:
    Relative_Happiness.append(happiness(h_score))

# Add the Relative Happiness column to the dataset
data['Relative Happiness']=Relative_Happiness
data.set_index('Year')


# In[7]:


# Number of coutries based on their Relative Happiness
df_RelHap=data.groupby(['Relative Happiness']).count()[['Country']]
df_RelHap


# - 25.1% of countries have a Happiness Score above the 75th percentile. (6.23375)
# - 25.1% of countries have a Happiness Score below the 25th percentile. (4.509)
# - 49.8% of countries have a Happiness Score in between.
# 
# So far, it may seem that Happiness Score is normally distributed. Let's continue investigating. 

# In[8]:


# Pie chart of Relative Happiness using 'data'
labels='Moderately Happy','Relatively Happy','Relatively Unhappy'
colors=['gold', 'yellowgreen', 'lightcoral']
explode=(0.01,0.05,0.025)

# Plotting piechart
plt.rcParams['figure.figsize']=[10,6]
plt.pie(df_RelHap,explode=explode,labels=labels,
        colors=colors,autopct='%1.1f%%',
        shadow=True, startangle=225)
plt.title('Percentage of Global Relative Happiness')
plt.show()


# We wanted to separate the 2015, 2016, and 2017 data so we could easily compare and contrast how the countries have changed over the years. This is easily represented by different choropleth graphs for each year, in which we would get into later. 

# In[8]:


# Separating 2015 from 'data'
df_2015=data[data['Year']==2015]
df_2015.set_index('Year').head()


# In[9]:


# 'df_2015' basic statistical details
df_2015[['Happiness Score']].describe()


# In[10]:


# Separating 2016 from 'data'
df_2016=data[data['Year']==2016]
df_2016.set_index('Year').head()


# In[11]:


# 'df_2016' basic statistical details
df_2016[['Happiness Score']].describe()


# In[12]:


# Separating 2017 from 'data'
df_2017=data[data['Year']==2017]
df_2017.set_index('Year').head()


# In[13]:


# 'df_2017' basic statistical details
df_2017[['Happiness Score']].describe()


# In[14]:


# Number of rows and columns within 'data'
data.shape


# In[15]:


# Number of rows and columns within 'df_2015'
df_2015.shape


# In[16]:


# Numer of rows and columns within 'df_2016'
df_2016.shape


# In[17]:


# Number of rows and columns within 'df_2017'
df_2017.shape


# In[18]:


# Columns within the DataFrame: data
columns=data.columns
for x in columns:
    print(x)


# Definition of columns:
# 
# Year - Year that is being researched (2015, 2016, or 2017)
# 
# Country - Country that is being researched
# 
# Region - Region of where the countries are located
# 
# Happiness Rank - Lower the value, the happier the country (1 being the highest) 
# 
# Happiness Score - Higher the value, the happier the country
# 
# Economy (GDP per capita) - Monetary value of finished goods and services. Higher the value, better the economy.
# - Job security
# - Livable wage
# - Cost of living
# 
# Family - How the citizens of a country value their family/friends, and how family bonds contribute to happiness. 
# - Who I can fall back on?
# - Trust in your family/friends
# - Quality relationships
# 
# Health - Quality of life citizens feel within their country that contributes to life expectancy.
# - Clean water
# - Health care
# - Pollution levels
# 
# Freedom - The higher the number, the more people feel they can make their own life choices without government intervention.
# - Absence of subjection
# - Voting rights
# - Freedom of speech
# 
# Trust - Trust in people, the government, and general society within the country. The higher the number, the more the citizens believe in the policies imposed by their government. 
# - Government transparency
# - Lack of corruption
# - Does the government have good intentions for the people or themselves?
# 
# Generosity - How generous the citizens are with other people or outsiders, such as tourists or complete strangers. 
# - Charity
# - Volunteering
# - Caring for tourists
# 
# Relative Happiness - Our way of quickly determining a country's level of happiness based on the scores of Economy, Family, Health, Freedom, Trust, and Generosity. 

# In[19]:


# Data type
data.info()


# After we separated the data into separate years, the group wanted to find out...
# ### Which happiness factor within our dataframe mostly contributes to a nation's overall happiness? And which countries exhibits it's highest and lowest scores?
# 
# In order for us to tackle this problem, we had to find out which category had the strongest correlation towards national happiness. On top of that, it is also important to know if this correlation was strong enough to propel the top country to 1st place in terms of happiness. (It is shown that 2014 is present within our data, however the team has verified that 2014 does not exist anywhere within the Excel spreadsheet.)

# In[20]:


# Groupby Country
groupby_country=data.groupby(by=['Country'])


# In[21]:


# Countries with the highest and lowest Economy
print(groupby_country.mean().sort_values(by='Economy',
                                         ascending=False).head()[['Economy']])
print(groupby_country.mean().sort_values(by='Economy',
                                         ascending=False).tail()[['Economy']])


# In[22]:


# Scatterplot of Economy vs. Happiness Score for all 3 years
sns.scatterplot(x='Economy',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Economy vs. Happiness Score')
plt.margins(0.084)

# Correlation Coefficient of Economy vs. Happiness Score
EcoVSHap_mat=data[['Economy','Happiness Score']].corr()
EcoVSHap_corr=EcoVSHap_mat['Economy'].loc['Happiness Score']
print("""
Economy vs. Happiness Score correlation coefficient:
{}
""".format(EcoVSHap_corr))


# In[23]:


# Countries with the highest and lowest score for Family
print(groupby_country.mean().sort_values(by='Family',
                                         ascending=False).head()[['Family']])
print(groupby_country.mean().sort_values(by='Family',
                                         ascending=False).tail()[['Family']])


# In[24]:


# Scatterplot of Family vs. Happiness Score for all 3 years
sns.scatterplot(x='Family',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Family vs. Happiness Score')
plt.margins(0.084)

# Correlation Coefficient of Family vs. Happiness Score
FamVSHap_mat=data[['Family','Happiness Score']].corr()
FamVSHap_corr=FamVSHap_mat['Family'].loc['Happiness Score']
print("""
Family vs. Happiness Score correlation coefficient:
{}
""".format(FamVSHap_corr))


# In[25]:


# Countries with the highest and lowest score for Health
print(groupby_country.mean().sort_values(by='Health',
                                         ascending=False).head()[['Health']])
print(groupby_country.mean().sort_values(by='Health',
                                         ascending=False).tail()[['Health']])


# In[26]:


# Scatterplot of Health vs. Happiness Score for all 3 years
sns.scatterplot(x='Health',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Health vs. Happiness Score')
plt.margins(0.081)

# Correlation Coefficient of Health vs. Happiness Score
HeaVSHap_mat=data[['Health','Happiness Score']].corr()
HeaVSHap_corr=HeaVSHap_mat['Health'].loc['Happiness Score']
print("""
Health vs. Happiness Score correlation coefficient:
{}
""".format(HeaVSHap_corr))


# In[27]:


# Which countries has the highest and lowest score for Freedom?
print(groupby_country.mean().sort_values(by='Freedom',
                                         ascending=False).head()[['Freedom']])
print(groupby_country.mean().sort_values(by='Freedom',
                                         ascending=False).tail()[['Freedom']])


# In[28]:


# Scatterplot of Freedom vs. Happiness Score for 3 years
sns.scatterplot(x='Freedom',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Freedom vs. Happiness Score')
plt.margins(0.081)

# Correlation Coefficient of Freedom vs. Happiness Score
FreVSHap_mat=data[['Freedom','Happiness Score']].corr()
FreVSHap_corr=FreVSHap_mat['Freedom'].loc['Happiness Score']
print("""
Freedom vs. Happiness Score correlation coefficient:
{}
""".format(FreVSHap_corr))


# In[29]:


#Countries with the most and least trust in their government
print(groupby_country.mean().sort_values(by='Trust',
                                         ascending=False).head()[['Trust']])
print(groupby_country.mean().sort_values(by='Trust',
                                         ascending=False).tail()[['Trust']])


# In[30]:


# Scatterplot of Trust vs. Happiness Score for all 3 years
sns.scatterplot(x='Trust',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Trust vs. Happiness Score')
plt.margins(0.081)

# Correlation Coefficient of Trust vs. Happiness Score
TruVSHap_mat=data[['Trust','Happiness Score']].corr()
TruVSHap_corr=TruVSHap_mat['Trust'].loc['Happiness Score']
print("""
Trust vs. Happiness Score correlation coefficient:
{}
""".format(TruVSHap_corr))


# In[31]:


# Countries with the most and least generous citizens
print(groupby_country.mean().sort_values(by='Generosity',
                                         ascending=False).head()[['Generosity']])
print(groupby_country.mean().sort_values(by='Generosity',
                                         ascending=False).tail()[['Generosity']])


# In[32]:


# Scatterplot of Generosity vs. Happiness Score for all 3 years
sns.scatterplot(x='Generosity',y='Happiness Score',data=data,hue='Year')
plt.title('Corr Coef: Generosity vs. Happiness Score')
plt.margins(0.081)

# Correlation Coefficient of Generosity vs. Happiness Score
GenVSHap_mat=data[['Generosity','Happiness Score']].corr()
GenVSHap_corr=GenVSHap_mat['Generosity'].loc['Happiness Score']
print("""
Generosity vs. Happiness Score correlation coefficient:
{}
""".format(GenVSHap_corr))


# In[33]:


# Countries with the highest and lowest happiness scores
print(groupby_country.mean().sort_values(by='Happiness Score',
                                         ascending=False).head()[['Happiness Score']])
print(groupby_country.mean().sort_values(by='Happiness Score',
                                         ascending=False).tail()[['Happiness Score']])


# In[34]:


# DataFrame of all the Correlation Coefficients 
df_corr=pd.DataFrame({'Happiness Factor':['Freedom','Economy',
                                          'Family','Health',
                                          'Trust','Generosity'],
                      'Hap Corr Coef':[FreVSHap_corr,EcoVSHap_corr,
                                       FamVSHap_corr,HeaVSHap_corr,
                                       TruVSHap_corr,GenVSHap_corr]})
df_corr1=df_corr.groupby('Happiness Factor')
df_corr1.mean()


# In[65]:


# Graph of what contributes to World happiness
df_corr.plot.bar(x='Happiness Factor',y='Hap Corr Coef')
plt.xticks(rotation=20,ha='center')
plt.title('Which Factor Contributes to World Happiness?')
plt.show()


# The potential of economic growth shows the largest contribution towards a country's overall happiness, while the selfless acts and giving spirit of a nation does not necessarily represent the joy of a nation. Qatar, Luxembourg, and Singapore are the top three in terms of economy prosperity; however, they are not the happiest nations in the world. Let's look further to investigate. 

# ### What are the happiest regions around the world from greatest to lowest?
# The best way to answer this was to first have a strong visualization of the happiness scores around the globe. Are there patterns we could gather based on visual representation?

# In[3]:


#Interactive Visualization of 2015 world happiness
choro_data_2015=dict(type='choropleth',
          colorscale='YlGnBu',
         locations=df_2015['Country'],
         z=data['Happiness Score'],
         text=df_2015['Happiness Rank'],
         colorbar={'title':'Happiness Score'},
         locationmode='country names')

layout_2015=dict(title='Happiness Score per Country in 2015',
           geo=dict(showframe=True,
                   projection={'type':'mercator'}))

choromap_2015=go.Figure(data=[choro_data_2015],layout=layout_2015)
iplot(choromap_2015,validate=False)


# In[4]:







#Interactive Visualization of 2016 world happiness
choro_data_2016=dict(type='choropleth',
          colorscale='YlGnBu',
         locations=df_2016['Country'],
         z=data['Happiness Score'],
         text=df_2016['Happiness Rank'],
         colorbar={'title':'Happiness Score'},
         locationmode='country names')

layout_2016=dict(title='Happiness Score per Country in 2016',
           geo=dict(showframe=True,
                   projection={'type':'mercator'}))

choromap_2016=go.Figure(data=[choro_data_2016],layout=layout_2016)
iplot(choromap_2016,validate=False)


# In[5]:


#Interactive Visualization of 2017 world happiness
choro_data_2017=dict(type='choropleth',
          colorscale='YlGnBu',
         locations=df_2017['Country'],
         z=data['Happiness Score'],
         text=df_2017['Happiness Rank'],
         colorbar={'title':'Happiness Score'},
         locationmode='country names')

layout_2017=dict(title='Happiness Score per Country in 2017',
           geo=dict(showframe=True,
                   projection={'type':'mercator'}))

choromap_2017=go.Figure(data=[choro_data_2017],layout=layout_2017)
iplot(choromap_2017,validate=False)


# It's really interesting to see Venezuela go from rank 23, 44, 82 throughout the three years... Without the three choropleth graphs, this would have been difficult to see. Makes you really wonder which other countries have large fluctuations in such a short amount of time. You may be able to make assumptions of the stability of a nation in comparison to their neighbors.

# Side note: After doing some personal research on how Venezuela dropped so significantly, I discovered that between the years 2015 and 2017, life expectancy drastically fell, as well as inflation and poverty soaring to new heights. This was in the middle of an opposition-led National Assembly attempting to overthrow their president, accusing him of lowering living standards and plunging the economy. The protests turned violent, and is currently affecting the nation today. 

# Now that we are able to visualize happiness around the globe, we noticed that there are distinctions between different regions of the world. So let's take what we see, and put it into numbers. 

#  

# In[72]:


# Groupby Region
groupby_region=data.groupby(by=['Region'])


# The farther you go down in the Region Happiness Score DataFrame, the smaller the values become. This is consistantly represented on the choropleth maps above. 

# In[73]:


# DataFrame that shows the average Happiness Score per region
groupby_region.mean().sort_values(by='Happiness Score',
                                         ascending=False)[['Happiness Score']]


# Let's turn the DataFrame into a visual

# In[74]:


# Standard Deviation of Region Happiness
print("Standard deviation of Region Happiness:")
print(data['Happiness Score'].std())

# Bar graph of average region happiness
piv_RegHap=pd.pivot_table(data,index='Region',values='Happiness Score',
               aggfunc='mean',margins=True)
piv_RegHap.plot(kind='bar')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Happiness Score')
plt.title('Region Happiness')
plt.ylim(0,8)
plt.show()


# Happiest regions from highest to lowest:
# 1. Australia and New Zealand
# 2. North America
# 3. Western Europe
# 4. Latin America and Caribbean
# 5. Eastern Asia
# 6. Middle East and Northern Africa
# 7. Central and Eastern Europe
# 8. Southeastern Asia
# 9. Southern Asia
# 10. Sub-Saharan Africa

# ### Which region harbors the best economy? Was economic correlation towards happiness strong enough to propel that region to 1st place in Happiness Score? Why or why not? 
# 
# Earlier, we determined that even though a country would have the highest Economy score, that does not necessarily mean they are the happiest country in the world. So, let's look into region. By investigating which region had the greatest to least scores per category, we were able to determine if economy was the sole factor of region happiness, respectively. 

# In[42]:


# Best to worst economies per region
groupby_region.mean().sort_values(by='Economy',
                                         ascending=False)[['Economy']]


# In[43]:


# Standard Deviation of Region vs. Economy
print("Standard deviation of Region vs. Economy:")
print(data['Economy'].std())

# Bar graph of average economic score per region
piv_RegEco=pd.pivot_table(data,index='Region',values='Economy',
               aggfunc='mean',margins=True)
piv_RegEco.plot(kind='bar',color='seagreen')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Economy')
plt.title('Region vs. Economy')
plt.ylim(0,1.6)
color='red'
plt.show()


# In[44]:


# Regions that value family and friends from highest to lowest
groupby_region.mean().sort_values(by='Family',
                                         ascending=False)[['Family']]


# In[45]:


# Standard Deviation of Region vs. Family 
print("Standard deviation of Region vs. Family:")
print(data['Family'].std())

# Bar graph of how each region values family and friends
piv_RegFam=pd.pivot_table(data,index='Region',values='Family',
               aggfunc='mean',margins=True)
piv_RegFam.plot(kind='bar',color='palevioletred')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Family')
plt.title('Region vs. Family')
plt.ylim(0,1.4)
plt.show()


# In[46]:


# Healthiest regions from best to worst
groupby_region.mean().sort_values(by='Health',
                                         ascending=False)[['Health']]


# In[47]:


# Standard Deviation of Region vs. Health
print("Standard deviation of Region vs. Health:")
print(data['Health'].std())

# Bar graph of a region's average health
piv_RegHea=pd.pivot_table(data,index='Region',values='Health',
               aggfunc='mean',margins=True)
piv_RegHea.plot(kind='bar',color='firebrick')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Health')
plt.title('Region vs. Health')
plt.ylim(0,1)
plt.show()


# In[48]:


# Most to least free regions
groupby_region.mean().sort_values(by='Freedom',
                                         ascending=False)[['Freedom']]


# In[49]:


# Standard Deviation of Region vs. Freedom
print("Standard deviation of Region vs. Freedom:")
print(data['Freedom'].std())

# Bar graph of each region's freedom score
piv_RegFre=pd.pivot_table(data,index='Region',values='Freedom',
               aggfunc='mean',margins=True)
piv_RegFre.plot(kind='bar',color='cornflowerblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Freedom')
plt.title('Region vs. Freedom')
plt.ylim(0,0.65)
plt.show()


# In[50]:


# Region's average trust towards their government
groupby_region.mean().sort_values(by='Trust',
                                         ascending=False)[['Trust']]


# In[51]:


# Standard Deviation of Region vs. Trust
print("Standard deviation of Region vs. Trust:")
print(data['Trust'].std())

# Bar graph of how trusting a region feels towards their government
piv_RegTru=pd.pivot_table(data,index='Region',values='Trust',
               aggfunc='mean',margins=True)
piv_RegTru.plot(kind='bar',color='coral')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Trust')
plt.title('Region vs. Trust')
plt.ylim(0,0.4)
plt.show()


# In[52]:


# Most and least generous regions towards others
groupby_region.mean().sort_values(by='Generosity',
                                         ascending=False)[['Generosity']]


# In[53]:


# Standard Deviation of Region vs. Generosity
print("Standard deviation of Region vs. Generosity:")
print(data['Generosity'].std())

# Bar graph of how generous a region is towards outsiders
piv_RegGen=pd.pivot_table(data,index='Region',values='Generosity',
               aggfunc='mean',margins=True)
piv_RegGen.plot(kind='bar',color='m')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Generosity')
plt.title('Region vs. Generosity')
plt.ylim(0,0.5)
plt.show()


# The happiest region in the world is the Australia and New Zealand area. However, they are ranked 3rd in economy. Economy is the strongest contributor towards happiness, however, even though they are ranked 3rd in economy, they are 1st place in every other category. This means that although economic growth is happiness' greatest factor, it is much more important to be stronger in every other category. 

# ### What are the happiest and unhappiest countries per region? And which year did they show their highest and lowest score?

# We noticed that there are parts of the world that are obviously having a harder time than other parts of the world. Let's look at the below boxplot to better visualize the disparity. 

# It's interesting to see that the Middle East and Northern Africa have 
# such a large disparity of happiness. Western Europe, even though they
# are considered one of the happiness regions in the world, have scores
# that dip pretty low in comparison to their neighbors. Two of the unhappiest regions, Sub-Saharan Africa and Southern Asia, have countries that are happier than some of the unhappiest nations in Western Europe. What is really interesting to note is that the Sub-Saharan Africa region harbors both the lowest median and overall scores for happiness. Unfortunately, there are not  many outliers, which means that it is a steady decline within that entire area. 

# In[54]:


# Boxplot of Happiness Scores per region
plt.figure(figsize=(16,6))
sns.boxplot(x='Region',y='Happiness Score',data=data,hue='Year')
plt.xticks(rotation=45,ha='right')
plt.title('Region Happiness')
plt.show()


# In[55]:


# Countries with the highest ever happiness score per region
df_max=pd.pivot_table(data=data,index='Region', 
                      values=['Country','Happiness Score'],
                      aggfunc='max')

filtered_max=data.loc[data['Happiness Score'].isin(
    df_max['Happiness Score'])].sort_values('Happiness Score',
    ascending=False)[['Country','Happiness Score','Year']]

filtered_max.set_index(data['Region'].drop_duplicates())


# In[56]:


#Countries with the lowest ever Happiness Score per region
df_min=pd.pivot_table(data=data,index=['Region'], 
                      values=['Country','Happiness Score'],
                      aggfunc='min')

filtered_min=data.loc[data['Happiness Score'].isin(
    df_min['Happiness Score'])].drop_duplicates(
    'Happiness Score').sort_values('Happiness Score'
    )[['Country','Happiness Score']]

filtered_min.set_index(data['Region'].drop_duplicates())

df_min_1=data.loc[data['Happiness Score'].isin(
    df_min['Happiness Score'])].drop_duplicates('Region')

pd.pivot_table(data=df_min_1, index='Region', 
               values=['Country','Happiness Score','Year'], 
               aggfunc='min').sort_values('Happiness Score',
                                          ascending=False)


# Happiest nation in:
#     1. Western Europe: Switzerland, 2015
#     2. North America: Canada, 2015
#     3. Australia and New Zealand: New Zealand, 2016
#     4. Middle East and Northern Africa: Israel, 2015
#     5. Latin America and Caribbean: Costa Rica, 2015
#     6. Southeastern Asia: Singapore, 2015
#     7. Central and Eastern Europe: Czech Republic, 2017
#     8. Eastern Asia: Taiwan, 2017
#     9. Sub-Saharan Africa: Mauritius, 2016
#     10. Southern Asia: Pakistan, 2017
# 
# Unhappiest nation in:
#     1. Western Europe: Greece, 2015
#     2. North America: United States, 2017
#     3. Australia and New Zealand: Australia, 2017
#     4. Middle East and Northern Africa: Syria, 2015
#     5. Latin America and Caribbean: Haiti, 2017
#     6. Southeastern Asia: Cambodia, 2015
#     7. Central and Eastern Europe: Ukraine, 2017
#     8. Eastern Asia: Mongolia, 2015
#     9. Sub-Saharan Africa: Central African Republic, 2015
#     10. Southern Asia: Afghanistan, 2016

# #### After analyzing the data, the team gathered enough evidence to determine if all the Happiness Scores within 'data' presented a normal distribution. Let's look into the numbers below to see the fate of our null hypothesis.
# 
# This ECDF graph tells us that there is no utopia around the world that is completely out of reach with another nation. On average, Switzerland is the happiest nation in the world (based on our 2015-2017 data), but there is a steady decline in happiness all the way to the average unhappiest nation, Burundi. 

# In[57]:


# ECDF
average_scores=groupby_country.mean().sort_values(by='Happiness Score',
                                         ascending=False)[['Happiness Score']]

# Average of the highest Happiness Score for the three years
average_high=((7.587+7.526+7.537)/3)

# List of Happiness Scores
c_happiness_score=average_scores['Happiness Score']

ecdf_data=[]
# Divide the happiness score of each country by average highest Happiness Score
for c in c_happiness_score:
    ecdf_data.append(c/average_high)
    
df_ecdf=pd.DataFrame(ecdf_data)

x=np.sort(ecdf_data)
n=len(x)
y=np.arange(1,n+1)/n

plt.plot(x,y,marker='.',ls='none')
plt.xlabel('Percentage of countries unhappier than the highest average x100')
plt.ylabel('ECDF')
plt.show()


# By finding the value of a single z-score, we are able to see how many standard deviations we are away from the mean of happiness. By having a score of approximately -0.182, our random point did not deviate too far away from the mean.  

# In[58]:


# Discovering a z-value

# 25 random Happiness scores within 'data'
z_rand=[7.278, 6.867, 5.605, 6.81, 6.611, 3.781, 3.34, 7.039 ,5.771, 
5.517, 4.513, 7.212, 7.006, 5.822, 5.272, 4.119, 3.808, 2.693, 6.13, 
7.2, 4.571, 4.514, 3.34, 6.778, 3.989,2.693, 5.971, 6.411, 5.389, 
5.335, 3.644, 5.132, 7.286, 5.303, 5.824, 3.989, 5.824, 5.429, 
2.693, 7.006]

# Finding the sum of all the values within z_rand
z_sum=sum(z_rand)

# Finding x-bar - sample mean
x_bar=z_sum/40
print('''x-bar: 
{}'''.format(x_bar))

# Number of rows in 'data'
num_pop=len(data.index)

# Finding mu - population mean
sum_happiness=sum(data['Happiness Score'])
mu=sum_happiness/num_pop
print('''
mu: 
{}'''.format(mu))

# STD of population 'Happiness Score'
sigma=data['Happiness Score'].std()
print('''
sigma: 
{}'''.format(sigma))

# Number of observations
n=40
print('''
number of observations:
{}'''.format(n))

# Solving for z-score
z=(x_bar-mu)/(sigma/math.sqrt(40))
print('''
z-score:
{}'''.format(z))


# In[59]:


# Determining pvalue
print(normaltest(data['Happiness Score']))

# Distribution of Happiness Score
sns.distplot(data['Happiness Score'],fit=stats.norm,kde=True,hist=True)
plt.title("Distribution of Happiness Score")
plt.show()


# 95% confidence level; 
# 1-0.95 = 0.05;
# alpha=0.05
# 
# 0.05/2 = 0.025 are the critical values
# 
# pvalue = approx. 2.628e-09
# 
# If p > alpha, fail to reject null hypothesis
# 
# If p <= alpha, reject null hypothesis

# In[60]:


# Testing the hypothesis

# 95% confidence level
alpha=1-0.95
pvalue=0.00000000263

if pvalue <= alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# Because our probability value is less than our alpha value, our null hypothesis is rejected. 
# 
# ### In conclusion...
# ### A normal distribution is NOT present within the Happiness Score for all the countries for the collective years of 2015, 2016, and 2017.

# Curious about the happiness rank of your favorite country? Ask us!

# In[9]:


data.loc[data['Country']=='Germany'][['Happiness Rank']].mean()


# In[ ]:




