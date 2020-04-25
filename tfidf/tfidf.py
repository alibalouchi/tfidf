import pandas as pd
import re
import math
import nltk
from nltk.corpus import names
from nltk.tokenize import word_tokenize

# This line should uncomment for the first time and the commented out
nltk.download('names')
nltk.download('punkt')

def TF_IDF(csv_file, stop_word_file, number_of_words, documents_id_key_index, document_index):
    word_dict = {}

    newDB_overview = []
    new_csv = pd.read_csv(csv_file)
    for item in new_csv.iterrows(): 
        item = item[1].tolist()
        newDB_overview.append([item[documents_id_key_index], item[document_index]])

    def stop_words(array_of_words):
        stop_word = open(stop_word_file).read().split("\n")
        for name in names.words('male.txt'):
            stop_word.append(name.lower())
        for name in names.words('female.txt'):
            stop_word.append(name.lower())
        res = []
        for word in array_of_words:
            if word in stop_word:
                continue
            else:
                res.append(word)
                continue
        return res

    overviews = []

    for overview in newDB_overview:
        if str(overview[1]) != 'nan':
            raw_words = list(word_tokenize(overview[1]))
            raw_words = list(map(lambda word: word.lower(), raw_words))
            word = [stop_words(raw_words), overview[0]]
            overviews.append(word)

    for overview in overviews:
        for word in overview[0]:
            if word in word_dict.keys():
                word_dict[word]["occurence"] = word_dict[word]["occurence"] + 1
                word_dict[word]["documents"].append(overview[1])
            else:
                word_dict[word] = {}
                word_dict[word]["occurence"] = 1
                word_dict[word]["documents"] = []
                word_dict[word]["documents"].append(overview[1])

    for word in word_dict:
        word_dict[word]["TF_IDF"] = word_dict[word]["occurence"] * math.log10(len(overviews) / len(word_dict[word]["documents"]))

    result = {}
    for overview in overviews:
        result[overview[1]] = {}
        for word in overview[0]:
            if word in word_dict.keys():
                result[overview[1]][word] = word_dict[word]["TF_IDF"]
        result[overview[1]] = sorted(result[overview[1]].keys(), key=lambda x: result[overview[1]][x], reverse=True)
        if len(result[overview[1]]) > number_of_words:
            result[overview[1]][number_of_words:] = []

    final_result = {}
    for movie in result.keys():
        final_result[movie] = []    
        for word in range(len(result[movie])):
            final_result[movie].append((result[movie][word], word_dict[result[movie][word]]["TF_IDF"]))
    
    return final_result
