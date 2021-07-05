import Foundation

func solution(_ arr:[[Int]]) -> [Int] {

    var answer: [Int] = []

    func check(_ arr: [[Int]]) -> Bool {
        let firstNum: Int = arr[0][0]
        for a in arr {
            for num in a {
                if num != firstNum {
                    return false
                }
            }
        }
        answer.append(firstNum)
        return true
    }

    func compress(_ arr: [[Int]], _ size: Int) {
        var quads = [[[Int]]](repeating: [], count: 4)

        for i in 0..<size/2 {
            var temp1 = [Int]()
            var temp2 = [Int]()
            for one in 0..<size/2 {
                temp1.append(arr[i][one])
            }
            quads[0].append(temp1)
            for two in size/2..<size {
                temp2.append(arr[i][two])
            }
            quads[1].append(temp2)
        }

        for i in size/2..<size {
            var temp1 = [Int]()
            var temp2 = [Int]()
            for three in 0..<size/2 {
                temp1.append(arr[i][three])
            }
            quads[2].append(temp1)
            for four in size/2..<size {
                temp2.append(arr[i][four])
            }
            quads[3].append(temp2)
        }

        for quad in quads {
            if !check(quad) {
                if quad.filter({$0.count == 1}).count == 4 {
                    for i in 0...3 {
                        answer.append(quad[i].first!)
                    }
                }else{
                    compress(quad, size/2)
                }
            }
        }


    }


    if !check(arr) {
        if arr.filter({$0.count == 1}).count == 4 {
            for i in 0...3 {
                answer.append(arr[i].first!)
            }
        }else{
            compress(arr, arr.count)
        }
    }

    return [answer.filter({$0 == 0}).count,answer.filter({$0 == 1}).count]

}