import tweepy
import time

class TweetBot():
    # class variables......
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('', '')

    api = tweepy.API(auth)
    user = api.me()

    @classmethod
    def myTimeLineTweet(cls):
        public_tweets = cls.api.home_timeline()

        for tweet in public_tweets:
            print(tweet.text)
    
    @classmethod
    def profileDetails(cls):
        print(f'Your Name is : {cls.user.name}')
        print(f'Your Screen name is : {cls.user.screen_name}')
        print(f'Count of Your Followers : {cls.user.followers_count}')

    
    def limitHandler(cursor):
        try:
            while(True):
                yield cursor.next()

        except tweepy.RateLimitError:
            time.sleep(1000)
        except StopIteration:
            print('----------')

    @classmethod
    def friendsScreenName(cls): #following
        count =0

        for friends in cls.limitHandler(tweepy.Cursor(cls.api.friends,cls.user.screen_name).items()):
            print(friends.screen_name)
            count+=1
            
        print(f'You have total : {count} Friends.')
    
    @classmethod
    def followFollowers(cls): #do a follow back to entered user
        n = input('Enter Screen name of how you want to follow--> ')
        list1=n.split(',')

        for follower in cls.limitHandler(tweepy.Cursor(cls.api.followers).items()):
            for x in list1:
                if follower.name==x:
                    follower.follow()
                    print(f'Follow Request Accepted : {follower.name}')
                    break

    @classmethod
    def favouriteTweet(cls):

        search_string = input("Enter string to like that tweets : ")
        numoftimes=int(input('Enter no. of times you want to like: '))

        for tweet in tweepy.Cursor(cls.api.search,search_string).items(numoftimes):
    
            try:
                tweet.favorite() #like a tweet
                print('I like that tweet')
            except tweepy.TweepError as err:
                print('this is .............')
                print(err.reason)
            except StopIteration:
                print('error')
                break

    @classmethod
    def reTweet(cls):

        search_string = input("Enter string to Retweets : ")
        numoftimes=int(input('Enter no. of times you want to like: '))

        for tweet in tweepy.Cursor(cls.api.search,search_string).items(numoftimes):
    
            try:
                tweet.retweet() #like a tweet
                print('Retweet Done...!!!')
            except tweepy.TweepError as err:
                print('this is .............')
                print(err.reason)
            except StopIteration:
                print('error')
                break
    
    @classmethod
    def addTweet(cls):
        print('press 1 for adding tweet without media')
        print('press 2 for adding tweet with media')

        t1=int(input('Enter your choice '))

        if(t1==1):
            tweet=input('Enter tweet text--> ')
            cls.api.update_status(tweet)
            print('Done')
        
        if(t1==2):
            tweet=input('Enter tweet text--> ')
            img_name=input("enter image name")
            cls.api.update_with_media(f'.\Twitter_Bot\{img_name}.jpg',tweet)
            print("Done...!!!")




bot=TweetBot()
print('press 1 for TimeLine Tweet')
print('press 2 for TimeLine Tweet')
print('press 3 for TimeLine Tweet')
print('press 4 for TimeLine Tweet')
print('press 5 for TimeLine Tweet')
print('press 6 for TimeLine Tweet')

choice = int('enter your choice ')

if(choice==1):
    bot.myTimeLineTweet()
if(choice==2):
    bot.profileDetails()
if(choice==3):
    bot.friendsScreenName()
if(choice==4):
    bot.followFollowers()
if(choice==5):
    bot.favouriteTweet()
if(choice==6):
    bot.reTweet()
if(choice==7):
    bot.addTweet()

