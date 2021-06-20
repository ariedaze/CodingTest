import Foundation

func solution(_ s:String) -> Int{
    var str = s.map { String($0) } // string > 배얄로
    var result = [String]()
    var idx = 0

    if str.count % 2 != 0 { return 0 }
    result.append(str.removeFirst())

    while idx < str.count {
        let next = str[idx]
        guard let last = result.last else { result.append(next); idx += 1; continue }

        if last == next {
            result.removeLast()
        } else {
            result.append(next)
        }
        idx += 1
    }
    return result.count == 0 ? 1 : 0
}