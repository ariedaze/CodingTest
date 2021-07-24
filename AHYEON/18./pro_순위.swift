import Foundation

func solution(_ n:Int, _ results:[[Int]]) -> Int {

    var graph: [[Int]] = Array(repeating: Array(repeating: 0, count: n+1), count: n+1)

    for r in results {
        graph[r[0]][r[1]] = 1
    }

    func floyWashall() {
        for i in 1...n { // i>j, k>i ==> k > i 순서가 중요!
            for j in 1...n {
                for k in 1...n {
                    if  graph[i][j] == 1 && graph[k][i] == 1 {
                        graph[k][j] = 1
                    }
                }
            }
        }
    }
    floyWashall()

    var answer: Int = 0

    for i in 1...n {
        var visit: Bool = true
        for j in 1...n {
            if i == j {
                continue
            }
            if graph[i][j] == 0 && graph[j][i] == 0 {
                visit = false
                break
            }
        }
        if visit {
            answer += 1
        }
    }


    return answer
}