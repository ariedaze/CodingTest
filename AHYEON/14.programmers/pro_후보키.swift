import Foundation


var numArr: [[Int]] = []

func solution(_ relation:[[String]]) -> Int {
    let column = relation[0].count
    for i in 0..<column {
        combination(i, column, [])
    }

    numArr.sort{ $0.count < $1.count}
    // print(numArr)
    return 0
}


func combination(_ beginAt: Int, _ depth: Int, _ arr: [Int]) {
    if beginAt == depth {
        return numArr.append(arr)
    } else {
        var arr = arr
        for i in beginAt..<depth {
            arr.append(beginAt)
            combination(i+1, depth, arr)
            arr.removeLast()
        }
    }
}