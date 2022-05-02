import os
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from tweet_crawler.utils import *

nltk.download('punkt')


# Install nltk.download('punkt') too


def tokenize(tweet):
    tweet = remove_new_line(tweet)
    tweet = remove_emojis(tweet)
    tweet = remove_hashtag(tweet)
    tweet = remove_mentions(tweet)
    tweet = remove_url(tweet)
    tweet = remove_punctuations(tweet)
    tweet = remove_symbols(tweet)
    tweet = tweet.lower()
    return tweet


def tokenizing_and_stemming(raw_file_name, output_directory):
    tweets = []
    filter_tweet = []
    tweet = []
    ps = PorterStemmer()
    final_tweet = ""

    with open(raw_file_name, "r") as data:
        contents = data.readlines()
        for content in contents:
            content = tokenize(content)
            tweets.append(word_tokenize(content))
        stop_words = stopwords.words('english')
        # Used method to remove symbols.
        # new_words = ["!", "/", "#", ".", "@", " ", "[", "?", "]", "'", '"', ":", ";", ",", "-", "(", ")",
        #              "``"]  # some addition to the nltk stopwords
        # stop_words.extend(new_words)
        for words in tweets:
            filter_tweet.append([word for word in words if not word.lower() in stop_words])
        for words in filter_tweet:
            tweet.append([ps.stem(word) for word in words])
        tweet = list(filter(lambda x: x, tweet))
        # print(tweet)
        for list1 in tweet:
            final_tweet += ' '.join(word for word in list1)
            final_tweet += "\n"
        # print(final_tweet)
        # Write stemmer_output_in_a_file
        output_file_name = "stemmer_output.txt"
        output_file_path = output_directory + "/" + output_file_name
        output_data = open(output_directory + "/" + output_file_name, "w")
        output_data.write(final_tweet)
        return output_file_path


def tokenizing_and_stemming_a_query(query_to_stem):
    tweets = []
    filter_tweet = []
    tweet = []
    ps = PorterStemmer()
    final_tweet = ""

    contents = [query_to_stem]
    for content in contents:
        # content = content.encode('ascii', 'ignore').decode('ascii')#remove all non-ascii characters
        content = tokenize(content)
        # content = re.sub(r'\n','',content)

        tweets.append(word_tokenize(content))
    stop_words = stopwords.words('english')

    for words in tweets:
        filter_tweet.append([word for word in words if not word.lower() in stop_words])

    for words in filter_tweet:
        tweet.append([ps.stem(word) for word in words])
    tweet = list(filter(lambda x: x, tweet))

    for list1 in tweet:
        final_tweet += ' '.join(word for word in list1)
        final_tweet += "\n"
    return final_tweet


if __name__ == "__main__":
    print(tokenizing_and_stemming_a_query("Hello + World !! "))
