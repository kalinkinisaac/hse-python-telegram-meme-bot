import praw
from config import config
import random

LIMIT = 100
red = praw.Reddit(client_id=config['REDDIT']['client_id'],
                  client_secret=config['REDDIT']['client_secret'],
                  user_agent=config['REDDIT']['user_agent'])


def generate_meme(subreddit=None, keyword='memes'):
    if subreddit:
        submission = red.subreddit(subreddit).random()
    else:
        all = red.subreddit("all")
        submission = None
        search = list(all.search(keyword, limit=LIMIT))
        random.shuffle(search)
        for sub in search:
            if sub.url and sub.url.endswith('.jpg'):
                submission = sub
                break
        if not submission:
            return None

    return submission.title, submission.url
