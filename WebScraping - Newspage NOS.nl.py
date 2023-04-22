#!/usr/bin/env python
# coding: utf-8

# # Web Scraping

# In[1]:


get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


# ### Obtain list of news from the coverpage

# URL definition:

# In[2]:


# url definition
url = "https://nos.nl/"


# List of news:

# In[3]:


# Request
requests.get(url)


# In[7]:


# We'll save in coverpage the cover page content
coverpage = requests.get(url).content


# In[6]:


soup = BeautifulSoup(coverpage, 'lxml')
soup


# In[90]:


# News identification
coverpage_headlines = soup.find_all('h2', class_='sc-2d866c3b-0 dypUEp')
len(coverpage_headlines)


# Now we have a list in which every element is a news article:

# In[91]:


coverpage_headlines[0]


# In[92]:


n=0
title = coverpage_headlines[n].get_text()
title


# In[94]:


coverpage_body = soup.find_all('p', class_='sc-2d866c3b-1 jPkGEE')
coverpage_body


# In[95]:


len(coverpage_body)


# In[96]:


coverpage_body[0].get_text()


# ### Let's extract the text from the articles:

# First, we'll define the number of articles we want:

# In[109]:


number_of_articles = 10


# In[110]:


# Empty lists for content, links and titles
news_headlines = []
news_content = []

for n in np.arange(0, number_of_articles):
    
    # Getting the title
    headline = coverpage_headlines[n].get_text()
    news_headlines.append(headline)
    
    # Reading the content (divided in paragraphs)
    content = coverpage_body[n].get_text()
    news_content.append(content)


# In[111]:


coverpage_body[0]


# Let's put them into:
# * a dataset which will the input of the models (`df_features`)
# * a dataset with the title and the link (`df_show_info`)

# In[112]:


# creating a df
news_headlines = pd.DataFrame(
    {'Article Headline': news_headlines})

# creating a df
news_content = pd.DataFrame(
     {'Article Content': news_content})


# In[113]:


news_headlines = news_headlines.drop_duplicates()
news_headlines


# In[114]:


news_content


# In[ ]:




