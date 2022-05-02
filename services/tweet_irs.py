# import twitter_search.twitter_search.stemmer
# import twitter_search.vsm.toeknizer
# import twitter_search.vsm.indexer
# import twitter_search.vsm.query_builder
import os
from tweet_crawler import tweet_collector
from stemmer import stemmer
from vsm import vector_space_model

'''
During run time itself program will fetch new tweets from USA region and parse them in a file.

'''


class TweetIrs:
    def __init__(self):
        self.name = "search_service"
        self.data_directory = "data_collection"
        self.data_location = "data_collection/raw_tweets.txt"
        self.stemmer_output = "data_collection/stemmer_output.txt"
        self.stemmed_ranked_document = "data_collection/stemmed_ranked_document.txt"
        self.raw_ranked_document = "data_collection/raw_ranked_document.txt"

    def get_stemmed_ranked_doc(self):
        return self.stemmed_ranked_document

    def get_raw_ranked_doc(self):
        return self.raw_ranked_document

    def extract_new_updated_tweets(self, refresh=False):
        if refresh:
            if not os.path.isdir(self.data_directory):
                os.makedirs(self.data_directory)
            file_to_write_raw_data = self.data_location
            tweet_collector.extract_top_tweets(file_to_write_raw_data)

    def tokenize_and_stemming_the_data(self):
        self.stemmer_output = stemmer.tokenizing_and_stemming(self.data_location, self.data_directory)

    def tokenize_and_stemming_the_query(self, query):
        return stemmer.tokenizing_and_stemming_a_query(query)

    def tfidf_and_vector_space_model(self, query, rl, irl, list):
        output_dict = vector_space_model.run_data_file(self.stemmer_output, query, rl, irl, list)
        stemmed_unranked_document_reader = open(self.stemmer_output, "r").readlines()
        raw_unranked_document_reader = open(self.data_location, "r").readlines()

        # stemmed_ranked_document

        stemmed_ranked_document_name = self.data_directory + "/" + "stemmed_ranked_document.txt"
        stemmed_ranked_document = open(stemmed_ranked_document_name, "w")
        # stemmed_ranked_document.write("Tweet/Document | Cosine Similarity" + "\n")
        self.stemmed_ranked_document = stemmed_ranked_document_name

        raw_ranked_document_name = self.data_directory + "/" + "raw_ranked_document.txt"
        raw_ranked_document = open(raw_ranked_document_name, "w")
        # raw_ranked_document.write("Tweet/Document | Cosine Similarity" + "\n")
        self.raw_ranked_document = raw_ranked_document_name

        for key, value in output_dict.items():
            line_number = int(key[1:])
            content_two_write_in_stemmed = stemmed_unranked_document_reader[line_number].strip() + "|" + str(value)
            content_two_write_in_raw = raw_unranked_document_reader[line_number].strip() + "|" + str(value)
            stemmed_ranked_document.write(content_two_write_in_stemmed + "\n")
            raw_ranked_document.write(content_two_write_in_raw + "\n")
        stemmed_ranked_document.close()
        raw_ranked_document.close()
