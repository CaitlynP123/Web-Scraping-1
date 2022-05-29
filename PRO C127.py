#Was able to complete project, had to research about how to append lists as columns and how to make them files

from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv
import pandas as pd

startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('C:/Users/C/OneDrive/Desktop/Coding/python/Web Scraping/chromedriver.exe')
browser.get(startUrl)

time.sleep(10)

headers = ['Name', 'Distance', 'Mass', 'Radius']

soup = BeautifulSoup(browser.page_source, 'html.parser')

table = soup.find('table')
temp_list = []
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)):
    Names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])


star_data = pd.DataFrame(list(zip(Names, Distance, Mass, Radius)))
star_data.to_csv('star_data.csv', header=headers, index=False)