from collections import Counter

sentence = str(input('Введите предложение '))

def words_counter(x):
    words = x.split(' ')
    count_words = len(words)
    return count_words

def replacer(x):
    rep = x.replace(input('заменяемый символ '), '😎')
    return rep

def split(x):
    x = [char for char in x]
    return x

def same_symbols_couter(x):
    x = split(x)
    count = Counter(x)
    return count

print(words_counter(sentence))
print(replacer(sentence))
print(split(sentence))
print(sentence)
print(same_symbols_couter(sentence))