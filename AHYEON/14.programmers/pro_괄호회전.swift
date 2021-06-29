import Foundation

func solution(_ s:String) -> Int {
    var answer = 0
    var arr = Array(s)

    for _ in 0..<arr.count {
        let str = String(arr)
        if check(str) {
            answer += 1
        }
        arr.append(arr.removeFirst())
    }

    return answer
}

func check(_ s:String) -> Bool {
    var stack = [Character]()

    for c in s {
        switch c {
            case "(", "[", "{": stack.append(c)
            case ")":
            if stack.isEmpty { return false }
            if stack.last == "(" {
                stack.removeLast()
            }
            case "]":
            if stack.isEmpty { return false }
            if stack.last == "[" {
                stack.removeLast()
            }
            case "}":
            if stack.isEmpty { return false }
            if stack.last == "{" {
                stack.removeLast()
            }
            default: break
        }
    }

    return stack.isEmpty ? true: false
}