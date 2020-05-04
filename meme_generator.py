import praw
from config import config


red = praw.Reddit(client_id=config['REDDIT']['client_id'],
                  client_secret=config['REDDIT']['client_secret'],
                  user_agent=config['REDDIT']['user_agent'])


def generate_meme():
    submission = red.subreddit('memes').random()
    return submission.title, submission.url
