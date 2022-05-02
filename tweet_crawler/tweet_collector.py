import tweepy
import re
import json
from tweet_crawler.utils import *

# API Keys and Tokens
consumer_key = "kzOZpB6hBK621z4horT3axCs6"
consumer_secret = "x3Tz2fxvEdhV95j6KM5prMu0wMLDW8HfqS5N3gjdMdEZytVl3v"
access_token = "1119541254-Gavfixo22v3Sy810IAjeUfHB2HfKzAVHobzVGdA"
access_token_secret = "aFRzUxgj29ofxcoEKxTYAg6AacNLSzB8EzCBROOX3MaE9"


# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def extract_top_tweets(file_to_write_raw_data):
    # places = api.search_geo(query="USA", granularity="country")
    # print(places)
    # #96683cc9126741d1
    # place_id = places[0].id
    place_id = '96683cc9126741d1'
    tweets = api.search_tweets(q="place:%s" % place_id, count=1000, tweet_mode='extended')
    print(len(tweets))
    # obj = json.loads(tweets)
    # json_formatted_str = json.dumps(obj, indent=4)
    # print(json_formatted_str)
    raw_data = open(file_to_write_raw_data, "w")
    document_name = 0
    for tweet in tweets:
        tweet = tweet.full_text
        tweet = remove_new_line(tweet)
        data = remove_emojis(tweet)
        data = remove_url(data)
        data = remove_stopwords(data)
        data = remove_hashtag(data)
        data = remove_mentions(data)
        data = remove_punctuations(data)
        if is_alpha_numeric(data) and len(data) > 0:
            raw_data.write(tweet + "\n")
        document_name += 1
    raw_data.close()


if __name__ == "__main__":
    extract_top_tweets("../data_collection/raw_tweets.txt")
