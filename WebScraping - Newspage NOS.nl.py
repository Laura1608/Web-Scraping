import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# ### Obtain list of news from the coverpage

# url definition
url = "https://nos.nl/"

# Request list of news
requests.get(url)

# Save content from coverpage
coverpage = requests.get(url).content
soup = BeautifulSoup(coverpage, 'lxml')

# Select headers h2
coverpage_headlines = soup.find_all('h2', class_='sc-2d866c3b-0 dypUEp')
len(coverpage_headlines)

# Checking the first headline
coverpage_headlines[0]

# Checking only the text part
coverpage_headlines[0].get_text()

# Select body p
coverpage_body = soup.find_all('p', class_='sc-2d866c3b-1 jPkGEE')
len(coverpage_body)

# Checking the first headline
coverpage_body[0].get_text()

# Creating a loop to extract all content

# Defining the number of articles
number_of_articles = 10

# Empty lists for headlines and content
news_headlines = []
news_content = []

# Loop where the headlines and content are added to the empty lists
for n in np.arange(0, number_of_articles):
    
    # Getting the title
    headline = coverpage_headlines[n].get_text()
    news_headlines.append(headline)
    
    # Reading the content (divided in paragraphs)
    content = coverpage_body[n].get_text()
    news_content.append(content)

# Creating a dataframe
news_headlines = pd.DataFrame(
    {'Article Headline': news_headlines})

# Creating a dataframe
news_content = pd.DataFrame(
     {'Article Content': news_content})

# Showing the list with the news headlines
news_headlines = news_headlines.drop_duplicates()
news_headlines

# Showing the list with the news content
news_content
