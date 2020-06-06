
# This is a README

## Getting Started

This package will (eventually) scrape the Yosemite Full Trailhead report on a daily basis and dump it into an S3 bucket, with the name of the dump being based on the timestamp of when the lambda function was ran.

This script is a rip-off of the guide written here: https://medium.com/@kagemusha_/scraping-on-a-schedule-with-aws-lambda-and-cloudwatch-caf65bc38848

## Deploying


#### Step 1 - Update the deployment package with your changes

```
zip -r package.zip *
```

#### Step 2 - Deploy the package to Lambda

```
serverless deploy
```


#### Step 3 - Run the code in Lambda (this can also be done from the Lambda console)

```
serverless invoke -f yose_scrape
```


Congratulations - you have ran the code. Check your S3 bucket for an updated dump.