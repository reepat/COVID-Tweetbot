import csv
import pandas as pd
import datetime

covidATH = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv")
covidGA = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-states.csv")
covidUS = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us.csv")

inputDate0 = (covidATH['date'][414])
DateFormat0 = "%Y-%m-%d"
outPutDateFormat = "%m/%d/%y"

date0 = datetime.datetime.strptime(inputDate0, DateFormat0)
DATE = datetime.date.strftime(date0,outPutDateFormat)


COUNTY = (covidATH['county'][414])
STATE = (covidATH['state'][414])
CASES = (f"{(covidATH['cases'][414]):,d}")
DEATHS = (f"{int((covidATH['deaths'][414])):,d}")

GACASES = (f"{(covidGA['cases'][10]):,d}")
GADEATHS = (f"{(covidGA['deaths'][10]):,d}")

USCASES = (f"{(covidUS['cases'][0]):,d}")
USDEATHS = (f"{(covidUS['deaths'][0]):,d}")

