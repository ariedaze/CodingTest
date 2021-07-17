func solution(_ strings:[String], _ n:Int) -> [String] {
    
    let answer = strings.sorted(by: {
        //해당 단어의 인덱스를 다음 단어와 비교하고 만약 앞 요소의 인덱스 대입 해당 값이 작으면 True를 리턴해서 정렬
        if Array($0)[n] == Array($1)[n] {
            return $0 < $1
        }
        // 그냥 작으면 True리턴
        return Array($0)[n] < Array($1)[n]
    })
    
    return answer
}
