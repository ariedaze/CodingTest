func solution(_ s:String) -> String {
    let middle: Int = s.count/2

    if s.count % 2 == 0 {
        return String(Array(s)[middle-1...middle])
    }
    return String(Array(s)[middle])
}