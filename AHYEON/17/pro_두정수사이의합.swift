func solution(_ a:Int, _ b:Int) -> Int64 {
    var answer: Int = 0

    if a < b {
        for i in a...b {
            answer += i
        }
    }
    else {
        for i in b...a {
            answer += i
        }
    }

    return Int64(answer)
}