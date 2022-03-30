#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("Data_set.csv")


# In[3]:


df.head(10)


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[11]:


df['show_name']=df['show_name'].fillna(df['show_name'].mode()[0])
df.isnull().sum()


# In[12]:


df['aired_on']=df['aired_on'].fillna(df['aired_on'].mode()[0])
df.isnull().sum()


# In[13]:


df['original_network']=df['original_network'].fillna(df['original_network'].mode()[0])
df.isnull().sum()


# In[16]:


df['rating']=df['rating'].fillna(df['rating'].mean())
df.isnull().sum()


# In[17]:


df['current_overall_rank']=df['current_overall_rank'].fillna(df['current_overall_rank'].median())
df.isnull().sum()


# In[18]:


df['watchers']=df['watchers'].fillna(df['watchers'].median())
df.isnull().sum()


# In[20]:


df.head(10)


# In[ ]:



