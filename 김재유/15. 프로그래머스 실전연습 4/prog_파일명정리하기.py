def solution(files):
    formatted_file = []
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                start = i
                for j in range(i+1, len(file)):
                    if not file[j].isdigit():
                        end = j
                        tail = file[end:]
                        break
                else:
                    end = len(file)
                    tail = ""
                break
        head = file[:start]
        number = file[start:end]
        formatted_file.append([head, number, tail])
    sorts = sorted(formatted_file, key= lambda x : (x[0].lower(), int(x[1])))
    print(head.lower())
    result = []
    for sort in sorts:
        result.append(sort[0]+sort[1]+sort[2])
    return result