func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    
    var answer: [Int] = []
    
    for num in arr {
        if num % divisor == 0 {
            answer.append(num)
        }
    }
    
    if answer.count == 0 {
        return [-1]
    }
    
    answer.sort(by: <)
    
    return answer
}
