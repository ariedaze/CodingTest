func solution(_ a:Int, _ b:Int) -> Int64 {
    var answer:Int64 = 0
    
    for i in a < b ? a...b : b...a {
        answer += Int64(i)
    }
    return answer
}
