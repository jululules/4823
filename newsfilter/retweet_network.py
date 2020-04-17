import time
import datetime
import sys
import tweepy
import json

# https://mediaeffectsresearch.wordpress.com/constructing-a-retweet-network/

def get_news_handles():
    keyword = "news"
    screen_name_list = []    
    line_generator = open("tweets_coronavirus_en_2020/03/07/14/30.json")
    for line in line_generator:
        line_object = json.loads(line)
        username_string = line_object["user"]["screen_name"]
        if keyword in username_string.lower():
            screen_name_list.append(username_string)
    return screen_name_list

def collect_retweets(screen_name_list):
    CONSUMER_KEY = 'LMxsDbA4lx7RqWhf2DqGeM1yx'
    CONSUMER_SECRET = 'azc96uPycF05zlIslDudv6YaWM40OIWhOd22VBBFVsUVjtdwdp'
    ACCESS_KEY = '228978699-mFQ0w0U3rEvohSQnuADEOfgu3rqQSIIVEeMMQrbU'
    ACCESS_SECRET = 'cikbqBaSgseWCHIJm3NRXx3WRDgO9zRLkEiSoQest0T7i'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days = today.weekday(), weeks = 1)
    end_date   = start_date + datetime.timedelta(days = 7)
    print('Start date:\t%s' % start_date.isoformat())
    print('End date:\t%s' % end_date.isoformat())
    
    max_id = utc2snowflake(time.mktime(end_date.timetuple()))
    min_id = utc2snowflake(time.mktime(start_date.timetuple()))
    print('min_id:\t%s' % min_id)
    print('max_id:\t%s' % max_id)

    F_NAME = 'mp_retweet_data_(%s_to_%s).json' % (start_date.isoformat(), end_date.isoformat())

    tweets_read = 0
    sn_read = 0
    with open(F_NAME,'w') as f_out:
        for screen_name in screen_name_list:
            try:
                search = api.user_timeline(screen_name = screen_name, min_id = min_id, max_id = max_id, include_rts = True)
            except tweepy.TweepError:
                pass # can't get records from this user, probably a protected account and it is safe to skip
            else:
                for result in search:
                    tweet = result._json
                    if tweet.get('retweeted_status'):
                        json.dump(tweet, f_out)
                        f_out.write('\n')
                        tweets_read += 1
                sn_read += 1
                print('\rUsers read:\t%d/%d\tRetweets read:\t%d' % (sn_read, len(screen_name_list), tweets_read))

    print('\rUsers read:\t%d/%d\tRetweets read:\t%d\tFinished!' % (sn_read, len(screen_name_list), tweets_read))

def utc2snowflake(utc_timestamp):
    return (int(round(utc_timestamp * 1000)) - 1288834974657) << 22

def main():
    screen_name_list = get_news_handles() 
    collect_retweets(screen_name_list)

if __name__ == "__main__":
    main()
