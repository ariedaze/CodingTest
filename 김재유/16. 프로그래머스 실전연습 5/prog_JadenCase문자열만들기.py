s = '3people unFollowed me'

words = s.split(' ')
new_words= []
for word in words:
    new_word = word.capitalize()
    new_words.append(new_word)
new_words = ' '.join(new_words)
print(new_words)
