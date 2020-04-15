import sys;
import json;


def get_news_handles(filename):
    keyword = "news"
    screen_name_list = []
    try:
        line_generator = open(filename)
    except:
        print("no file named " + filename.__str__())
        return
    for line in line_generator:
        line_object = json.loads(line)
        username_string = line_object["user"]["screen_name"]
        if keyword in username_string.lower():
            screen_name_list.append(username_string)
            print(username_string)
    return screen_name_list


def get_handles_on_day():
    fname = "tweets_coronavirus_en_2020/03/01/"
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
            get_news_handles(file)
            #print(file)


get_handles_on_day()