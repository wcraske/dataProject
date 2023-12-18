#!/usr/bin/env python
# coding: utf-8

# # Rhys Elliott

# ## Research question/interests
# 
# One of the most important aspects obeing a NHL goalies is being able to perform under pressure.  I will analyze which NHL goalies have the highest save rate while shorthanded and comparing it to their even strength save percentage.  Their "clutch factor"  will also be compared to their win rate to give an idea of how key of a role they played in their victories.s.

# In[6]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

APINHLStatistics = pd.read_csv("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742", low_memory=False)
APINHLStatistics = APINHLStatistics.dropna()
APINHLStatistics


# # Milestone 3

# Task 1

# In[34]:


APINHLStatistics.columns


# In[35]:


APINHLStatistics.shape


# In[36]:


APINHLStatistics.head()


# In[37]:


APINHLStatistics.index


# In[38]:


type(APINHLStatistics)


# In[39]:


APINHLStatistics.info()


# In[40]:


APINHLStatistics['decision']


# In[41]:


subset = APINHLStatistics[['game_id', 'shots', 'saves']]
subset


# In[44]:


APINHLStatistics.loc[APINHLStatistics['decision'] == 'W', ['shots', 'saves']]


# In[46]:


APINHLStatistics.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))


# Task 2

# In[170]:


APINHLStatistics = pd.read_csv("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742", low_memory=False)
APINHLStatistics = APINHLStatistics.dropna()

APINHLStatistics["PKSave%"] = (
    APINHLStatistics["shortHandedSaves"] / APINHLStatistics["shortHandedShotsAgainst"]
                              )*100


# In[171]:


APINHLStatistics = APINHLStatistics.rename(columns = {'powerPlaySavePercentage': 'PPSave%',
                                                      'evenStrengthSavePercentage': 'evenSave%',
                                                      'player_id': 'playerID',
                                                      'game_id': 'gameID'
                                                     }
                                          )


# In[174]:


APINHLStatistics = APINHLStatistics[['playerID', 'PPSave%', 'PKSave%', 'evenSave%']]
APINHLStatistics.sort_values(by=["PKSave%"], ascending = False)
APINHLStatistics.groupby('playerID').mean()


# Task 3

# In[7]:


def load_and_process(url):
    """
    first line: loading my dataset to the dataframe
    second line: dropping any lines that contain NaN values. Can't use these to rank goalies.
    """
    df1 = (
            pd.read_csv(url, low_memory = False)
            .dropna()
            )
    
    """
    first line: rename some columns so they are more readable
    second line: combining the goalies by their numbers.  then averages out all of their stats across games.
    third line: creates a new columns "PKSavePercentage". combines shortHandedShotsAgainst and
    shortHandedSaves to get their save percentage on the penalty kill.
    fourth line: drops columns that won't be useful for the final analysis.
    fifth line: sorts from highest penalty kill save percentage to lowest.
    """
    df2 = (
           df1
            .rename(columns = {'powerPlaySavePercentage': 'PPSave%',
                              'evenStrengthSavePercentage': 'evenSave%',
                              'player_id': 'playerID',
                              'game_id': 'gameID'})
            .groupby('playerID').mean()
            .assign(PKSavePercentage=lambda x:(x.shortHandedSaves/x.shortHandedShotsAgainst)*100) 
            .drop(['gameID', 'team_id', 'timeOnIce', 'assists', 'goals',
                   'pim', 'shots', 'saves', 'powerPlaySaves', 'shortHandedSaves',
                   'evenSaves', 'shortHandedShotsAgainst', 'evenShotsAgainst',
                   'powerPlayShotsAgainst'], axis=1)
            .sort_values(by=["PKSavePercentage"], ascending = False)
        )
   
    """
    first line: drop any PKSavePercentages (our new column) that has NaN values
    second line: goalies with 100% PKSavePercentages is impossible if they've played enough games
    in order to get rid of these, for example, backup goalies who have played few games and whose 
    data is skewed, we will filter out anybody with a 100% save rate on the penalty kill
    """
    df3 = (
        df2
        .dropna()
        .query('PKSavePercentage != 100')
         )
    
    return df3
          


# In[8]:


load_and_process("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742")


# Task 4

#  # Analysis
#  
#  - Over two NHL seasons, there were a total of 322 goalies who played
#  - Of those, only 243 had to kill a penalty (short handed)
#  -  Many of the best goalies had a penalty kill save percentage that was higher than their even strength save percentage.
#  - Many of the goalies with a high PKSavePercentage have a lower PPSavePercentage.  This means they let in more goals per shots faced when they are on the powerplay than when they are killing a penalty.
#  

# # Pandas Profiling Analysis
# 
# - From the profiling report, aside from saves, goalies don't offer any more statistics.  Their goals, assists and PIM are averaged at less than 1.
# - The most goals a goalies scored in a game is 1 which is quite impressive! The most assists in a game is 2.
# - One goalie managed to rack up 27 penalty minutes in a single game! That's 300 times the mean.
# - The min for short handed saves was -1.  This mean the opponent must've scored without shooting.  This is a result of an own-goal.

# In[ ]:





# In[ ]:




