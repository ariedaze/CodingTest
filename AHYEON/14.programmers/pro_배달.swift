import Foundation

func solution(_ N:Int, _ road:[[Int]], _ k:Int) -> Int {
    var answer = 0

    var cost: [[Int]] = []
    var arr: [Int] = []

    // 초기화
    for _ in 0...N{
        arr.append(999999999)
    }

    for i in 0...N{
        cost.append(arr)
        cost[i][i] = 0
    }

    for i in 0..<road.count{
        if cost[road[i][0]][road[i][1]] > road[i][2]{
            cost[road[i][0]][road[i][1]] = road[i][2]
            cost[road[i][1]][road[i][0]] = road[i][2]
        }
    }
    for k in 1...N{
        for i in 1...N{
            for j in 1...N{
                if cost[i][k] + cost[k][j] < cost[i][j]{
                    cost[i][j] = cost[i][k] + cost[k][j]
                }
            }
        }
    }

    for i in 1...N{
        if cost[1][i] <= k{
            answer += 1
        }
    }

    return answer
}