from email import header
import re
from turtle import st
from xml.etree.ElementTree import QName
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import csv

response = requests.get('https://quotes.toscrape.com/')
if response.status_code != 200:
    raise Exception("Failed to load the page {}") .format('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text , 'lxml')

quotes_info = soup.find_all('div',class_ ='quote')
#print(quotes_info)

info = []

for i in quotes_info:
    quotes = i.find('span',class_ ='text').text.replace('/n' ,'')
    #print(quotes)

    author = i.find('small',class_ ='author').text.replace('/n' ,'')
    #print(author)

    tags = i.find_all('a',class_ ='tag')
    htags =[]
    for i in tags:
          htags.append(i.text.strip())
    print(htags)
      

    quotes_dict = {
        'Quotes' : quotes,
        'Author' : author,
        'Tags'   : htags
    }

    info.append(quotes_dict)
    info_df =pd.DataFrame(info)

# print(info_df)

with open ('Quotes.csv','w') as f:
        thewriter = csv.writer(f)
        header = ['Quotes' , 'Author', 'Tags']
        thewriter.writerow(header)
        info_df.to_csv('Quotes.csv',index = None)


















