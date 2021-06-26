import Foundation

func solution(_ board:[[Int]]) -> Int {
    var newBoard = board

    var answer = 0
    let rowCount = newBoard.count
    let colCount = newBoard[0].count
    var max = 0

    if rowCount < 2 || colCount < 2 {
        for y in 0..<rowCount {
            for x in 0..<colCount where newBoard[y][x] == 1 {
                max = 1
                break
            }
        }
    } else {
        for y in 1..<rowCount {
            for x in 1..<colCount where newBoard[y][x] == 1 {
                newBoard[y][x] = min(newBoard[y - 1][x], newBoard[y][x - 1], newBoard[y - 1][x - 1]) + 1
                if newBoard[y][x] > max {
                    max = newBoard[y][x]
                }
            }
        }
    }

    answer = Int(pow(CGFloat(max), 2))

    return answer
}