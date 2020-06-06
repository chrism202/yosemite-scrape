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


	# return results
	return {
		'test': "test999",
		'testy': "test999"
	}


def save_file_to_s3(bucket, file_name, data):
  s3 = boto3.resource('s3')
  obj = s3.Object(bucket, file_name)
  obj.put(Body=json.dumps(data))
  # obj.put(data)




def scrape(event, context):
  data = page_scrape()
  # fname=datetime.datetime.now()+""
  now = datetime.datetime.now()
  date_out = now.strftime("%Y-%m-%d-%Hh%Mm%Ss")
  file_name = date_out
  save_file_to_s3('yose-daily-scrape', file_name, data)


