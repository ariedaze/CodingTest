
func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    let blank = "#"
    func isSameBlock(_ row: Int, _ col: Int) -> Bool {
        guard case let first = mat[row][col], first != blank else {
            return false
        }
        if mat[row][col + 1] == first && mat[row + 1][col] == first && mat[row + 1][col + 1] == first {
            return true
        } else {
            return false
        } }
    let bd = board.map { $0.map { String($0) } }
    var mat = [[String]](repeating: [String](repeating: "", count: m), count: n)
    for i in (0..<n) {
        for j in (0..<m) {
            mat[i][j] = bd[m - j - 1][i]
        }
    }
    while true {
        var position = [[Int]]()

        for row in (0 ..< n - 1) {
            for col in (0 ..< m - 1) {
                if isSameBlock(row, col) {
                    position.append([row, col])
                 }
            }
        }
        if position.count == 0 { break }
        for pos in position {
            mat[pos[0]][pos[1]] = blank
            mat[pos[0]][pos[1] + 1] = blank
            mat[pos[0] + 1][pos[1]] = blank
            mat[pos[0] + 1][pos[1] + 1] = blank
        }
        for i in (0..<mat.count) {
            mat[i].removeAll(where: { $0 == blank })
            mat[i] += [String](repeating: blank, count: m - mat[i].count)
        } }

    return mat.reduce(0) { $0 + $1.filter { $0 == blank }.count }
}


