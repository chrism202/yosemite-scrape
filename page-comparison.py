# DONT MODIFY ANYTHING ON THIS PAGE

import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')
results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")


print(results)
