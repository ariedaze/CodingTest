s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = s.replace("{", ",").replace("}", ",").split(",")
s = [ in_s for in_s in s if in_s]
set_s = set(s)
result = [0] * len(set_s)
for num in set_s:
    result[s.count(num)-1] = int(num)
print(result[::-1])
