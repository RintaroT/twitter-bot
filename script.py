import tweepy
from os import listdir
from os.path import isfile, join
auth = tweepy.OAuthHandler("blKxFtkCQGkStbDjgTNmMT0Bd", "4TEzlLdgimIWSEMSgozkB27xoZCZML52zwGwiePrTXyalZQTH9")
auth.set_access_token("1215051406941523968-DtrCbRZrBHAD78dFMtlN8zxwa4xVkY", "ki6L5REofeL2ZBsjs0cZP0HJ0bx1iCchvLT0FRKTOFuZz")

api = tweepy.API(auth)
api.update_with_media('test.jpg', 'RISE UP')
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


onlyfiles = [f for f in listdir("C:/Users/Thornton/Documents/GitHub/twitter-bot") if isfile(join("C:/Users/Thornton/Documents/GitHub/twitter-bot", f))]
