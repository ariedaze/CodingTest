import Foundation

func solution(_ n:Int) -> Int
{
    var answer:Int = n + 1

    let oneCount = String(n, radix: 2).filter { $0 == "1"}.count

    while true {
        if oneCount == String(answer, radix: 2).filter{$0 == "1"}.count {
            break
        }
        answer += 1
    }

    return answer
}