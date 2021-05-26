import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var result = ""
    var stack: String = ""
    var k = k

    number.forEach { num in
        while true {
            guard let peek = stack.last, Int(String(peek))! < Int(String(num))! else { break }
            if k == 0 { break }
            k -= 1
            stack.removeLast()
        }
        stack.append(num)
    }

    result = stack

    if k > 0  {
        result = String(stack.dropLast(k))
    }

    return result
}



