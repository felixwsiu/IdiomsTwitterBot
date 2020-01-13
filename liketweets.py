import tweepy
import logging
from setup import create_api

filterwords=["Chinese","Culture","Idioms","China","Hong Kong","Taiwan","Mandarin","Cantonese","Language","Learn"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



class liketweets(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self,status):
        print("Processing tweet...."+str(status.id))
        if not ((status.in_reply_to_status_id != None) or (status.user.id == self.me.id)):
            if not status.favorited:
                status.favorite()


def main(filters):
	api = create_api()
	#set up listener object that will act upon tweets
	tweetlistener = liketweets(api)

	#begin pushing data to session through listener
	likestream = tweepy.Stream(api.auth,tweetlistener)

	#filter the data with selected keywords
	likestream.filter(track=filters)





main(filterwords)