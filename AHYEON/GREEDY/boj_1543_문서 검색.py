document = input()
word = input()

len_doc = len(document)
len_word = len(word)
pos = 0

cnt = 0
while pos + len_word <= len_doc:
    if word == document[pos:pos+len_word]:
        cnt += 1
        pos += len_word
    else:
        pos += 1

print(cnt)