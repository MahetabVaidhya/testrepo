#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


s = pd.Series([1,2,3,4,5,np.nan,8,9,10])
s


# In[22]:


df = pd.DataFrame({'A':[1,2,3,4],
                  'B': pd.Timestamp('20200301'),
                  'C':pd.Series(1,index=list(range(4)), dtype='float32'),
                  'D':np.array([5]*4,dtype='int32'),
                  'E':pd.Categorical(['true','False','True','False']),
                  'F':'Edruka'})


# In[6]:


df


# In[7]:


df.dtypes


# In[16]:


d = pd.date_range('20220101',periods=17)


# In[17]:


d


# In[25]:


df1 = pd.DataFrame(np.random.randn(10,4),columns=['A','B','C','D'])


# In[26]:


df1


# In[27]:


df1.head()


# In[28]:


df1.tail()


# In[31]:


df.index


# In[32]:


df1.columns


# In[33]:


df.to_numpy()


# In[34]:


df1.to_numpy()


# In[35]:


df.describe()


# In[36]:


df1.describe()


# In[38]:


df1.sort_values(by='A')


# In[39]:


df1['C']


# In[40]:


df1[0:7]


# In[43]:


df1.loc[:,['D','C']]


# In[44]:


df1.iloc[3]


# In[46]:


df1.iloc[3:7,0:2]


# In[49]:


df1[df1['A'] > 0]


# In[50]:


df1.isnull()


# In[51]:


date = pd.date_range('20220101',periods=10)


# In[52]:


date


# In[53]:


new_df = pd.DataFrame(np.random.randn(10,4),index=date,columns=['A','B','C','D'])


# In[54]:


new_df


# In[59]:


df2 = new_df.reindex(index=date[0:4],columns=list(new_df.columns) + ['E'])


# In[62]:


df2.loc[date[0]:date[1],'E'] = 1


# In[63]:


df2


# In[64]:


df2.isnull()


# In[66]:


df2.fillna(value=2)


# In[67]:


df2.isna()


# In[69]:


df2.mean(1)


# In[70]:


import matplotlib.pyplot as plt


# In[71]:


plt.close('all')


# In[72]:


ts = pd.Series(np.random.randn(500), index = pd.date_range('1/1/2022', periods=500))


# In[73]:


ts = ts.cumsum()


# In[74]:


ts.plot


# In[75]:


ts.plot()


# In[76]:


ts


# In[77]:


ts.to_csv("ts.csv")


# In[89]:


pd.read_csv(r'C:\blackcoffer\new\pokemon.csv')


# In[ ]:





# In[ ]:




