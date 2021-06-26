import Foundation

let dirs_dict: [Character: (Int, Int)] = [
    "U": (1, 0),
    "D": (-1, 0),
    "R": (0, 1),
    "L": (0, -1)
]

func solution(_ dirs:String) -> Int {
    var x = 0, y = 0
    var visited: [[Int]] = []
    for d in dirs {
        if let (dx, dy) = dirs_dict[d] {
            let nx = x + dx
            let ny = y + dy

            if nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5 {
                if !visited.contains([x, nx, y, ny]) && !visited.contains([nx, x, ny, y]){
                    visited.append([x, nx, y, ny])
                    visited.append([nx, x, ny, y])
                }

                x = nx
                y = ny
            }
        }
    }

    return visited.count / 2
}