import os
import re
import math
import string
from collections import Counter


# converted_content = []
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
    return unique_list


# Find length of the document vector
def vector_length(column):
    sum = 0
    for i in column:
        sum = sum + i ** 2
    return sum ** (1 / 2)


# Normalize document vector
def normalize_vector(column):
    vector_len = vector_length(column)
    if vector_len > 0:
        for i in range(len(column)):
            column[i] = round(column[i] / vector_len, 3)


# Find cosine similarity of two Normalized document vectors
def cosine_sim(D1, D2):
    sim_vector = 0
    for i in range(len(D1)):
        sim_vector += D1[i] * D2[i]
    return sim_vector


# Find column vector
def column_vector(vector, i):
    return [row[i] for row in vector]


# Returns idf and posting_list and dictionary
def idf(terms):
    posting_list = {}
    IDF = {}
    dictionary = []
    for docid in range(len(terms)):
        term_set = unique(terms[docid])
        for word in term_set:
            try:
                posting_list[word].add((docid, terms[docid].count(word)))
            except:
                posting_list[word] = {(docid, terms[docid].count(word))}
        # sort DF
        posting_list = dict(sorted(posting_list.items()))
    for term in posting_list:
        dictionary.append(term)
        IDF[term] = round(math.log10(len(terms) / len(posting_list[term])), 3)
    return IDF, posting_list, dictionary


# Create Query Vector
def query_vector(query, IDF):
    # Remove lower and remove punctuation when finalized
    query = query.lower()
    # remove punctuations
    query = query.translate(str.maketrans('', '', string.punctuation))
    query_term = query.strip().split()
    query_vector = []
    for term in IDF:
        query_vector.append(IDF[term] * query_term.count(term))
    # Normalize Query Vector
    normalize_vector(query_vector)
    return query_vector


# creates a vector model for a corpus (content of file)
def document_representation(IDF, posting_list, no_of_docs):
    row = len(IDF)
    doc_rep = [[0 for i in range(no_of_docs)] for j in range(row)]
    # Keep count of term id
    k = 0
    for posting in posting_list:
        for (doc_id, count) in posting_list[posting]:
            doc_rep[k][doc_id] = count * IDF[posting]
        k += 1

    # Normalize document representation
    lengths_of_vector = []
    for i in range(no_of_docs):
        doc_vector = column_vector(doc_rep, i)
        lengths_of_vector.append(vector_length(doc_vector))

    for i in range(row):
        for j in range(no_of_docs):
            doc_rep[i][j] = round(doc_rep[i][j] / lengths_of_vector[j], 3)
    return doc_rep


# Print vectors
def print_vectors(doc_representation, dictionary):
    for col in range(len(doc_representation[0])):
        print(f'\tD{col}', end='')
    # print()
    for row in range(len(doc_representation)):
        print(dictionary[row], end='\t')
        for col in range(len(doc_representation[row])):
            print(doc_representation[row][col], end='\t')
        print()


# Cosine Rank Vector/Dictionary from normalized query vector and normalized doc rep
def cosine_rank(doc_representation, query_vector):
    rank_dict = {}
    for col in range(len(doc_representation[0])):
        doc = f'D{col}'
        cos_sim = round(cosine_sim(column_vector(doc_representation, col), query_vector), 3)
        rank_dict[doc] = cos_sim
    return dict(sorted(rank_dict.items(), key=lambda kv: kv[1], reverse=True))


# Relevant doc in form ['D1', 'D2'] or [1,2, ---, n]
def centroid(doc_rep, documents):
    no_relevant_doc = len(documents)
    row_doc_rep = len(doc_rep)
    if no_relevant_doc <= 0:
        return 0
    elif isinstance(documents[0], str):
        documents = [int(doc[1:]) for doc in documents]
    sum_vector = [0 for i in range(len(doc_rep))]
    for i in documents:
        sum_vector = [sum_vector[j] + column_vector(doc_rep, i)[j] for j in range(row_doc_rep)]
    return [round(sum_vector[i] / no_relevant_doc, 3) for i in range(row_doc_rep)]


