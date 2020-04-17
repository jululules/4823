import filter_by_handle
import tweepy

CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)


namelist = filter_by_handle.get_info_minute()

print(len(namelist).__str__() + " accounts")

for x in namelist:
    try:
        user = api.get_user(x)
        screen_name = user.screen_name
        verified = user.verified.__str__()
        protect = user.protected.__str__()
        num_tweets = user.statuses_count.__str__()
        bio = user.description.__str__()
        link = user.url.__str__()
        following = user.friends_count.__str__()
        followers = user.followers_count.__str__()
        id = user.id.__str__()
        favorites = user.favourites_count.__str__()
        print("screen name: @" + screen_name)
        print("verified: " + verified)
        #print("private: " + protect)
        print("number of tweets: " + num_tweets)
        #print("link in bio: " + bio)
        print("following: " + following)
        print("followers: " + followers)
        print("favorites: " + favorites)
        print("  ")
        print("-----------")
        print("  ")

    except:
        print("user couldnt be fetched")
        print("  ")
        print("-----------")
        print("  ")





