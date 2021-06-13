import Foundation


func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    var answer:[Int] = []
    var rectangle:[[Int]] = makeRectangle(rows: rows, columns: columns)
    var newRectangle:[[Int]] = rectangle
    for q in queries {
        var borderNumbers:[Int] = []
        changeBorderColumns(start: (q[1]-1,q[0]-1), end: (q[3]-1,q[2]-1), newRectangle: &newRectangle,rectangle:&rectangle, answer: &answer,borderNumbers: &borderNumbers)
        changeBorderRows(start: (q[1]-1,q[0]-1), end: (q[3]-1,q[2]-1), newRectangle: &newRectangle,rectangle:&rectangle, answer: &answer,borderNumbers: &borderNumbers)
        rectangle = newRectangle
        answer.append(borderNumbers.min() ?? 0)
    }
    return answer
}

func makeRectangle(rows:Int,columns:Int) -> [[Int]]{
    var rectangle:[[Int]] = []
    for row in 0..<rows {
        let col =  (1+(columns*row)...(columns*(row+1))).map{$0}
        rectangle.append(col)
    }
    return rectangle
}

func changeBorderColumns(start:(Int,Int),end:(Int,Int),newRectangle:inout [[Int]],rectangle:inout [[Int]],answer:inout [Int],borderNumbers:inout [Int]) {
    let topCol = Array(newRectangle[start.1][start.0...end.0])
    borderNumbers.append(contentsOf: topCol)
    var newTopCol:[Int] = topCol
    for i in 0..<topCol.count-1{
        newTopCol[i+1] = topCol[i]
    }
    newTopCol[0] = rectangle[start.1+1][start.0]
    newRectangle[start.1][start.0...end.0] = ArraySlice(newTopCol)
    let bottomCol = Array(newRectangle[end.1][start.0...end.0])
    borderNumbers.append(contentsOf: bottomCol)
    var newBottomCol:[Int] = bottomCol
    for i in 1...bottomCol.count-1{
        newBottomCol[i-1] = bottomCol[i]
    }
    newBottomCol[bottomCol.count-1] = rectangle[end.1-1][end.0]
    newRectangle[end.1][start.0...end.0] = ArraySlice(newBottomCol)
}

func changeBorderRows(start:(Int,Int),end:(Int,Int),newRectangle:inout [[Int]],rectangle:inout [[Int]],answer:inout [Int],borderNumbers:inout [Int]) {
    if abs(end.1 - start.1) <= 1 { return }
    for i in start.1+1...end.1-1 {
        borderNumbers.append(newRectangle[i][start.0])
        borderNumbers.append(newRectangle[i][end.0])
        newRectangle[i][start.0] = rectangle[i+1][start.0]
        newRectangle[i][end.0] = rectangle[i-1][end.0]
    }
}
