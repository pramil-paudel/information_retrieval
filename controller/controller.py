import os

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from tweet_crawler.tweet_collector import extract_top_tweets


def test(request):
    return render(request, 'index.html', {"tweets": ""})


def search(request):
    extract_top_tweets
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'raw_tweets.txt')
    print(file_path)
    input_file = open(file_path,"r")
    tweets = []
    for line in input_file:
        tweets.append(line)
    print(tweets)
    return render(request, 'index.html', {"tweets": tweets[:10]})

    # return HttpResponse("Hello, World!")
