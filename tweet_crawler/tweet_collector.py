import tweepy
import json
import re

# API Keys and Tokens
consumer_key = "kzOZpB6hBK621z4horT3axCs6"
consumer_secret = "x3Tz2fxvEdhV95j6KM5prMu0wMLDW8HfqS5N3gjdMdEZytVl3v"
access_token = "1119541254-Gavfixo22v3Sy810IAjeUfHB2HfKzAVHobzVGdA"
access_token_secret = "aFRzUxgj29ofxcoEKxTYAg6AacNLSzB8EzCBROOX3MaE9"


# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def remove_new_line(string_to_remove_new_line):
    return string_to_remove_new_line.strip().replace("\n", "")


def extract_top_tweets(file_to_write_raw_data):
    # places = api.search_geo(query="USA", granularity="country")
    # print(places)
    # #96683cc9126741d1
    # place_id = places[0].id
    place_id = '96683cc9126741d1'
    tweets = api.search_tweets(q="place:%s" % place_id, count=1000, tweet_mode='extended')
    # obj = json.loads(tweets)
    # json_formatted_str = json.dumps(obj, indent=4)
    # print(json_formatted_str)
    raw_data = open(file_to_write_raw_data, "w")
    document_name = 0
    for tweet in tweets:
        tweet = re.sub(r'http\S+','',tweet.full_text)
        # raw_data.write(remove_new_line(str(document_name)) + "|" + tweet.text + "\n")
        raw_data.write(remove_new_line(tweet) + "\n")
        document_name += 1
    raw_data.close()


if __name__ == "__main__":
    extract_top_tweets("../data_collection/raw_tweets.txt")
