import os
import tweepy
import secrets
import covid
import pandas as pd
import time

from secrets import(
    C_KEY,
    C_SECRET,
    A_TOKEN,
    A_TOKEN_SECRET    
)

from covid import(
    DATE,
    COUNTY,
    STATE,
    CASES,
    DEATHS,
    GADEATHS,
    GACASES,
    USDEATHS,
    USCASES
)

 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
interval = 60*60*24

linkATH = 'https://www.accgov.com/coronavirus'
linkGA =  'https://www.cdc.gov/coronavirus/2019-ncov/index.html'

# tweet
while True:
    tweetATH = "As of {},\n\nCASES IN ATHENS: {}\nDEATHS IN ATHENS: {}\n\nPlease stay safe. For more on Athens, visit {}".format(DATE, CASES, DEATHS, linkATH)
    api.update_status(tweetATH)
    
    tweetGA = "As of {}, \n\nCASES IN GEORGIA: {} \nDEATHS IN GEORGIA: {}\n\n Please stay safe. For more, visit {}".format(DATE,GACASES, GADEATHS, linkGA)
    api.update_status(tweetGA)

    tweetUS = "As of {}, \n\nCASES IN US: {} \nDEATHS IN US: {}\n\n Please stay safe. For more, visit {}".format(DATE,USCASES, USDEATHS, linkGA)
    api.update_status(tweetUS)

time.sleep(interval)

