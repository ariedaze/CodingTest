import Foundation

func solution(_ n:Int) -> Int {
    
    let threeBinary : String = String(n, radix: 3)
    let flipThreeBinary : String = String(threeBinary.reversed())
    let answer = Int(flipThreeBinary, radix: 3)!
    
    return answer
}
