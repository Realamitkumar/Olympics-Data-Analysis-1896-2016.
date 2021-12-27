#!/usr/bin/env python
# coding: utf-8

# # Welcome to Olympics Data Analysis 1896-2016 Rio Di Jenerio

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Load Our Dataset
ath=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')


# In[223]:


ath.min()


# In[44]:


#Join the dataframes or Merge the dataframe

ath=ath.merge(region_df,on='NOC',how='left')


# In[45]:


ath.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'],inplace=True)


# In[46]:


#Shape of our merged Dataset
ath.shape


# In[47]:


#Here there is a problem which is many of the column
#whose name is start with lower case so
#we have to convert that into upper case
ath.rename(columns={'region':'Region','notes':'Notes'},inplace=True)


# In[48]:


#Let's see the statistical behaviour of our data
#by applying describe() function
#But this will us only analysis about numeric columns
ath.describe()


# In[49]:


ath.isnull().sum()

# So here we have missing values in around 6 columns


# In[50]:


ath['Age'].unique().tolist() #You can see the nan values here


# In[51]:


#players from india
india_1=ath.query('Team == "India"')


# In[52]:


india_1.head(10)


# In[53]:


india_1.shape #So 1400 players are from india


# In[54]:


#Top countries participating
top_country=ath.Team.value_counts().sort_values(ascending=False).head(10)


# In[55]:


top_country


# In[56]:


#let's make a bar graph of top 10 countries
plt.figure(figsize=(14,4))
sns.barplot(x=top_country.index,y=top_country,palette='Set2');
plt.title('Top Participation Nation')


# In[57]:


##On the basis of Summer i want to filter out our data
ath_summer=ath[ath['Season']=='Summer']


# In[58]:


#Top_10 Participating countries who is participated in summer 
ath_10_Participated=ath_summer.Team.value_counts().sort_values(ascending=False).head(10)


# In[61]:


#let's make a bar graph of top 10 countries participated in Summer
plt.figure(figsize=(14,7))
plt.title('Top_10 Participated Nation In Summer')
sns.barplot(x=ath_10_Participated.index,y=ath_10_Participated,palette='Set3')


# In[62]:


ath['Age'].fillna


# In[63]:



ath_age=ath[ath['Age']>21.0]


# In[64]:


#Age Distribution Of the participants Whose Age>21yrs
plt.figure(figsize=(14,7))
plt.xlabel('Age')
plt.ylabel('No. Of Participants')
plt.title('Age Distribution Of The Athletes')
plt.hist(ath_age.Age,bins=(10), color='orange',edgecolor='red');


# In[65]:


#On the basis of Winter i want to filter out our data
ath_winter=ath[ath['Season']=='Winter']


# In[66]:


ath_winter.shape #In winter there were 48564 participated


# In[67]:


#Top_10 Participating countries who is participated in Winter
ath_10_winter=ath_winter.Team.value_counts().sort_values(ascending=False).head(10)


# In[68]:


ath_10_winter #These are the countries who were participated in winter


# In[109]:


#let's make a bar graph of top 10 countries participated in Winter
plt.figure(figsize=(14,7))
plt.title('Top_10 Participated Nation In Winter')
sns.barplot(x=ath_10_winter.index,y=ath_10_winter,palette='Set3')
plt.xlabel("Country's")
           


# In[110]:


#Summer Olympics Sports
ath_summer_sports=ath[ath['Season']=='Summer'].Sport.unique()


# In[111]:


ath_10_summer=ath_summer.Sport.value_counts().sort_values(ascending=False).head()


# In[112]:


#let's make a bar graph of top 10 sports happened in summer
plt.figure(figsize=(14,7))
plt.title('Top_10 sports happened In Summer')
sns.barplot(x=ath_10_summer.index,y=ath_10_summer,palette='Set3')
plt.ylabel('Teams Participated')
plt.xlabel('Sports')


# In[113]:


ath_winter=ath[ath['Season']=='Winter']


# In[114]:


#Winter Olympics Sports
ath_winter_sports=ath[ath['Season']=='Winter'].Sport.unique()


# In[115]:


ath_10_winter=ath_winter.Sport.value_counts().sort_values(ascending=False).head()


# In[116]:


#let's make a bar graph of top 10 sports happened in summer
plt.figure(figsize=(14,7))
plt.title('Top_10 sports happened In Winter')
sns.barplot(x=ath_10_winter.index,y=ath_10_winter,palette='Set3')
plt.ylabel('Teams Participated')
plt.xlabel('Sports')


# In[117]:


#Male and Female Participants
gender_counts=ath['Sex'].value_counts()
gender_counts


# In[118]:


#pie plot for male and female athletes
plt.figure(figsize=(12,7))
plt.title('Gender Distribution')
plt.pie(gender_counts,labels=gender_counts.index,autopct='%1.1f%%',startangle=150,shadow=True);


# In[119]:


ath['Medal'].value_counts()


# In[127]:


#One hot encoding 
ath_medals=pd.concat([ath,pd.get_dummies(ath['Medal'])],axis=1)


# In[128]:


#Total Medals
ath_medals['Total Medals']=ath_medals['Gold']+ath_medals['Silver']+ath_medals['Bronze']


# In[148]:


#Total No. Of Female Athletes in each olympics incase of Summer 
female_ath=ath[(ath.Sex=='F') & (ath.Season=='Summer')][['Sex','Year']]
female_ath=female_ath.groupby('Year').count().reset_index()
female_ath.head()


# In[150]:


#Total No. Of Female Athletes in each olympics incase of Winter
female_ath=ath[(ath.Sex=='F') & (ath.Season=='Winter')][['Sex','Year']]
female_ath=female_ath.groupby('Year').count().reset_index()
female_ath.head()


# In[151]:


female_olymp=ath[(ath.Sex=='F') & (ath.Season=='Summer')]


# In[153]:


import seaborn as sns


# In[158]:


sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
sns.countplot(x='Year',data=female_olymp,palette='Spectral')
plt.title('Women Participation Incase Of Summer')


# In[159]:


female_olympWin=ath[(ath.Sex=='F') & (ath.Season=='Winter')]


# In[160]:


sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
sns.countplot(x='Year',data=female_olymp,palette='Spectral')
plt.title('Women Participation Incase Of Winter')


# In[162]:


part=female_olympWin.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()
plt.title('Plot Of Female Athletes Over Time Incase Of Winter Season')


# In[163]:


#let's see the athletes whoes is more than 50
more_ath=ath['Sport'][ath['Age']>50]
more_ath


# In[175]:


plt.figure(figsize=(12,6))
plt.title('Sports Played Whoes Age>50')
sns.barplot(x=more_ath.index,y=more_ath,palette='Set3')
plt.xlabel('Age')
plt.ylabel('Sports')


# In[177]:


#Athletes who won Gold medal
gold_guy=ath[(ath.Medal=='Gold')]


# In[181]:


gold_guy


# In[184]:


# Athletes over 50 years age won how may golds
gold_guy['ID'][gold_guy['Age']>50].count()


# In[191]:


gold_sports=gold_guy['Sport'][gold_guy['Age']>50]


# In[192]:


gold_sports


# In[218]:


#Olympics

max_year=ath.Year.max()
print(max_year)

name_teams=ath[(ath.Year==max_year)&(ath.Medal=='Gold')]
name_teams.head(10)


# # So Our Olympic Data Analysis  Finished I Hope It Was Informative and Insights Full.
