#!/usr/bin/python3
import requests
import datetime

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

#Challenge

def returnstartdate():
    startdt = input("Please enter a start date in the format YYYY-MM-DD::")
    print("Start date is: " + startdt)
    return startdt

def returnenddate():
    enddt = input("Please enter an end date in the format YYYY-MM-DD:")
    print("End date is: " + enddt)
    return enddt

def validate_date(date_text):
    try:
        datetime.strptime(d, '%Y-%m-%d')
        return True
    except ValueError:
        return False
        #raise ValueError("Incorrect data format. Please enter date in the format YYYY-MM-DD")

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    # Get start date
    startdt = returnstartdate()
    # Check start date
    if print(validate_date(startdt)) == "False":
        print("Incorrect data format. Please enter date in the format YYYY-MM-DD.")
    ## update the date below, if you like
    startdate = "start_date=" + startdt

    #Get end date
    enddt = returnenddate()
    #Check end date
    if print(validate_date(enddt)) == "False":
        print("Incorrect data format. Please enter date in the format YYYY-MM-DD.")
    ##
    enddate = "end_date=" + enddt

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
