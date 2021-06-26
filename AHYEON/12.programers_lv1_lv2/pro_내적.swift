import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    let length: Int = a.count
    var answer: Int = 0

    for i in 0..<length {
        answer += a[i]*b[i]
    }

    return answer
}