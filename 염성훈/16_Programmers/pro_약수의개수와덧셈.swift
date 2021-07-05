
import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var answer = 0
    
    for number in left..<right+1 {
        var count = 0
        for i in 1..<number{
            if number % i == 0 {
                count+=1
            }
        }
        
        if count % 2 == 0 {
            answer -= number
        } else {
            answer += number
        }
        
    }
    
    return answer
}
