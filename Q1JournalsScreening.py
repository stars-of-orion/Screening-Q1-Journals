#!/usr/bin/env python
# coding: utf-8

# In[4]:


''


# In[11]:


import pandas as pd

df = pd.read_excel('Q1 journals.xlsx') # can also index sheet by name or fetch all sheets
mylist = df['Source title'].tolist()

print(len(mylist))
no_duplication_lst = list(set(mylist))
print(len(no_duplication_lst))


df = pd.read_csv ('List_of_extracted_papers.csv')
df['Q1'] = pd.Series(dtype='int')

filtered_df = df[df['Source title'].isin(no_duplication_lst)]

filtered_df.shape
filtered_df.to_csv('out.csv', index=False)  


# In[14]:





# In[17]:





# In[19]:





# In[ ]:




