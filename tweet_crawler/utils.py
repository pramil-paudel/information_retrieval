import re
import string


def remove_new_line(string_to_remove_new_line):
    return string_to_remove_new_line.strip().replace("\n", "")


def remove_mentions(tweet):
    return re.sub("@[A-Za-z0-9_]+", "", tweet).strip()


def remove_url(tweet):
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


def remove_punctuations(tweet):
    return tweet.translate(str.maketrans('', '', string.punctuation))


def remove_symbols(tweet):
    tweet = re.sub(r'[^\w]', ' ', tweet)
    # removes single alphabets
    tweet = re.sub(r'(?:^| )\w(?:$| )', ' ', tweet)
    # removes multiple spaces
    return re.sub(' +', ' ', tweet)


# removes white space and checks appha numeric
def is_alpha_numeric(tweet):
    pattern = re.compile(r'\s+')
    tweet = re.sub(pattern, '', tweet)
    return tweet.strip().isalnum()

# remove single character alphabets
