import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var fail: Dictionary = [Int:Double]()
    var total: Int =  stages.count

    for i in 1...N {
        let n = stages.filter {$0 == i}.count
        fail[i] = Double(n) / Double(total)
        total -= n
    }
    //sorted는 정렬된 값을 리턴하기 떄문에 반드시 변수에 할당, sort는 원래 값을 정렬한다.
    let end = fail.sorted(by: <).sorted(by: {$0.value > $1.value})
    let result = end.map {$0.key}
    
    return result
}
