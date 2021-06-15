record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
records = []
username = {}
result = []
for rec in record:
    recs = list(rec.split())
    if recs[0] == 'Enter':
        username[recs[1]] = recs[2]
        records.append(recs)
    elif recs[0] == 'Change':
        username[recs[1]] = recs[2]
    else:
        records.append(recs)

for record in records:
    if record[0] == 'Enter':
        result.append(username[record[1]]+"님이 들어왔습니다.")
    else:
        result.append(username[record[1]] + "님이 나갔습니다.")
print(result)
