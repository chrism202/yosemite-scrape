

import requests
from bs4 import BeautifulSoup
# import pprint

URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This ID is the table containing the core data
results = soup.find(id='cs_control_5529617')



# ------ The below 'settings' will find all trailnames ------

# trail_elems = results.find_all('span')
trail_elems = results.find_all('span', attrs={"style": "tab-stops:21.75pt 79.5pt"})



for trail_elem in trail_elems:

	# trail_name = trail_elem.find('span', attrs={"style": "color:black"})

	print(trail_elem, end='\n'*2)


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