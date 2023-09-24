sentence = str(input('Введите предложение '))

def counter(x):
    words = x.split(' ')
    count_words = len(words)
    return count_words

def replacer(x):
    rep = x.replace(input('заменяемый символ '), '😎')
    return rep

print(counter(sentence))
print(replacer(sentence))