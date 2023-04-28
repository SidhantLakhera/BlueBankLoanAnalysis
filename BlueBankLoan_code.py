#!/usr/bin/env python
# coding: utf-8

# In[43]:


import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


json_file = open('loan_data_json.json')
data = json.load(json_file)


# In[10]:


df = pd.DataFrame(data)


# In[11]:


df.head()


# In[13]:


df.info()


# In[15]:


df.describe()


# In[24]:


df['Annual Income'] = round(np.exp(df['log.annual.inc']),1)


# In[25]:


df.head()


# In[35]:


length = len(df)
fico_category = []
for x in range(0,length):
    fico = df['fico'][x]

    if fico >= 300 and fico < 400:
        ficocat = 'Very Poor'

    elif fico >= 500 and fico < 600:
        ficocat = 'Poor'

    elif fico >= 601 and fico < 660:
        ficocat = 'Fair'

    elif fico >= 660 and fico < 700:
        ficocat = 'Good'

    elif fico >= 700:
        ficocat ='Excellent'

    else:
        ficocat ='Unknown'
    fico_category.append(ficocat)


# In[38]:


fico_category = pd.Series(fico_category)


# In[39]:


df['fico_category'] = fico_category


# In[40]:


df.head()


# In[41]:


df.loc[df['int.rate'] > 0.12,'int.rate.type'] = 'High'
df.loc[df['int.rate'] <= 0.12,'int.rate.type'] = 'Low'


# In[42]:


df.head()


# In[46]:


catplot = df.groupby(['fico_category']).size()
catplot


# In[45]:


purposecount= df.groupby(['purpose']).size()


# In[49]:


df['fico_category'].value_counts().plot(kind='bar',color='g')


# In[50]:


df['purpose'].value_counts().plot(kind='bar',width=0.2,color='red')


# In[55]:


sns.scatterplot(data=df,x='dti',y='Annual Income')
plt.show()


# In[57]:


df.to_csv('loan_cleaned.csv',index=True)


# In[60]:


pd.read_csv('loan_cleaned.csv',index_col=0)


# In[ ]:




