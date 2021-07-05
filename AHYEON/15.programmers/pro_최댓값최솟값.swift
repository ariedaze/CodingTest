func solution(_ s:String) -> String {
    let sArray: [Int] = s.components(separatedBy: " ").map { Int($0)! }

    let minNum: Int = sArray.min()!
    let maxNum: Int = sArray.max()!

    return "\(minNum) \(maxNum)"
}