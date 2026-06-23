import re
import json

TEXT_KEY = 'reviewText'
WORDS_KEY = 'words'
WORD_COUNT_KEY = 'word_count'

def read_json_file(path):
                   if not path:
                         raise Exception("You must provide a valid file path.")
                   try:
                         dataset = list()
                         with open(path) as json_file:
                              for line in json_file:
                                   dataset.append(json.loads(line))
                         return dataset
                   except (IOError, OSError):
                           raise Exception("You must provide a valid JSON file.")

def compute_word_count(words):
        if type(words) != list:
                raise Exception("Words must be a list")
        word_count = dict()
        for word in words:
               if word in word_count:
                    word_count[word] = word_count[word]+1
               else:
                    word_count[word] = 1
        return word_count

def compute_word_count_review(review):
       if type(review) != dict:
              raise Exception("Review must be a dictionary")
       new_review = review.copy()
       word_freq = compute_word_count(new_review[WORDS_KEY])
       new_review[WORD_COUNT_KEY] = word_freq
       return new_review

def compute_word_count_dataset(dataset):
       if type(dataset) != list:
              raise Exception("Dataset must be a list")
       result = list(map(compute_word_count_review, dataset))
       return result

def tokenize(text):
       if type(text) != str:
              raise Exception("Text must be a string")
       text_lower = text.lower()
       text_clean = re.sub(r"[^\w]", " ",text_lower)
       wors = text_clean.split()
       return words

def tokenize_review(review):
       if type(review) != dict:
              raise Exception("Review must be a dictionary")
       new_review = review.copy()
       words = tokenize(new_review[TEXT_KEY])
       new_review[WORDS_KEY] = words
       return new_review

def tokenize_dataset(dataset):
       if type(dataset) != list:
              raise Exception("Dataset must be a list")
       result = list(map(tokenize_review, dataset))
       return result
