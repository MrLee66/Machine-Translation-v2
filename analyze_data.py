from collections import Counter

import nltk
from tqdm import tqdm

from config import *


def train_length_zh():
    print('train_length_zh')
    translation_path = os.path.join(train_translation_folder, train_translation_zh_filename)

    with open(translation_path, 'r') as f:
        data = f.readlines()

    max_len = 0
    lengthes = []
    print('scanning train data (zh)')
    for sentence in tqdm(data):
        length = len(sentence.strip().lower())
        lengthes.append(length)
        if length > max_len:
            max_len = length

    print('max_len: ' + str(max_len))

    counter_length = Counter(lengthes)

    total_count = len(data)
    common = counter_length.most_common()
    covered_count = 0
    for i in range(1, max_len + 1):
        count = [item[1] for item in common if item[0] == i]
        if count:
            covered_count += count[0]
        print('{} -> {}'.format(i, covered_count / total_count))


def train_length_en():
    print('train_length_en')
    translation_path = os.path.join(train_translation_folder, train_translation_en_filename)
    with open(translation_path, 'r') as f:
        data = f.readlines()

    max_len = 0
    lengthes = []
    print('scanning train data (en)')
    for sentence in tqdm(data):
        tokens = nltk.word_tokenize(sentence.strip().lower())
        length = len(tokens)
        lengthes.append(length)
        if length > max_len:
            max_len = length

    print('max_len: ' + str(max_len))

    counter_length = Counter(lengthes)
    total_count = len(data)
    common = counter_length.most_common()
    covered_count = 0
    for i in range(1, max_len + 1):
        count = [item[1] for item in common if item[0] == i]
        if count:
            covered_count += count[0]
        print('{} -> {}'.format(i, covered_count / total_count))


if __name__ == '__main__':
    train_length_zh()
    train_length_en()
