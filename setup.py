import tweepy
import logging
import os

logger = logging.getLogger()

#create a credentials.py and hold app keys&tokens
from credentials import ckey,csecret,atoken,asecret




def create_api():
	consumer_key = ckey
	consumer_secret = csecret
	access_token = atoken
	access_token_secret = asecret

	#authenticates account with tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#creating the API object
	api = tweepy.API(auth)

	try:
	    api.verify_credentials()
	    print("Authentication OK")
	except:
	    print("Error during authentication")

	logger.info("API created")
	return api


