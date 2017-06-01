#Word Cloud - show the words appear in different color and
#size according to the appeared frequency of each word.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import operator
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    text=""
    for post_text in soup.findAll('p',{'lang':'en'}):
        content = post_text.get_text()
        text = text+content
        #words = content.lower().split()
        #for each_word in words:
            #word_list.append(each_word)
    #print(text)
    # generate word cloud
    plt.figure(figsize=(20,10))
    wordcloud = WordCloud(background_color='white', mode = "RGB", width = 2000, height=1000).generate(text)
    plt.title("Wordcloud")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# main program
start('https://www.yelp.com'+url)
