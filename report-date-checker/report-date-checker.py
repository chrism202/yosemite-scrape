
# This script will pulse the Yosemite Full Trailhead report and determine if the report has been updated. If it has, then we will send an alert (email or text message) to the interested party (me)

#  - Connect to the database

#  - Get the latest date from the database

#  - Get the latest date from the report

#  - If the date in the report is newer than the latest in the database then send an alert (text message, email)


import requests
import boto3
from datetime import datetime
from bs4 import BeautifulSoup
from pprint import pprint
import json





def main(event, context):
	report_date = get_report_date()

	table = connect_to_db('us-east-1', 'yose-trailhead-report-dates')

	db_date = get_db_date(table)

	if report_date >= db_date:
		update_database(report_date, table)
		send_alert()
		pass


	print(report_date)
	print(db_date)



def get_report_date():

	URL = 'https://www.nps.gov/yose/planyourvisit/fulltrailheads.htm'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')

	# This ID is the table containing the core data
	results = soup.find(id='cs_control_5529617')
	results = results.find(class_="Component text-content-size text-content-style ArticleTextGroup clearfix")

	# Transform the date in the report to a datetime object
	report_date = results.text.split("\n")
	report_date = report_date[1].split(": ")
	report_date = datetime.strptime(report_date[1],'%m/%d/%Y')

	return report_date


def connect_to_db(region_name, table_name):

    dynamodb = boto3.resource('dynamodb', region_name=region_name)

    table = dynamodb.Table(table_name)

    return table
    
    



def get_db_date(table):

	# Create a dummy date until we get the database connected
	db_date = datetime(2020,6,8)  #Datetime is year,month,day
	
	return db_date



def update_database(report_date, table):

	# In this function we will update the database by adding the new report date to the database

	data_to_load = {
		'EntryID': str(datetime.now()),
		'ReportDate': str(report_date)
	}

	table.put_item(Item=data_to_load)

	pprint("Database has been updated")




def send_alert():

	# In this function we will send the alert through AWS services like SES or SQS

	pprint("Alert has been sent")



# Uncomment the below line for local testing
main("hello", "world")
# update_database()