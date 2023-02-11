#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
# get_ipython().system('{sys.executable} -m pip install pandas')


# In[2]:


# get_ipython().system('{sys.executable} -m pip install requests')


# In[8]:


# get_ipython().system('{sys.executable} -m pip install pandasql')


# In[18]:


import random

# In[3]:


import pandas as pd
import numpy as np
import requests
import requests_cache
import json
import time

# fetching the data

dict = {'limit': 1000, 'page': 1, 'min_score': 6.8}
# s = requests.Session()
requests_cache.install_cache()
data_item = requests.get("https://api.jikan.moe/v4/anime/", dict).json()
# print(my_data['data'][0]['title'])
# print(data_item['pagination']['has_next_page'])
anime_data = [data_item]
# while True:
#     if data_item['pagination']['has_next_page'] == True:
#         print(dict['page'] )
#         dict['page'] += 1
#         data_item = requests.get("https://api.jikan.moe/v4/anime/", dict).json()
#         anime_data.append(data_item)
#         print('hi')
#     else:
#         break
j = 0
# for i in range(1, 50):
while data_item['pagination']['has_next_page'] == True:
    dict['page'] += 1
    try:
        time.sleep(1)
        r = requests.get("https://api.jikan.moe/v4/anime/", dict)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    data_item = r.json()
    # print(dict['page'])
    # print(data_item.keys())
    anime_data.append(data_item)

# print(len(anime_data))
# print(type(my_data['data']))

# building a data frame
df = pd.DataFrame(
    columns=["title", "title japanese", "title_synonyms", "a_type", "genre", "episodes", "status", "duration",
             "score", "season", "year"])
for item in anime_data:
    for anime in item['data']:
        j += 1
        title = anime['title']
        title_japanese = anime['title_japanese']
        title_synonyms = anime['title_synonyms']
        a_type = anime['type']
        episodes = anime['episodes']
        status = anime['status']
        duration = anime['duration']
        score = anime['score']
        season = anime['season']
        year = anime['year']
        try:
            genres = anime['genres'][0]['name']
        except IndexError:
            genres = 'null'

        # print('sno', j)
        # print(title)
        # print(title_synonyms)
        # print(duration)
        # print(genres)
        # print(score)

        # saving to the data frame df

        df = df.append({'title': title, 'title_japanese': title_japanese, 'title_synonyms': title_synonyms,
                        'a_type': a_type, 'genre': genres, 'episodes': episodes, 'status': status, 'duration': duration,
                        'score': score, 'season': season, 'year': year}, ignore_index=True)

# In[6]:


# df.head(70)


# In[18]:


#import difflib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


# In[5]:


# get_ipython().system('{sys.executable} -m pip install sklearn')


# In[14]:


# features for recommendation
selected_features = ['a_type', 'genre']

# In[15]:


# removing null values of selected features
for feature in selected_features:
    df[feature] = df[feature].fillna('')
    if df[feature] is None:
        df[feature] = df[feature].fillna('')

# In[15]:


# string of selected features combined
# combined_features = df['a_type']+df['genre']+df['episodes'].apply(str)
# print(combined_features)


# In[20]:


# vectorizer = TfidfVectorizer()
# converting to vector
# feature_vectors = vectorizer.fit_transform(combined_features)
# getting similarity scores using cosine similarity
# similarity =  cosine_similarity(feature_vectors)
# print(similarity.shape)


# In[3]:


# r_df = df.query('score>8')


# In[4]:


# r_df.head()


# In[21]:


# changing datatype to int

df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
df = df.replace(np.nan, 0, regex=True)
df['episodes'] = df['episodes'].astype(int)

# In[22]:


# getting input
u_type = ''
u_genre = ''
u_episodes = ''
# u_type = input('choose TV / Movie')
# print(type(df['genre']))
# genre_list = set(df['genre'])
u_episodes = 0


def input_tv(ep):
    tv_df = df.query('a_type == "TV"')
    global u_type
    u_type = 'TV'
    global u_episodes
    u_episodes = ep
    # print(u_episodes)
    if u_episodes.isdigit():

        u_episodes = int(u_episodes)
    else:
        u_episodes = max(list(tv_df["episodes"].apply(int)))
    # u_genre = input(f'choose a genre {set(tv_df["genre"])}')
    return set(tv_df["genre"])


def input_mv():
    global u_type
    u_type = 'Movie'
    mv_df = df.query('a_type == "Movie"')
    # u_genre = input(f'choose a genre {set(mv_df["genre"])}')
    global u_episodes
    u_episodes = max(list(mv_df["episodes"]))
    return u_episodes, set(mv_df["genre"])


def input_genre(name):
    global u_genre
    u_genre = name


# print(type(u_episodes))


# In[21]:


# df.dtypes


# In[23]:


# retrieving required data
def result_data():
    print(u_type, u_episodes, u_genre)
    req_data = df.query('a_type == @u_type and genre==@u_genre and episodes< @u_episodes')
    # print(req_data.head())
    # using loc to return record based on the label(index)
    # example: if df contains 2,4,5,6.. 6 is the label and 4 is the position ; position 6 is out of bounds
    print(req_data.loc[[random.choice((list(req_data.index.values)))]].values.tolist())
    return req_data.loc[[random.choice((list(req_data.index.values)))]]

# In[24]:


# In[26]:


# li = list(req_data.index.values)
# print(li)
# r = random.choice(li)
# print(r)
# req_data.loc[[r]]


# In[ ]:
