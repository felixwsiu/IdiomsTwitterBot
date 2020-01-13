import tweepy

from setup import create_api
import time

def follow_followers(api):
    print("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print("Following : "+follower.name)
            follower.follow()

def main():
    #creates our api and follows all followers
    api = create_api()
    while True:
        follow_followers(api)
        print("Waiting...")
        time.sleep(60)

main()