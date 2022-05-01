import tweepy

# API Keys and Tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def extract_top_tweets(file_to_write_raw_data):
    places = api.geo_search(query="USA", granularity="country")
    place_id = places[0].id
    tweets = api.search(q="place:%s" % place_id, count=1000)
    raw_data = open(file_to_write_raw_data, "w")
    document_name = 0
    for tweet in tweets:
        #raw_data.write(str(document_name) + "|" + tweet.text + "\n")
        raw_data.write(tweet.text + "\n")
        document_name += 1
    raw_data.close()


if __name__ == "__main__":
    extract_top_tweets("")
