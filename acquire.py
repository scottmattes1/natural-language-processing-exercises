import pandas as pd
import numpy as np
from requests import get
from env import get_db_url
import os

from bs4 import BeautifulSoup



################## ACQUIRE BLOG ARTICLES ##################

def acquire_blog_articles():
    """
    Acquires the title and content of 5 Codeup blog posts. Returns a list of dictionaries where each element represents an article
    """
    
    if os.path.exists('blog.csv'):
        df = pd.read_csv('blog.csv')
    
    else:
        # URL's to scrape
        urls = ['https://codeup.edu/alumni-stories/how-i-paid-43-for-my-codeup-tuition/',
            'https://codeup.edu/data-science/where-do-data-scientists-come-from/',
            'https://codeup.edu/data-science/codeups-data-science-career-accelerator-is-here/',
            'https://codeup.edu/featured/women-in-tech-panelist-spotlight/',
            'https://codeup.edu/codeup-news/women-in-tech-panelist-spotlight-sarah-mellor/'
           ]

        # Intiate the results list
        results = []

        # Iterate through the urls that were taken as an argument
        for url in urls:
            # Set the headers to give us access
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            # Take in the url's html file
            response = get(url, headers=headers)
            # Format in beautfulsoup
            bs = BeautifulSoup(response.text)
            # Create a dictionary of the title and content
            content = dict(title = bs.h1.text, content = '\n'.join([p.text for p in bs.find_all('p')]))
            # Append the results to the list of dictionaries
            results.append(content)
            
            # Convert to a dataframe
            df = pd.DataFrame(results)
            
            # Save to a csv in the directory
            df.to_csv('blog.csv', index=False)
        
        
        
    return df


################# ACQUIRE NEWS ARTICLES ###################

def acquire_news_articles():
    """
    Scrapes news articles from provided URLs and returns their title, content, and category in a dataframe
    """
    
    if os.path.exists('news.csv'):
        df = pd.read_csv('news.csv')
    
    else:
        results = []

        # URL's to scrape
        urls = [
        'https://inshorts.com/en/read/business',
        'https://inshorts.com/en/read/sports',
        'https://inshorts.com/en/read/technology',
        'https://inshorts.com/en/read/entertainment'
        ]

        # Iterate through the list of urls that were taken as an argument
        for url in urls:
            # Take in the urls html file
            response = get(url)
            # Convert it to beautifulsoup format
            soup = BeautifulSoup(response.text, 'html.parser')
            # Make a list of all the headlines on the page
            headlines = soup.find_all('span', itemprop="headline")
            # Make a list of all the article content on the page
            articles = soup.find_all('div', itemprop="articleBody")
            # Grab the category from the end of the url
            category = url.split('/')[-1]

            # For the number of headlines there are in the url, create a dictionary of the title, content, and category
            for i in range(len(headlines)):
                article = {
                    'title': headlines[i].text,
                    'article': articles[i].text,
                    'category': category
                }
                # Append the results to a list
                results.append(article)

                # Cast the results to a dataframe
                results_df = pd.DataFrame(results)

                # Save to a csv in the directory
                df.to_csv('news.csv', index=False)
    
    return df


####################### ACQUIRE SPAM ##########################



