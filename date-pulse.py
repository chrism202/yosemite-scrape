

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')
results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")

# print(results)

# exit()



 # -- Check the format of the update ---

# TODO: Detect the type of website update to account for changes in 

# Use the previously downloaded version of the site to test this logic
# f=open("guru99.txt", "r")
# if f.mode == 'r':
# 	contents =f.read()

# print(type(results))

# ---



report_date = results.text.split("\n")
report_date = report_date[1].split(": ")
report_date = datetime.strptime(report_date[1],'%m/%d/%Y')



print(report_date)


# First we need to get the trailheads into a list

# better_results = results.find_all('span')
# # pprint(better_results)
# current_date=[]
# for trailhead_elem in better_results:
# 	trailhead_name = trailhead_elem.find('span', attrs={"style": "color:black"})
# 	current_date.append(trailhead_name.text)

# ---





