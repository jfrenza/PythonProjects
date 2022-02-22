#!/usr/bin/env python
# coding: utf-8

# ## TV Shows and movies listed on Netflix

# **This dataset consists of TV shows and movies available on Netflix as of 2019. The dataset is collected from Flixable which is a third-party Netflix search engine.**

# **Your task: Create a dashboard that will help the Marketing manager at Flixable understand the content available as of 2019. You are free to create it in a platform and format of your choosing, where you can answer the following questions.**
# 
# 
# Has Netflix been increasingly focusing on TV rather than movies in recent years?
# 
# What is the average length of movies?
# 
# What is the most popular category per country?
# 
# Have overall releases increased or decreased over time? Which year had more releases?
# 
# Who are the top five most famous actors in TV shows or movies in terms of number of casted movies or TV shows? 
# 
# Is there a connection between the rating and the category that the movie or TV show has been listed in?
# 

# In[96]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')


# **Firstly, the Pandas, Numpy and Matplotlib modules were imported; those will help to clean and analyse the data as well as create images that will help to understand its content and distribution**
# 
# **Additionally, I've used the pandas tool read_csv to charge the dataset that was provided**

# In[97]:


df.info()


# **I've used .info() to better understand the dataset; using this method, .info(), it can be seen that the dataset  has some blank spaces, as well as the number of columns, their names and the data type for each one of them.**

# ### Has Netflix been increasingly focusing on TV rather than movies in recent years?

# In[98]:


df['Split_List'] = df.date_added.str.split(',')

df['Year_added'] = df.Split_List.str.get(1)


# In[99]:


Movies = df[df.type == 'Movie']
TV_shows = df[df.type == 'TV Show'] 

TV_shows_g = TV_shows.groupby(['Year_added'])['type'].count()

TV_shows_g['2009'] = 0
TV_shows_g['2010'] = 0
TV_shows_g['2011'] = 0
TV_shows_g['2012'] = 0
                              


# In[507]:


fig1,ax1 = plt.subplots(figsize = (14, 4), facecolor = 'white')

plt.title('Movies Vs TV Shows over the years',
         fontdict = {'fontsize': 15, 'color': 'black', 
                     'fontweight': 'bold'})

Labels_Year = ['2008','2009','2010','2011',
               '2012','2013','2014','2015',
               '2016','2017','2018','2019',
               '2020','2021']

plt.plot(Labels_Year, Movies.groupby(['Year_added'])['type'].count(),
        marker = 'D',
        label = 'Movies')

plt.plot(Labels_Year, TV_shows_g, marker = 'D',
        label = 'TV Shows')



plt.legend()
plt.savefig('Movies_Shows_overyears.png')
plt.show()


# ***Firstly, the data was cleaned. Date realeased was split to extract the year, afterwords plot so the differences are seen between movies and Tv shows over the years***

# ### What is the average length of movies?

# In[115]:


df['split_duration'] = df.duration.str.split(" ")
df['duration_minutes'] = df.split_duration.str.get(0)
df.duration_minutes = df.duration_minutes.astype('int')

Movies_Duration = df[df.type == 'Movie']

Movies_Duration_Average = round(np.average(Movies_Duration.duration_minutes),2)

print(f'The average length of movies is: {Movies_Duration_Average} minutes')


# ***The duration was split as the data type was an string;therefore, it wasn't possible to calculate the average, after the number was extracted the data type was changed from string to integer and finally the numply method: np.average was used to calculate the mean***

# ### What is the most popular category per country?

# In[530]:


popular_category = df.groupby(['country','listed_in'], as_index = False)['show_id'].count()

popular_category.sort_values(by='show_id', ascending=False, ignore_index=True, inplace = True)

popular_category.columns=['Country','Category','Count']

popular_category.head(20)


# ### Have overall releases increased or decreased over time? Which year had more releases?

# In[364]:


data = df.groupby(by ='release_year',
                  as_index = False)['show_id'].count().sort_values(by = 'release_year',
                                                                   ascending=False)


# In[508]:


fig1,ax3 = plt.subplots(figsize =(14,4), facecolor = 'white')

plt.title('Overal releases',
         fontdict= {'fontsize':15,
                    'color':'black',
                   'fontweight':'bold'})

hbars = ax3.bar(data.release_year,data.show_id)

ax3.set_xlabel = 'Years'

plt.savefig('Overall Releases.png')

plt.show()


# In[381]:


sorted_data = data.sort_values(by='show_id', ascending=False, ignore_index = True)

print(f'The year that had most releases was: {sorted_data.release_year[0]}')


# ### Who are the top five most famous actors in TV shows or movies in terms of number of casted movies or TV shows?

# In[455]:


Cast = df.dropna()

Cast = Cast.cast.apply(lambda x: str(x).split(',')).tolist()

Actors = []

for lst in Cast:
    for actor in lst:
        Actors.append(actor)


# In[533]:


df_Actors = pd.DataFrame(Actors)

df_Actors.columns =['Actors']

df_Actors = Df_Actors.groupby('Actors')['Actors'].count()

sorted_actors = df_Actors.sort_values(ascending = False)

print('The top five most famous actors are: ')

sorted_actors.index[0:5]


# ### Is there a connection between the rating and the category that the movie or TV show has been listed in?

# In[536]:


rating_category = df.groupby(['rating','listed_in'], as_index = False)['show_id'].count()

rating_category.sort_values(by='show_id', ascending=False, ignore_index=True, inplace = True)

rating_category.columns=['Rating','Category','Count']

rating_category.tail(20)

