import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var left: (Int, Int) = (3, 0)
    var right: (Int, Int) = (3, 2)
    var answer: String = ""

    let pos: [(Int, Int)] = [
        (3, 1), (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

    numbers.forEach {
        if $0 == 1 || $0 == 4 || $0 == 7 {
            left = pos[$0]
            answer += "L"
        }
        else if $0 == 3 || $0 == 6 || $0 == 9 {
            right = pos[$0]
            answer += "R"
        }
        else {
            let leftDist: Int = abs(left.0 - pos[$0].0) + abs(left.1 - pos[$0].1)
            let rightDist: Int = abs(right.0 - pos[$0].0) + abs(right.1 - pos[$0].1)
            if leftDist == rightDist {
                if hand == "right" {
                    answer += "R"
                    right = pos[$0]
                }
                else {
                    answer += "L"
                    left = pos[$0]
                }
            } else if leftDist > rightDist {
                answer += "R"
                right = pos[$0]
            } else {
                answer += "L"
                left = pos[$0]
            }
        }

    }

    return answer
}