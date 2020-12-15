#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from collections import Counter


# In[ ]:


syntagms = pd.read_csv(#directory_csv) #import the csv with N syntagms. 
art = pd.read_csv(#directory_csv) #import the csv previously scraped. 
#It has rows for elements with a corpus. Articles in our case


# In[ ]:


art['Date'] =  pd.to_datetime(art['Date']) #change dateformat.


# In[ ]:


art[(art['Date'] > '2010-01-01') & (art['Date'] < '2011-12-31')] #select the data range.


# In[ ]:


S1 = list(syntagms['column_name']) #extract the column from the dataset with syntagms. Extract as a list.


# In[1]:


#create a new list including variants with punctuation 
Stest = S1[3]
S2 = []
for i in S1:
    v1 = i + '.'
    v2 = i + ','
    v3 = i + '?'
    v4 = i + '!'
    v5 = i + '"'
    v6 = i + '>>'
    v7 = i + ')'
    v8 = i + ' '   
    S2.append(v1)
    S2.append(v2)
    S2.append(v3)
    S2.append(v4)
    S2.append(v5)
    S2.append(v6)
    S2.append(v7)
    S2.append(v8)


# In[ ]:


l = [] #empty list
t = [] #empty list
for i in S2:
    l.append(i)
    e = art['Text'].apply(lambda x: x.count(i)) 
    t.append(e)
    
#it is a loop that takes any item in the list S2, 
#add it to a new one (l) and for this item check for its frequency in the corpus. 
#It stores the frequencies in order in the list (e), then stores again the list (e) in (t).


# In[ ]:


A = np.array(t)
#it creates an array A from t. For each item in S2 there is the frequency in each element of the dataframe art (the collection of corpus)


# In[ ]:


import pickle
with open('ti.pickle', 'wb') as f:
    pickle.dump(A, f)

#pickle the array (Pay attention to the dimension of the DataFrame, there are limits)


# In[ ]:


df = pd.DataFrame(A) #make a dataframe with the A array


# In[ ]:


#AT THIS POINT WE HAVE A MATRIX OF DATA WITH N ROWS AS MANY AS THE SYNTAGMS 
#AND N COLUMNS AS MANY AS THE TEXTS COLLECTED IN THE DATAFRAME WITH THE CORPUS


# In[ ]:


df['Total'] = df.sum(axis=1) #create a column with a total of row.


# In[ ]:


df['SYNTAGMS'] = l #add a column with the syntagms of each row


# In[ ]:


df.sort_values(by=['Total'], ascending=False) #sort values
dfn = df2[df2['Total'] > 0] #create a new dataframe filtering syntagms whose value is > 0


# In[ ]:


dfn.to_csv(insert_directory) #save to csv

