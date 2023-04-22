{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Web Scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Obtain list of news from the coverpage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL definition\n",
    "url = \"https://nos.nl/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Request list of news\n",
    "requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save content from coverpage\n",
    "coverpage = requests.get(url).content\n",
    "soup = BeautifulSoup(coverpage, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "107"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Select headers h2\n",
    "coverpage_headlines = soup.find_all('h2', class_='sc-2d866c3b-0 dypUEp')\n",
    "len(coverpage_headlines)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h2 class=\"sc-2d866c3b-0 dypUEp\">'Na advocaat Weski ook neef Ridouan Taghi aangehouden'</h2>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the first headline\n",
    "coverpage_headlines[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"'Na advocaat Weski ook neef Ridouan Taghi aangehouden'\""
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Getting only the text part\n",
    "coverpage_headlines[0].get_text()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Select body p\n",
    "coverpage_body = soup.find_all('p', class_='sc-2d866c3b-1 jPkGEE')\n",
    "len(coverpage_body)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'De praalwagens vertrokken vanochtend iets na 09.00 uur uit Noordwijk, op weg naar Haarlem. Langs de weg worden ruim een miljoen bezoekers verwacht.'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking the first headline\n",
    "coverpage_body[0].get_text()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Creating a for loop to extract all content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining the number of articles we want\n",
    "number_of_articles = 10\n",
    "\n",
    "# Empty lists for headlines and content\n",
    "news_headlines = []\n",
    "news_content = []\n",
    "\n",
    "# Loop where the headlines and content are added to the empty lists\n",
    "for n in np.arange(0, number_of_articles):\n",
    "    \n",
    "    # Getting the title\n",
    "    headline = coverpage_headlines[n].get_text()\n",
    "    news_headlines.append(headline)\n",
    "    \n",
    "    # Getting the content (divided in paragraphs)\n",
    "    content = coverpage_body[n].get_text()\n",
    "    news_content.append(content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating dataframes\n",
    "news_headlines = pd.DataFrame(\n",
    "    {'Article Headline': news_headlines})\n",
    "\n",
    "news_content = pd.DataFrame(\n",
    "     {'Article Content': news_content})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Article Headline</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>'Na advocaat Weski ook neef Ridouan Taghi aang...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Nederland bereidt risicovolle evacuatie uit Su...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>De poncho's zijn gewild bij bloemencorso in de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>BBB kiest in provincie voor VVD, PvdA en zelfs...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Run op lastminutes door matig lenteweer, maar ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Man mishandelt NS-medewerker en geeft politiem...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Touringcar brandt uit op A2 bij Breukelen</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Scheepswrak met ruim 1000 slachtoffers WO II n...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Article Headline\n",
       "0  'Na advocaat Weski ook neef Ridouan Taghi aang...\n",
       "1  Nederland bereidt risicovolle evacuatie uit Su...\n",
       "3  De poncho's zijn gewild bij bloemencorso in de...\n",
       "5  BBB kiest in provincie voor VVD, PvdA en zelfs...\n",
       "6  Run op lastminutes door matig lenteweer, maar ...\n",
       "7  Man mishandelt NS-medewerker en geeft politiem...\n",
       "8          Touringcar brandt uit op A2 bij Breukelen\n",
       "9  Scheepswrak met ruim 1000 slachtoffers WO II n..."
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Showing the list with the news headlines\n",
    "news_headlines = news_headlines.drop_duplicates()\n",
    "news_headlines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Article Content</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>De praalwagens vertrokken vanochtend iets na 0...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>De verkenningsfase is achter de rug, tijd om t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Begin volgende week wordt het opnieuw niet war...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>De NS-medewerker en de politieman hebben aangi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Niemand raakte gewond. De snelweg was geheel d...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Amerikaanse torpedo's joegen het Japanse schip...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Humphries stond in Australië bekend als een va...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>De tweevoudig olympisch kampioene heeft bewust...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>In dit liveblog lees je de belangrijkste ontwi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Steeds meer landen maken zich op om hun burger...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     Article Content\n",
       "0  De praalwagens vertrokken vanochtend iets na 0...\n",
       "1  De verkenningsfase is achter de rug, tijd om t...\n",
       "2  Begin volgende week wordt het opnieuw niet war...\n",
       "3  De NS-medewerker en de politieman hebben aangi...\n",
       "4  Niemand raakte gewond. De snelweg was geheel d...\n",
       "5  Amerikaanse torpedo's joegen het Japanse schip...\n",
       "6  Humphries stond in Australië bekend als een va...\n",
       "7  De tweevoudig olympisch kampioene heeft bewust...\n",
       "8  In dit liveblog lees je de belangrijkste ontwi...\n",
       "9  Steeds meer landen maken zich op om hun burger..."
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Showing the list with the news content\n",
    "news_content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
