## start

import random
word_length = random.randint(5, 20);
random_word = "";
for _ in range(word_length):
    random_word += random.choice(['a', 'b', 'c']);
print("Random word:", random_word);

##End