import sys; sys.stdin = open('input_data/1543.txt')

sentence = input()
word = input()
sentence_length = len(sentence)
word_length = len(word)
result = 0
now = 0
while now <= sentence_length-word_length:
    if sentence[now:now+word_length] == word:
        result += 1
        now += word_length
    else:
        now += 1
print(result)