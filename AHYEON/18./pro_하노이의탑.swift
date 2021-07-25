import Foundation

extension Array where Element == [Int] {
    mutating func hanoi(_ from: Int, _ by:Int, _ to:Int, _ n: Int) {
        if n == 1 {
            self.append([from,to])
            return
        }
        hanoi(from, to, by, n-1)
        hanoi(from, by, to, 1)
        hanoi(by, from, to ,n-1)
    }
}
func solution(_ n:Int) -> [[Int]] {
    var result: [[Int]] = []
    result.hanoi(1,2,3, n)
    return result
}
