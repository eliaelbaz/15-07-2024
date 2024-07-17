## start

import random
list_length = random.randint(10, 20);
random_words = [];
for _ in range(list_length):
    word_length = random.randint(5, 20);
    random_word = "";
    for _ in range(word_length):
        random_word += random.choice(['a', 'b', 'c']);
    random_words.append(random_word);
print("Random words list:", random_words);

## End