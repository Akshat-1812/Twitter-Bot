import tweepy
import time


auth = tweepy.OAuthHandler('I2znntbizUOED8HgJesCcTAkn', 'DwgvRUIV34VSp7Mp2JS30oFop7x05DiLGyUEBKRnjj4NUSLizw')
auth.set_access_token('1183312006985801729-MhmIWxii1JvdOeWwCdERW21kEKiNVO', 'dDvqzxcncZfcwPho7lazjfLg6iWFfLUWW7ZyFq9qv6Wz0')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

print('----------------------------------------------------------------------')

user = api.me()

print(user.name)
print(user.screen_name)
print(user.followers_count)

count =0
for friend in user.friends():
   count+=1
   print(friend.screen_name)

print(count)

print('----------------------------------------------------------------------')
#bot that accept a follow request
def limitHandler(cursor):
    try:
        while(True):
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limitHandler(tweepy.Cursor(api.followers).items()):
    
    if follower.name=='Shubh Joshi':
        follower.follow()
        break

print('----------------------------------------------------------------------')
#bot that like a tweet,retweet

search_string = 'Smartphone'
# search_string = 'Akshat Chouhan'
numoftimes=2


for tweet in tweepy.Cursor(api.search,search_string).items(2):
    
    try:
        print('aks')
        tweet.favorite() #like a tweet
        tweet.retweet() #retweet
        print('I like that tweet')
    except tweepy.TweepError as err:
        print('this is .............')
        print(err.reason)
    except StopIteration:
        print('error')
        break

print('----------------------------------------------------------------------')
#bot send tweet with image

api.update_with_media('.\Twitter_Bot\py_logo.jpg','This is a test tweet from py Python script')

