import praw
import os
import youtube_dl


USERNAME = ""
PASSWORD = ""
user_agent = "Video Downloader"

r = praw.Reddit(user_agent=user_agent)

submissions = r.get_subreddit('cringe').get_top(limit=12)

urls = []
names=[]

def yt() :
    for x in submissions:
        ydl_opts = {'outtmpl': "/Users/amirjaffari/Desktop/YouTube/"+x.title + '.%(ext)s'}
        urls.append(str(x.url))
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
           ydl.download([x.url, ])
yt()
