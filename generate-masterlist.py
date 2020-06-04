

import requests
import sys
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')
results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")














# First we need to get the trailheads into a list
# ... This code works with the original report format

trailhead_elems = results.find_all('b')
# print(trailhead_elems)
trailhead_list=[]
for trailhead_elem in trailhead_elems:
	trailhead_name = trailhead_elem.find('span', attrs={"style": "color:black"})
	trailhead_list.append(trailhead_name.text)

# We now have an array called trailhead_list with all of the trail head names in it

# - - - - - - - - - - - - - - - - - - - - - - - - - -






# Next, we need to get all of the months into a list
# ... This code works with the original report format

trail_elems = results.find_all('span', attrs={"style": "tab-stops:21.75pt 79.5pt"}) #find dates
trailhead_month_list=[]
for trail_elem in trail_elems:
	trail_month = trail_elem.find('span', attrs={"style": "color:black"})
	trailhead_month_list.append(trail_month.text)
	# pprint(trail_month.text)

# - - - - - - - - - - - - - - - - - - - - - - - - - -




# Next, we need to get all of the days into a list
# ... This code works with the original report format

trailhead_days_list=[]
for trail_days in trail_elems:
	trail_day = trail_days.find_all('span', attrs={"style": "color:black"})
	trailhead_days_list.append(trail_day[1].text.split())

# - - - - - - - - - - - - - - - - - - - - - - - - - -







# Next, we need to identify which month is 'first' for a given trailhead, so we can calculate the 'index'

# Logic: If the next month is 'lower' than the previous month in value, then we can assume we have jumped to the next trailhead

master_list=[]


max_counter=0
max_counter_tracker=[]
index=0
trailhead_name_index=0
trailhead_month_list_copy=trailhead_month_list

for month_indexer in trailhead_month_list_copy:
	if month_indexer == "May":
		max_counter=5
	elif month_indexer == "June":
		max_counter=6
	elif month_indexer == "July":
		max_counter=7
	elif month_indexer == "August":
		max_counter=8
	elif month_indexer == "September":
		max_counter=9
	elif month_indexer == "October":
		max_counter=10
	# No 'others'
	# print("Value of index: ", str(index))
	# max_counter_tracker[index]=max_counter
	max_counter_tracker.append(max_counter)

	# pprint(master_list)

	if index != 0:
		# do nothing
		if max_counter_tracker[index] <= max_counter_tracker[index-1]:
			# We have jumped to a new trailhead
			# trailhead_month_list[index] = trailhead_month_list[index] + " - NEW TRAILHEAD"
			trailhead_name_index=trailhead_name_index+1
	
	trailhead_month_list[index] = trailhead_month_list[index] + " - " + trailhead_list[trailhead_name_index]


	master_list.append([trailhead_list[trailhead_name_index],month_indexer, trailhead_days_list[index]])


	# If the trailhead name at any index is Cottonwood creek, increment the counter by one (AFTER printing the name once)
	# Same for Rancheria falls
	# Check this every day
	if trailhead_list[trailhead_name_index] == "Cottonwood Creek":
		# print(trailhead_name_index)
		trailhead_name_index=trailhead_name_index+1
	# elif trailhead_list[trailhead_name_index] == "Rancheria Falls":
	# 	trailhead_name_index=trailhead_name_index+1

	index=index+1

# return master_list

# pprint(master_list)
