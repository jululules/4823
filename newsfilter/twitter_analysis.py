#Jules Henry, Ahmir Ghorbanian
#Spring 2020

#Script to run point analysis on given tweet data.
#Returns and prints score information and writes to text files.



import retweeters
import filter_by_handle
import tweepy


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
    print(points)
    return rep


CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

f=open("results.txt", "a+")
f2=open("cred_sources.txt", "a+")

snames = filter_by_handle.get_info_month()

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
        link = user.url.__str__()
        following = user.friends_count.__str__()
        followers = user.followers_count.__str__()
        id = user.id.__str__()
        favorites = user.favourites_count.__str__()
        rts = data[0].__str__()
        favs = data[1].__str__()

        if cred:
            credibility = "yes"
            f2.write(screen_name + "," + verified + "," + followers + "," + following + "," + rts + "," + favs + "," + num_tweets + "," + credibility)
            f2.write("\n")
        else:
            credibility = "no"

        f.write(screen_name + "," + verified + "," + followers + "," + following + "," + rts + "," + favs + "," + num_tweets + "," + credibility)
        f.write("\n")

        print("screen name: @" + screen_name)
        print("verified: " + verified)
        # print("private: " + protect)
        print("number of tweets: " + num_tweets)
        # print("link in bio: " + bio)
        print("following: " + following)
        print("followers: " + followers)
        print(data)
        print(info)
        print("credible: ")
        print(cred)
        print("  ")
        print("-----------")
        print("  ")
    except tweepy.TweepError:
        pass
        print("user couldn't be fetched")
f.close()
f2.close()