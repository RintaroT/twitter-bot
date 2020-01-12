import os
from pynput.keyboard import Key, Controller
keyboard = Controller()
#bulk-downloader-for-reddit.exe --directory .\\dump --subreddit "MapPorn" --limit 20
sub = "cursedimages"
os.system('cmd /c "bulk-downloader-for-reddit.exe --directory .//scraper --subreddit' + " " + sub + " " + '--limit 10')
