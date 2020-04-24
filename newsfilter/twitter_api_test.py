#Jules Henry, Ahmir Ghorbanian
#Spring 2020

#Test script to run analysis on individual accounts.
#Prints accounts infomation and score result.


import tweepy

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
            rts = rts + tweet.retweet_count
            favs = favs + tweet.favorite_count
        data = [rts, favs]
    return data


CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True)
name = 'wilxtv'
user = api.get_user(name)
verified = user.verified
protect = user.protected
num_tweets = user.statuses_count
bio = user.description
link = user.url
following = user.friends_count
followers = user.followers_count
id = user.id
favorites = user.favourites_count

data = rt_fav_single(name, api)
info = [verified, followers, following, data[0], data[1], num_tweets]

print(info)

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
print(points)

