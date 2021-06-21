def solution(infos, queries):
    user_data={
        "cpp":set(),
        "python":set(),
        "java":set(),
        "backend":set(),
        "frontend":set(),
        "junior":set(),
        "senior":set(),
        "chicken":set(),
        "pizza":set()
              }
    scores = []
    answer = []
    for idx, info in enumerate(infos):
        info = list(info.split())
        for data in info[:4]:
            user_data[data].add(idx)
        scores.append(int(info[4]))
    for query in queries:
        query = list(query.split())
        check = set()
        for idx, score in enumerate(scores):
            if score >= int(query[7]):
                  check.add(idx)
        for cut in query[:7]:
            if cut == "-" or cut == "and":
                pass
            else: 
                if cut == "cpp":
                    check -= user_data["python"]
                    check -= user_data["java"]
                    continue
                if cut == "python":
                    check -= user_data["cpp"]
                    check -= user_data["java"]
                    continue
                if cut == "java":
                    check -= user_data["cpp"]
                    check -= user_data["python"]
                    continue
                if cut == "backend":
                    check -= user_data["frontend"]
                    continue
                if cut == "frontend":
                    check -= user_data["backend"]
                    continue
                if cut == "junior":
                    check -= user_data["senior"]
                    continue
                if cut == "senior":
                    check -= user_data["junior"]
                    continue
                if cut == "pizza":
                    check -= user_data["chicken"]
                    continue
                if cut == "chicken":
                    check -= user_data["pizza"]
                    continue
        answer.append(len(check))
    return answer