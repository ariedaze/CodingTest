func solution(_ strings:[String], _ n:Int) -> [String] {
    let answer: [String] = strings.sorted {
        let s1: Character = $0[$0.index($0.startIndex, offsetBy: n)]
        let s2: Character = $1[$1.index($1.startIndex, offsetBy: n)]

        if s1 == s2 {
            return $0 < $1
        } else {
            return s1 < s2
        }
    }

    return answer
}