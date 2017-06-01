from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import operator
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

html = urlopen(source_url)
bs = BeautifulSoup(html, "lxml")

links = bs.find("div",{"class" : "search-results-content"}).findAll("a" , href=re.compile("(/biz/)+([A-Za-z0-9_:()])+"))

for link in links: 
    print(link)

#From this html java script, we can see the restaurant's url is in the <a class="biz-name js-analytics-click" group.
html = urlopen(source_url)
bs = BeautifulSoup(html, "lxml")

links = bs.find("div",{"class" : "search-results-content"}).findAll("a" , href=re.compile("(/biz/)+([A-Za-z0-9_:()])+"))

for link in links: 
    print(link)

