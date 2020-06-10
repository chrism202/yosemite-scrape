
# This code is a modified version of the below Medium post, designed to scrape the Yosemite Full Trailheads report on a twice-daily basis, to collect data for later analysis
# Link to Medium article - https://medium.com/@kagemusha_/scraping-on-a-schedule-with-aws-lambda-and-cloudwatch-caf65bc38848



import requests
import boto3
import datetime
from bs4 import BeautifulSoup
from pprint import pprint
import json



def page_scrape():

	URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')

	# This ID is the table containing the core data
	results = soup.find(id='cs_control_5529617')
	results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")

	results_string=str(results)
	return results_string



def save_file_to_s3(bucket, file_name, data):
  s3 = boto3.resource('s3')
  obj = s3.Object(bucket, file_name)
  # obj.put(Body=json.dumps(data))
  obj.put(Body=data)





def scrape(event, context):
  data = page_scrape()
  # fname=datetime.datetime.now()+""
  now = datetime.datetime.now()
  date_out = now.strftime("%Y-%m-%d-%Hh%Mm%Ss")
  file_name = date_out
  # pprint(data)
  save_file_to_s3('yose-daily-scrape', file_name, data)


# Uncomment the below line for local testing
# scrape("hello", "world")


