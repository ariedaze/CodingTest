import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    let length: Int = absolutes.count
    var answer: Int = 0

    for i in 0..<length {
        if signs[i] {
            answer += absolutes[i]
        }
        else {
            answer -= absolutes[i]
        }
    }

    return answer
}