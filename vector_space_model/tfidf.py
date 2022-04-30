import os
import re
import math
from collections import Counter
converted_content = []


# print(contents)
# Returns Document Frequency
def doc_freq(terms):
    DF = {}

    for count in range(len(terms)):
        term = terms[count]
        for word in term:
            try:
                DF[word].add(count)
                # print(DF)
            except:
                DF[word] = {count}
    # print(dict(sorted(DF.items())))
    for i in DF:
        DF[i] = len(DF[i])
    # print(DF)
    # print(DF['like'])
    return DF
def unique(T):

    # insert the list to the set
    lset = set(T)
    # convert the set to the list
    unique_list = (list(lset))
    # print(A)
    return unique_list
def tf_idf(DF, terms):
    tfidf = {}
    # tf = {}
    N = len(terms)
    for i in range(N):
        term = terms[i]
        # count = 0
        for word in unique(term):
            tf = term.count(word)
            df = DF[word]
            # print("{} {}".format(word,df))
            idf = math.log(N/(df+1)) #we cannot divide by 0, we smoothen the value by adding 1 to the denominator.
            tfidf[i,word] = tf*idf
            # print("{} {}".format(word,tf))
    # print(tfidf)
    return tfidf





with open("output.txt", "r") as data:
    contents = data.readlines()
    terms = []
    # print((converted_content))
    no_of_documents = len(contents) #Counting the tweet as a single document
    for content in contents:
        # print(content)
        content = content.split()
        # print(type(terms))
        terms.append(content)
    # print()
    # print(len(terms))
    DF1 = doc_freq(terms)
    tf_idf(DF1, terms)

    # print(contents.split())
    # print(no_of_documents)
