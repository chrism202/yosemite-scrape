

import requests
from bs4 import BeautifulSoup
# import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find(id='cs_idLayout2')
results = soup.find(id='cs_control_5529617')



# ------ The below 'settings' will find all trailnames ------

# trail_elems = results.find_all('span')
trail_elems = results.find_all('b')

trailhead_list=[]


for trail_elem in trail_elems:

	trail_name = trail_elem.find('span', attrs={"style": "color:black"})

	trailhead_list.append(trail_name.text)

	# print(trail_name.text, end='\n'*2)

print(trailhead_list)


# ------------------------------------------------------------


# print(results.prettify())


# style="tab-stops:4.5pt"

        # <span style="font-size:10.0pt">
        #  <span style='font-family:"Times New Roman",serif'>
        #   <span style="color:black">
        #    Cathedral Lakes
        #   </span>
        #  </span>
        # </span>