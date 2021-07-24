import Foundation

func solution(_ n:Int) -> Int {
    var n = n
    var ternary: [Int] = []
    while n > 0 {
        ternary.append(n%3)
        n /= 3
    }

    var digit: Int = 1
    var answer: Int = 0
    var count: Int = ternary.count

    for i in 0..<count {
        answer += ternary[count-1-i]*digit
        digit *= 3
    }
    return answer
}