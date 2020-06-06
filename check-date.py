

import requests
import sys
import datetime
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')
results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")



def generate_master_list():
	# TODO: Move this to seperate file, add in report formatting logic check

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

	return master_list



# Now that we have the master list, we need to filter out the list items that are relevant to the named trailhead.

master_list = generate_master_list()

# pprint(master_list[0])


# June 16th
input_date=datetime.datetime(2020,6,6)

day_temp=[]
my_date=[]


# convert the date im interested in (my_date) into the right array format

# Add the 'trail name' so we don't get confused later
my_date.append("Date im interested in")

# Add the month in the full text version to match the master_list
my_date.append(input_date.strftime("%B"))

# Add the day (in array format) ... make sure it is added as a string so that it matches the format used in the master list
day_temp.append(str(input_date.day))
my_date.append(day_temp)




# pprint(my_date)



# search through the entire master list and crate a new list with all of the available trailheads

available_trailheads=[]
not_available_trailheads=[]
all_month_trailheads=[]

for trail_index in master_list:
	if trail_index[1] == my_date[1]:
		# They are in the right month...
		all_month_trailheads.append(trail_index)
		for day_array_index in trail_index[2]:
			if day_array_index == my_date[2][0]:
				not_available_trailheads.append(trail_index)
				pass
				# not_available_trailheads.append(trail_index)

		# need to check that day item exists in day array

		pass
	pass

# not_available_trailheads = list(dict.fromkeys(not_available_trailheads))
# not_available_trailheads = dict.fromkeys(not_available_trailheads)

# newlist=[]

# for i in not_available_trailheads:
#   if i not in newlist:
#     newlist.append(i)



# it does exist which means that I *cannot* book it...

# available_trailheads=list(all_month_trailheads - not_available_trailheads)

available_trailheads = [x for x in all_month_trailheads if x not in not_available_trailheads]




# output the full list of trailheads in an easy to read format


# pprint(all_month_trailheads)
# pprint(len(all_month_trailheads))

# pprint(available_trailheads)
# pprint(len(available_trailheads))

# pprint(not_available_trailheads)
# pprint(len(not_available_trailheads))


# pprint(newlist)
# pprint(len(newlist))

# pprint(len(master_list))

# exit()


# now = datetime.datetime.now()
# date_out = now.strftime("%Y-%m-%d-%Hh%Mm%Ss")
# # print("date and time:",date_time)	

# pprint(date_out)