# Rochhio Algorithm on normalized docs, discarding irrelevant documents
# Relevant doc in form ['D1', 'D2'] or [1,2]
def rochhio_algorithm(alpha, beta, gamma, doc_rep, query_vector, relevant_doc, irelevant_docs):
    len_vector = len(query_vector)
    cen_rel_vector = centroid(doc_rep, relevant_doc)
    if irelevant_docs is not None:
        cen_irl_vector = centroid(doc_rep, irelevant_docs)
        return [round(alpha * query_vector[i] + beta * cen_rel_vector[i] - gamma * cen_irl_vector[i], 3) for i in
                range(len_vector)]
    else:
        return [round(alpha * query_vector[i] + beta * cen_rel_vector[i], 3) for i in range(len_vector)]


# Currently Not Used
def tf_idf(IDF, terms):
    tfidf = {}
    N = len(terms)
    for i in range(N):
        term = terms[i]
        for word in unique(term):
            tf = term.count(word)
            idf = IDF[word]
            # we cannot divide by 0, we smoothen the value by adding 1 to the denominator, No need. DF cannot be zero
            tfidf[i, word] = tf * idf
    return tfidf


# with open("output.txt", "r") as data:
#     contents = data.readlines()
#     terms = []
#     # print((converted_content))
#     no_of_documents = len(contents)  # Counting the tweet as a single document
#     for content in contents:
#         # conversion to lower case
#         content = content.lower()
#         # remove punctuations
#         content = content.translate(str.maketrans('', '', string.punctuation))
#         content = content.strip().split()
#         # for term in content:
#         terms.append(content)
#     IDF, posting_list, dictionary = idf(terms)
#     doc_rep = document_representation(IDF, posting_list, len(terms))
#     print_vectors(doc_rep, dictionary)
#     Q1 = 'Gold Silver Truck.'
#     qv = query_vector(Q1, IDF)
#     print(cosine_rank(doc_representation=doc_rep, query_vector=qv))
#     relevant_docs = ['D1', 'D3']
#     avg = centroid(doc_rep, relevant_docs)
#     # print(avg)
#     alpha = 1
#     beta = 0.5
#     relevant_qv = rochhio_algorithm(alpha, beta, doc_rep, qv, relevant_docs)
#     normalize_vector(relevant_qv)
#     # print(relevant_qv)
#     print(cosine_rank(doc_rep, relevant_qv))

def run_data_file(stemmed_data_file, query, rl, irl, doc_list):
    with open(stemmed_data_file, "r") as data:
        contents = data.readlines()
        terms = []
        # print((converted_content))
        no_of_documents = len(contents)  # Counting the tweet as a single document
        for content in contents:
            # conversion to lower case
            content = content.lower()
            # remove punctuations
            content = content.translate(str.maketrans('', '', string.punctuation))
            content = content.strip().split()
            # for term in content:
            terms.append(content)
        IDF, posting_list, dictionary = idf(terms)
        doc_rep = document_representation(IDF, posting_list, len(terms))
        # print_vectors(doc_rep, dictionary)
        Q1 = query
        qv = query_vector(Q1, IDF)
        # print(cosine_rank(doc_representation=doc_rep, query_vector=qv))
        alpha = 1
        beta = 0.5
        gamma = 0.15
        irelevant_docs = None
        if irl:
            irelevant_docs = doc_list
        if rl:
            relevant_docs = doc_list
        else:
            relevant_docs = ['D1', 'D3']
        relevant_qv = rochhio_algorithm(alpha, beta, gamma, doc_rep, qv, relevant_docs, irelevant_docs)
        normalize_vector(relevant_qv)
        # print(relevant_qv)
        final_output = cosine_rank(doc_rep, relevant_qv)
        # print(final_output)
        return final_output
