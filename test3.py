

import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')
results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")







# First we need to get the trailheads into a list

trailhead_elems = results.find_all('b')
trailhead_list=[]
for trailhead_elem in trailhead_elems:
	trailhead_name = trailhead_elem.find('span', attrs={"style": "color:black"})
	trailhead_list.append(trailhead_name.text)

# ---



# Next, we need to get all of the months into a list

trail_elems = results.find_all('span', attrs={"style": "tab-stops:21.75pt 79.5pt"}) #find dates
trailhead_month_list=[]
for trail_elem in trail_elems:
	trail_month = trail_elem.find('span', attrs={"style": "color:black"})
	trailhead_month_list.append(trail_month.text)
	# pprint(trail_month.text)

# ---


# Next, we need to get all of the days into a list

trailhead_days_list=[]
for trail_days in trail_elems:
	trail_day = trail_days.find_all('span', attrs={"style": "color:black"})
	trailhead_days_list.append(trail_day[1].text.split())


# pprint(len(trailhead_days_list))
# pprint(len(trailhead_month_list))



# for trail_elem in trail_elems:
# 	trail_month = trail_elem.find('span', attrs={"style": "color:black"})
# 	trailhead_month_list.append(trail_month.text)



# ---




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
	elif trailhead_list[trailhead_name_index] == "Rancheria Falls":
		trailhead_name_index=trailhead_name_index+1



	index=index+1


# pprint(trailhead_month_list[-20:])
# pprint(max_counter_tracker[-20:])
# pprint(trailhead_list)

pprint(master_list)







# ---

# may_counter=0
# index=0
# trailhead_month_list_copy=trailhead_month_list

# for month_indexer in trailhead_month_list_copy:
# 	if month_indexer == "May":
# 		may_counter=may_counter+1
# 	trailhead_month_list[index] = trailhead_month_list[index] + str(may_counter)
# 	index=index+1

# print(trailhead_month_list)


# ---




# i=0
# count_may=0
# count_june=0
# count_july=0
# count_august=0
# count_september=0
# count_october=0
# count_other=0

# for trail_elem in trail_elems:

# 	i=i+1

# 	trail_name = trail_elem.find('span', attrs={"style": "color:black"})

# 	if trail_name.text == "May":
# 		count_may=count_may+1
# 	elif trail_name.text == "June":
# 		count_june=count_june+1
# 	elif trail_name.text == "July":
# 		count_july=count_july+1
# 	elif trail_name.text == "August":
# 		count_august=count_august+1
# 	elif trail_name.text == "September":
# 		count_september=count_september+1
# 	elif trail_name.text == "October":
# 		count_october=count_october+1
# 	else:
# 		count_other=count_other+1

# 	print(i, end='\n')
# 	print(trail_name.text, end='\n'*2)
	# print(trail_elem, end='\n'*2)

# print("Count of Mays: ", count_may)
# print("Count of June: ", count_june)
# print("Count of July: ", count_july)
# print("Count of August: ", count_august)
# print("Count of September: ", count_september)
# print("Count of October: ", count_october)
# print("Count of Other: ", count_other)

# print(trailhead_list)
# print(trailhead_month_list)


# -------------------------


# print(results.prettify())

# 43 different trailheads

# style="tab-stops:4.5pt"

        # <span style="font-size:10.0pt">
        #  <span style='font-family:"Times New Roman",serif'>
        #   <span style="color:black">
        #    Cathedral Lakes
        #   </span>
        #  </span>
        # </span>