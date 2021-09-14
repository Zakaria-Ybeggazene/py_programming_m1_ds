import re
from collections import Counter

file_path = "ipsum.txt"
num_lines = 0
num_characters = 0
num_words = 0
word_counts = Counter()
longest_word = ""
len_longest_word = 0
character_counts = Counter()
try:
    with open(file_path, 'r') as infile:
        for line in infile:
            num_lines += 1
            num_characters += len(line)
            line_words = re.findall(r'\w+', line)
            if line_words == []:
                continue
            num_words += len(line_words)
            cap_words = [word.upper() for word in line_words]
            word_counts = word_counts + Counter(cap_words)
            max_len = len(max(line_words, key=len))
            if len_longest_word < max_len:
                len_longest_word = max_len
                longest_word = [word for word in line_words if len(word)==max_len][0]
            characters = ''.join(line_words)
            character_counts = character_counts + Counter(characters)
        print("Stats for file {}".format(file_path))
        print("# of lines : {}".format(num_lines))
        print("# of characters : {}".format(num_characters))
        print("# of words : {}".format(num_words))
        print("Most frequent word : {} with {} occurrences".format(word_counts.most_common(1)[0][0], word_counts.most_common(1)[0][1]))
        print("Longest word : {}".format(longest_word))
        print("Mean of # of words per line : {}".format(num_words/num_lines))
        print("Most frequent letter : {} with {} occurrences".format(character_counts.most_common(1)[0][0], character_counts.most_common(1)[0][1]))
except IOError as error:
        print("cut: {}: No such file or directory".format(file_path))