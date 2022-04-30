import os
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#Install nltk.download('punkt') too
def token_stemmer():
    tweets = []
    filter_tweet = []
    tweet = []
    ps = PorterStemmer()
    final_tweet = ""

    with open("raw_tweets.txt", "r") as data:
        contents = data.readlines()
        for content in contents:

            # content = content.encode('ascii', 'ignore').decode('ascii')#remove all non-ascii characters
            content = re.sub(r'http\S+', '',content)# removes urls
            content = re.sub(r'❤️+','', content)
            content = re.sub(r'[^\x00-\x7F]+', '', content)
            content = re.sub(r'  ','',content)
            # content = re.sub(r'\n','',content)


            tweets.append(word_tokenize(content))
        stop_words = stopwords.words('english')
        new_words = ["!", "/", "#", ".", "@", " ", "[", "?","]","'", '"', ":", ";", ",", "-", "(", ")","``"] # some addition to the nltk stopwords
        stop_words.extend(new_words)
        for words in tweets:
            filter_tweet.append([word for word in words if not word.lower() in stop_words])
        for words in filter_tweet:

            tweet.append([ps.stem(word) for word in words])
        tweet = list(filter(lambda x: x, tweet))
        # print(tweet)
        for list1 in tweet:
            final_tweet += ' '.join(word for word in list1)
            final_tweet += "\n"
        print(final_tweet)
        # while("" in final_tweet) :
            # final_tweet.remove("")
        return(final_tweet)
        # print(final_tweet)

if __name__ == "__main__":
    token_stemmer()
