import retweeters
import filter_by_handle
import tweepy
import json


def points_eval(info):
    points = 0
    rep = 0
    if info[0]:
        points = points+3
    if info[1] > 10000:
        points = points+2
    if info[2] < 2000:
        points = points+1
    if info[3] > 10:
        points = points+2
    if info[4] > 10:
        points = points+1
    if info[5] > 25000:
        points = points+1
    if points > 4:
        rep = 1 
    return rep


CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

snames = filter_by_handle.get_info_minute()

for name in snames:
    data = retweeters.rt_fav_single(name, api)
    try:
        user = api.get_user(name)
        screen_name = user.screen_name
        info = [user.verified, user.followers_count, user.friends_count, data[0], data[1], user.statuses_count]
        cred = points_eval(info)
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
        # print("private: " + protect)
        print("number of tweets: " + num_tweets)
        # print("link in bio: " + bio)
        print("following: " + following)
        print("followers: " + followers)
        #print("favorites: " + favorites)
        print(data)
        print(info)
        print("credible: ")
        print(cred)
        print("  ")
        print("-----------")
        print("  ")
    except:
        pass
        print("user couldn't be fetched")
