from lib import *

# read dataset
dataset = read_json_file("reviews.json")
print(dataset[0])

# tokenize dataset
dataset_tokenized = tokenize_dataset(dataset)
# compute word count
dataset_word_count = compute_word_count_dataset(dataset_tokenized)