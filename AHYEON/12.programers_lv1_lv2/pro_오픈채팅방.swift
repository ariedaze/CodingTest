import Foundation

func solution(_ record:[String]) -> [String] {
    var nickname: [String : String] = [:]
    var answer: [[String]] = []

    record.forEach {
        let status = $0.components(separatedBy: " ")

        switch status[0] {
            case "Leave":
                answer.append(contentsOf: [[status[1], "님이 나갔습니다."]])
            case "Enter":
                answer.append(contentsOf: [[status[1], "님이 들어왔습니다."]])
                nickname[status[1]] = status[2]
            default:
                nickname[status[1]] = status[2]
        }
    }

    return answer.map({ nickname[$0[0]]! + $0[1] })
}