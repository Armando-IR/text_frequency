#!/usr/bin/env python
# coding: utf-8

# In[ ]:


listurls = [list_with_urls_to_be_scraped]


# In[ ]:


import requests
from time import sleep
import random
from bs4 import BeautifulSoup
import urllib
import re


# In[ ]:


listtest = listurls[:3]


# In[ ]:


data=[]
errors=[]
for item in listurls:
    try: 
        url = item
        page = urllib.request.urlopen(item).read() #requests library opens urls in a loop
        soup = BeautifulSoup(page,'html.parser')  #parsing the page by html
        sleep((random.randint(2,5))*random.randint(1,3)) #random sleep to avoid BAN
        corpus = soup.find('div', {"class": "entry-content-body"}) #it finds the text of the article
        for div in corpus:
            script = soup.find_all('script')
            for item in script:
                m = item.decompose()
        corpus = corpus.text.replace('\r\n ', ' ').replace('\n\n', ' ').replace('\r\n\t\xa0\n', ' ').replace('\n',' ').replace('\ ', "'").replace('\xa0\r', '').strip()
    
        try:
            date = soup.find('time', {"class": "datestamp"}).text.replace('gennaio', '01').replace('febbraio', '02').replace('marzo', '03').replace('aprile', '04').replace('maggio', '05').replace('giugno', '06').replace('luglio', '07').replace('agosto', '08').replace('settembre', '09').replace('ottobre', '10').replace('novembre', '11').replace('dicembre', '12').replace('\r\n ', '').replace('\n\n', '').replace('\r\n\t\xa0\n', '').replace("\ '", "'").replace('\r\n ', '').replace('\n\n', '').replace('\r\n\t\xa0\n', '').replace("\ '", "'").strip()
        except:
            date= 'NaN' #store NaN if no tag with this
            errors.append(['date', url]) #whether the tag search for this data should fail, 
            #except continues the script by returning the item to an error log list (in order to identify the error, we match it with the name of the failing process, in this case: 'date')
        try:
            author = soup.find('span', {"class": "author-name"}).text.replace('\r\n ', '').replace('\n\n', '').replace('\r\n\t\xa0\n', '').replace("\ '", "'").replace('\r\n ', '').replace('\n\n', '').replace('\r\n\t\xa0\n', '').replace('\n','').replace("\ '", "'").strip()
        except:
            author= 'NaN'
            errors.append (['author', url])
        
        try:
            title= soup.find('h1', {"class": "entry-title"}, {'data-amp' : 'amp-title'}).text.strip()
        except:
            title = 'NaN'
            errors.append(['title', url])

        try:
            summary = soup.find('p', {"class": "summary entry-summary"}, {'data-amp' : 'amp-abstract'}).text.strip()
        except:
            summary = 'NaN'
            errors.append(['summary', url])
    
    
        taglist = []
        tag = soup.find_all('a', {"class": "btn block-btn default-btn rounded-btn"}, href=True) #href=True 
        for item in tag:
            taglist.append(item.get_text().replace('\r\n', '').replace('\\s', '').strip())
        
    
      
    
    
        re.sub("all\''", "all'", corpus) #cleaning some problems...
        data.append([date, author, title, summary, corpus, taglist, url]) #all the scraped parameters stored in a list

    except:
        errors.append(['process', url]) #whether the entire process should fail, store the failure in the 'errors' list with a value 'process'


# In[ ]:


import json
p = json.dumps(data, ensure_ascii=False)
print(p)

with open('scraped_full.json', 'w') as f:
    f.write("%s\n" % json.dumps(data, ensure_ascii=False))

#save error list (as a sort of log) in json format
    import json
p = json.dumps(data, ensure_ascii=False)
print(p)

with open('scraped_full_errors.json', 'w') as f:
    f.write("%s\n" % json.dumps(errors, ensure_ascii=False))


# In[ ]:


import pandas as pd
df = pd.DataFrame(data)


# In[ ]:


df.to_csv('/Users/Armando_Bevilacqua/Desktop/scraped_full.csv')

