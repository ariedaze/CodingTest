import Foundation


func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var check: Int = 0
    var unknown: Int = 0

    for lotto in lottos {
        if win_nums.contains(lotto) {
            check += 1
        }
        else if lotto == 0 {
            unknown += 1
        }
    }
    func getRank(_ num: Int) -> Int {
        switch num {
            case 6: return 1
            case 5: return 2
            case 4: return 3
            case 3: return 4
            case 2: return 5
            default: return 6
        }
    }

    return [getRank(check+unknown), getRank(check)]
}

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {

    let zeroCount = lottos.filter { $0 == 0}.count
    let winCount: Int = win_nums.filter { lottos.contains($0) }.count

    return [min(7-winCount-zeroCount,6), min(7-winCount,6)]
}