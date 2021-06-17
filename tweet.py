import tweepy
import time

auth = tweepy.OAuthHandler('KFQUXYH7SwsaZoqaAam9K4ZY5', 'BvUi0Y22FoZTMH1k6MEQOLx6L5t2uDysFlNku5OkNJJTmRz9Em')
auth.set_access_token('201628245-lDqAgfcEMI5tdbq6NBoH8MX2mujEQ5LtrZGNIgNq', 'R4SwLjmmFA4Rd7GT9DljEZl0EOY2PVo4i15h00NXAG50m')

api = tweepy.API(auth)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# generous bot, always going to follow back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 100:
        follower.follow()
        break

# search the keywords python, in all the tweets
search_string = 'python'
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersofTweets):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break





