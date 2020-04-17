import tweepy
import json
import filter_by_handle as handles

CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True)

snames = handles.get_info_minute()
print(len(snames))

def rt_fav_list(snames, api):
    for name in snames:
        try:
            timeline = api.user_timeline(name)
        except:
            timeline = []
        print(name)
        rts = 0
        favs = 0
        if len(timeline) > 3:
            for tweet in timeline:
                #tweet_info = [tweet.retweet_count, tweet.favorite_count]
                rts = rts + tweet.retweet_count
                favs = favs + tweet.favorite_count
                #print(tweet_info)
                #tweet_id = tweet.id
                #try:
                #    retweeters = api.retweeters(tweet.id)
                #    print(retweeters)
                #except:
                #    pass
            data = [rts, favs]
            print(data)
            print("  ")
            print("-----------")
            print("  ")


def rt_fav_single(name, api):
    try:
        timeline = api.user_timeline(name)
    except:
        timeline = []
    print(name)
    rts = 0
    favs = 0
    data = [0, 0]
    if len(timeline) > 3:
        for tweet in timeline:
            # tweet_info = [tweet.retweet_count, tweet.favorite_count]
            rts = rts + tweet.retweet_count
            favs = favs + tweet.favorite_count
            # print(tweet_info)
            # tweet_id = tweet.id
            # try:
            #    retweeters = api.retweeters(tweet.id)
            #    print(retweeters)
            # except:
            #    pass
        data = [rts, favs]
        #print(data)
        #print("  ")
        #print("-----------")
        #print("  ")
    return data
