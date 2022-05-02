import tweepy
import re
import json

# API Keys and Tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def remove_new_line(string_to_remove_new_line):
    return string_to_remove_new_line.strip().replace("\n", "")


def remove_mentions(tweet):
    return re.sub("@[A-Za-z0-9_]+", "", tweet).strip()

def remove_url (tweet):
    return re.sub(r'http\S+', '', tweet).strip()

def remove_hashtag(tweet):
    return re.sub("#[A-Za-z0-9_]+", "", tweet).strip()

def remove_emojis(tweet):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', tweet).strip()

# removes white space and checks appha numeric
def is_alpha_numeric (tweet):
    pattern = re.compile(r'\s+')
    tweet = re.sub(pattern, '', tweet)
    return tweet.strip().isalnum()

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
        tweet = tweet.full_text
        tweet = remove_new_line(tweet)
        data = remove_emojis(tweet)
        data = remove_hashtag(data)
        data = remove_mentions(data)
        data = remove_url(data)
        if not is_alpha_numeric(data) and len(data) > 0:
            print('data', data, len(data))
            raw_data.write(tweet + "\n")
        document_name += 1
    raw_data.close()


if __name__ == "__main__":
    # text = '@caius__21 إنها پوپيات الصدمة كيتعرف بلي لفغونس صح حطت جزائريين قراب  الانفجار كل ڤروپ و شحال بعيد ؤ كاين الي دخلوهم داخل برامل نتع أنواع مختلفة من المعادن باش يعرفو واش يصرا لبناد كاين واحد منلي سلكو قالك البرميل الي كان داخلو فيه ثقبا صغيرة كي دخل لفلاش ولا مايشوف والو وما خفي كان أعظم️'
    # print(text)
    # text = remove_emojis(text)
    # print(text)
    # text = remove_url(text)
    # print(text)
    # text = remove_mentions(text)
    # print(text)
    # text = remove_hashtag(text)
    # print(text)
    # print(text.isalnum())

    extract_top_tweets("../data_collection/raw_tweets.txt")
