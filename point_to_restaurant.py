import numpy
import pandas as pd
import random
from random import randint

#datafram
df = pd.read_csv('yelp_restaurant2.csv', encoding = "ISO-8859-1")
#select the random restaurant
random_index = random.randint(0,150)
#Define the restaurant's name, address and source url
name = df.iloc[random_index,0]
address = df.iloc[random_index,1].strip()
source_url = df.iloc[random_index,2]

#Open the source url by python
from selenium import webdriver
driver = webdriver.Chrome('D:/courses/2017Spring/application references/chromedriver_win32/chromedriver.exe')
driver.get(source_url)
# From the opened webpage, find out the restaurant we want and click to open it
driver.find_element_by_link_text(name).click()
