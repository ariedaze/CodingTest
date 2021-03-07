import sys; sys.stdin = open('input_data/1541.txt')

text = input()
text_apart = text.split('-')
result = 0
for idx, part in enumerate(text_apart):
    part = list(map(int, part.split('+')))
    if idx == 0:
        result += sum(part)
    else:
        result -= sum(part)
print(result)