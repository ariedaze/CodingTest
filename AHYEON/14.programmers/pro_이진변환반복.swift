import Foundation

func solution(_ s:String) -> [Int] {
    var s = s
    var cnt = 0
    var zeroCount = 0

    while s != "1" {
        cnt += 1
        let newS = s.filter{ $0 == "1"}
        zeroCount += s.count - newS.count
        s = String(newS.count, radix: 2)
    }
    return [cnt, zeroCount]
}