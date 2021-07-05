import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    let sA = A.sorted { $0 < $1 }
    let sB = B.sorted { $0 > $1 }
    var answer: Int = 0

    for i in 0..<sA.count {
        answer += sA[i] * sB[i]
    }

    return answer
}

