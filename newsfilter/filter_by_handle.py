import sys;
import json;



keyword = "news"

if len(sys.argv)>1:
    line_generator = open(sys.argv[1])
else:
    line_generator = open("tweets_coronavirus_en_2020/03/07/14/30.json")

for line in line_generator:
    line_object = json.loads(line)
    username_string = line_object["user"]["screen_name"]
    if keyword in username_string.lower():
        print(username_string)

