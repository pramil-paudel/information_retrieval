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


def extract_top_tweets():
    places = api.geo_search(query="USA", granularity="country")
    place_id = places[0].id
    tweets = api.search(q="place:%s" % place_id, count=1000)
    raw_data = open("raw_tweets.txt","w")
    document_name = 0
    for tweet in tweets:
        # print(document_name + "|" + tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place")
        raw_data.write(str(document_name) + "|" + tweet.text + "\n")
        document_name +=1
    raw_data.close()


if __name__ == "__main__":
    extract_top_tweets()
