import tweepy
from os import listdir
from os.path import isfile, join
import os
import random
import time


x = 0
while x < 1000:
    x += 1
    i = 0
    while i < 4:
        i += 1
        if i == 1:
            filetype = "cursedimages"
        if i == 2:
            filetype = "meirl"
        if i == 3:
            filetype = "MapPorn"
        if i == 4:
            filetype = "vexillology"
        allfiles = [f for f in listdir("scraper/" + filetype + "/") if isfile(join("scraper/" + filetype + "/" , f))]
        ii = 0
        while ii < len(allfiles):
            file = allfiles[ii]
            for x in allfiles:
                if os.path.exists("scraper/" + filetype + "/" + file):
                    os.remove("scraper/" + filetype + "/" + file)
            ii += 1

    os.system('start cmd /k "cd redditscrape && bulk-downloader-for-reddit.exe --directory ../scraper --subreddit cursedimages --limit 25"')
    os.system('start cmd /k "cd redditscrape && bulk-downloader-for-reddit.exe --directory ../scraper --subreddit meirl --limit 25"')
    os.system('start cmd /k "cd redditscrape && bulk-downloader-for-reddit.exe --directory ../scraper --subreddit dataisbeautiful --limit 25"')
    os.system('start cmd /k "cd redditscrape && bulk-downloader-for-reddit.exe --directory ../scraper --subreddit MapPorn --limit 25"')
    os.system('start cmd /k "cd redditscrape && bulk-downloader-for-reddit.exe --directory ../scraper --subreddit vexillology --limit 25"')
    time.sleep(30)

    auth = tweepy.OAuthHandler("blKxFtkCQGkStbDjgTNmMT0Bd", "4TEzlLdgimIWSEMSgozkB27xoZCZML52zwGwiePrTXyalZQTH9")
    auth.set_access_token("1215051406941523968-DtrCbRZrBHAD78dFMtlN8zxwa4xVkY", "ki6L5REofeL2ZBsjs0cZP0HJ0bx1iCchvLT0FRKTOFuZz")
    rand = random.randint(1,4)
    if rand == 1:
        allfiles = [f for f in listdir("scraper/cursedimages") if isfile(join("scraper/cursedimages", f))]
        file = allfiles[random.randint(0, len(allfiles)-1)]
        api = tweepy.API(auth)
        if "md" in file:
            os.system('start cmd /k "cd desktop" && "py script.py"')
        else:
            api.update_with_media("scraper/cursedimages/" + file, "cursed")
    if rand == 2:
        allfiles = [f for f in listdir("scraper/meirl") if isfile(join("scraper/meirl", f))]
        file = allfiles[random.randint(0, len(allfiles)-1)]
        api = tweepy.API(auth)
        if "md" in file:
            os.system('start cmd /k "cd desktop" && "py script.py"')
        else:
            api.update_with_media("scraper/meirl/" + file, "shit Meme")

    if rand == 3:
        allfiles = [f for f in listdir("scraper/MapPorn") if isfile(join("scraper/MapPorn", f))]
        file = allfiles[random.randint(0, len(allfiles)-1)]
        api = tweepy.API(auth)
        if "md" in file:
            os.system('start cmd /k "cd desktop" && "py script.py"')
        else:
            api.update_with_media("scraper/MapPorn/" + file)
    if rand == 4:
        allfiles = [f for f in listdir("scraper/vexillology") if isfile(join("scraper/vexillology", f))]
        file = allfiles[random.randint(0, len(allfiles)-1)]
        api = tweepy.API(auth)
        if "md" in file:
            os.system('start cmd /k "cd desktop" && "py script.py"')
        else:
            api.update_with_media("scraper/vexillology/" + file, "flag")
    time.sleep(1800)
