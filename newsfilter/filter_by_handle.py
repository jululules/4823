import sys;
import json;


def get_info_day():
    screen_name_list = []
    fname = "tweets_coronavirus_en_2020/03/11/"
    for x in range(24):
        if x < 10:
            fopen = fname + "0" + x.__str__() + "/"
        else:
            fopen = fname + x.__str__() + "/"
        for x in range(60):
            if x < 10:
                file = fopen + "0" + x.__str__() + ".json"
            else:
                file = fopen + x.__str__() + ".json"
            keyword = "news"
            try:
                line_generator = open(file)
            except:
                print("no file named " + file.__str__())
                line_generator = []
            for line in line_generator:
                line_object = json.loads(line)
                userinfo_string = line_object["user"]["screen_name"]
                if keyword in userinfo_string.lower():
                    screen_name_list.append(userinfo_string)
                    userinfo_list = [line_object["user"]["screen_name"], line_object["id"],line_object["retweet_count"]]
                    print(userinfo_list)
    return screen_name_list

def get_info_minute():
    screen_name_list = []
    fname = "tweets_coronavirus_en_2020/03/11/10/19.json"
    keyword = "news"
    try:
        line_generator = open(fname)
    except:
        print("no file named " + fname.__str__())
        line_generator = []
    for line in line_generator:
        line_object = json.loads(line)
        userinfo_string = line_object["user"]["screen_name"]
        if keyword in userinfo_string.lower():
            screen_name_list.append(userinfo_string)
            userinfo_list = [line_object["user"]["screen_name"], line_object["id"], line_object["retweet_count"]]
            #print(userinfo_list)
    return screen_name_list

def get_info_hour():
    screen_name_list = []
    fopen = "tweets_coronavirus_en_2020/03/11/10/"
    keyword = "news"
    for x in range(60):
        if x < 10:
            file = fopen + "0" + x.__str__() + ".json"
        else:
            file = fopen + x.__str__() + ".json"
        keyword = "news"
        try:
            line_generator = open(file)
        except:
            print("no file named " + file.__str__())
            line_generator = []
        for line in line_generator:
            line_object = json.loads(line)
            userinfo_string = line_object["user"]["screen_name"]
            if keyword in userinfo_string.lower():
                screen_name_list.append(userinfo_string)
                userinfo_list = [line_object["user"]["screen_name"], line_object["id"], line_object["retweet_count"]]
                print(userinfo_list)
    return screen_name_list

