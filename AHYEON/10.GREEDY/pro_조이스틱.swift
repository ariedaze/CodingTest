import Foundation
func solution(_ name:String) -> Int {
    var ans = 0
    let name = name.map({$0})

    // up down 계산
    for i in 0..<name.count {
        if name[i] != "A" && name[i] < "N" {
            ans += Int(name[i].asciiValue! - 65)
        } else if name[i] >= "N" {
            ans += Int(91 - name[i].asciiValue!)
        }
    }

    // left right 계산
    var minMove = name.count-1
    for i in 0..<name.count {
        if name[i] != "A" {
            var next = i + 1
            while next < name.count && name[next] == "A" {
                next += 1
            }
            let move = 2 *  i + name.count - next
            minMove = min(move, minMove)
        }
    }
    return ans + minMove
}

