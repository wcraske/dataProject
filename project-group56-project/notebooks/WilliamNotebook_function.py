#!/usr/bin/env python
# coding: utf-8

# # William Craske

# ## Research question/interests
# 
# Finding the likelihood or trend of scoring when on a power play or down a player, compared to whether it's the winning goal.
# 

# In[1]:


import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns


nhlStats = pd.read_csv(r"..\data\raw\nhlStats.csv", low_memory = False)
nhlStats = nhlStats.dropna(how="any", axis = 0)
nhlStats


# # Milestone 3
# 

# In[2]:


nhlStats.head()


# In[3]:


nhlStats.shape


# In[4]:


nhlStats.columns


# In[5]:


nhlStats.nunique(axis=0)
nhlStats.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))


# In[6]:


nhlStats.index


# In[7]:


nhlStats.info()


# In[8]:


nhlStats.isnull().sum()


# In[64]:


sns.set_style('darkgrid')

vis1 = sns.catplot(data = nhlStats[nhlStats['goals'] > 0], x='game_id', y = 'saves', kind = "bar")
vis1.set_axis_labels("succesful saves", "game ID")

#shows succesful saves in each game where there were more than 1 goal


# In[11]:


nhlStats.columns


# In[11]:


nhlStats.columns


# In[57]:


sns.set_theme(style="whitegrid")
sns.set(font_scale = .6)

vis2 = sns.countplot(data = nhlStats[nhlStats['game_id'] > 2.018030e+09], x='evenShotsAgainst')
vis2.set_xticklabels(vis2.get_xticklabels(), rotation=75, horizontalalignment='right')
vis2.set_xticklabels(['{:.2f}'.format(float(t.get_text())) for t in vis2.get_xticklabels()])
vis2
#showsaverage of shots against when even strength and after 2018


# In[70]:


vis3 = sns.lineplot(data = nhlStats[nhlStats['game_id'] > 2.019030e+09], x='game_id', y = 'gameWinningGoal')

#graph of game winning goals after 2019


# In[86]:


#task 2

nhlStats = pd.read_csv(r"..\data\raw\nhlStats.csv", low_memory = False)

nhlStats = nhlStats.dropna(how="any", axis = 0)

nhlStats = nhlStats.rename(columns = {"game_id" : "gameID", "player_id" : "playerID",
                                      "team_id" : "teamID", "pim" : "penaltyMins",
                                      "shortHandedShotsAgainst" : "shShotsAgainst",
                                      "play_id" : "playID", "decision" : "result"})


nhlStats = nhlStats[['gameID','gameWinningGoal',
       'powerPlayShotsAgainst','goals','timeOnIce', 'assists',
       'penaltyMins', 'shots', 'saves', 'powerPlaySaves', 'shortHandedSaves',
       'evenSaves', 'shShotsAgainst', 'evenShotsAgainst', 'result', 'savePercentage',
       'powerPlaySavePercentage', 'evenStrengthSavePercentage', 'playID',
       'strength','emptyNet']]

nhlStats = nhlStats.sort_values(by=["gameID"], ascending = False)

nhlStats


# In[88]:


def loadAndProcess(address):
    
    #method chain 1 - load data, deal with missing data
    df1 = (
        pd.read_csv(address, low_memory = False)
        .dropna(how="any", axis = 0)
        
    )
    
    #method chain 2 - rename columns, and sort by gameID
    df2 = (
        df1
        .rename(columns = {"game_id" : "gameID", "player_id" : "playerID",
                                      "team_id" : "teamID", "pim" : "penaltyMins",
                                      "shortHandedShotsAgainst" : "shortHandShotsAgainst",
                                      "play_id" : "playID", "decision" : "result"})
        .sort_values(by=["gameID"], ascending = False)
        
    )
    #method chain 3 - drop columns that wont be used in research question
    df3 = (
        df2
        .drop(['playerID', 'teamID', 'timeOnIce', 'goals',
               'playID', 'emptyNet'], axis=1)
    )
    return df3


    


# In[ ]:




