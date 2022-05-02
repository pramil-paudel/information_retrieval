import os

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from services.tweet_irs import TweetIrs


def test(request):
    return render(request, 'index.html', {"tweets": ""})


def search(request):
    search_query = request.GET.get('query', None)
    query = search_query
    twitter_search_service = TweetIrs()
    # Calling Stemmer
    twitter_search_service.extract_new_updated_tweets(True)
    twitter_search_service.tokenize_and_stemming_the_data()
    query = twitter_search_service.tokenize_and_stemming_the_query(query)

    twitter_search_service.tfidf_and_vector_space_model(query, False, False, [])

    stemmed_ranked_file = twitter_search_service.get_stemmed_ranked_doc()
    # First Read Stemmed dict and send it to front
    final_output_one = {}
    stemmed_output = open(stemmed_ranked_file, "r").readlines()
    for line in stemmed_output:
        line_split = line.split("|")
        final_output_one[line_split[0]] = line_split[1]
    return render(request, 'index.html', {"ranked_tweets": final_output_one, "query_data": query})


def stemmed_document(request):
    query = request.GET.get('query_data', None)

    final_output_one = {}
    stemmed_output = open("data_collection/stemmed_ranked_document.txt", "r").readlines()
    for line in stemmed_output:
        line_split = line.split("|")
        final_output_one[line_split[0]] = line_split[1]
    return render(request, 'index.html', {"ranked_tweets": final_output_one, "query_data": query})


def raw_document(request):
    query = request.GET.get('query_data', None)

    final_output_one = {}
    stemmed_output = open("data_collection/raw_ranked_document.txt", "r").readlines()
    for line in stemmed_output:
        line_split = line.split("|")
        final_output_one[line_split[0]] = line_split[1]
    return render(request, 'index.html', {"ranked_tweets": final_output_one, "query_data": query})


def relevant_data(request):
    query = request.GET.get('query_data', None)
    tweet_id = request.GET.get('tweet_id', None)
    irelevant_doc = [str("D" + str(tweet_id))]
    twitter_search_service = TweetIrs()
    query = twitter_search_service.tokenize_and_stemming_the_query(query)
    twitter_search_service.tfidf_and_vector_space_model(query, False, True, irelevant_doc)
    stemmed_ranked_file = twitter_search_service.get_stemmed_ranked_doc()
    # First Read Stemmed dict and send it to front
    final_output_one = {}
    stemmed_output = open(stemmed_ranked_file, "r").readlines()
    for line in stemmed_output:
        line_split = line.split("|")
        final_output_one[line_split[0]] = line_split[1]
    return render(request, 'index.html', {"ranked_tweets": final_output_one, "query_data": query})

def irelevant_data(request):
    query = request.GET.get('query_data', None)
    tweet_id = request.GET.get('tweet_id', None)
    relevant_doc = [str("D" + str(tweet_id))]
    twitter_search_service = TweetIrs()
    query = twitter_search_service.tokenize_and_stemming_the_query(query)
    twitter_search_service.tfidf_and_vector_space_model(query, True, False, relevant_doc)
    stemmed_ranked_file = twitter_search_service.get_stemmed_ranked_doc()
    # First Read Stemmed dict and send it to front
    final_output_one = {}
    stemmed_output = open(stemmed_ranked_file, "r").readlines()
    for line in stemmed_output:
        line_split = line.split("|")
        final_output_one[line_split[0]] = line_split[1]
    return render(request, 'index.html', {"ranked_tweets": final_output_one, "query_data": query})
