import Foundation

let numberDict: [String: String] = [
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10"
]

func solution(_ s:String) -> Int {
    var answer: String = ""
    var part: String = ""
    for string in s {
        if let num = Int(String(string)) {
            answer += String(string)
            continue
        } else {
            part += String(string)
        }
        if let numString = numberDict[part] {
            answer += numString
            part = ""
        }

    }

    if let numAnswer = Int(answer) {
        return numAnswer
    }
    return 1
}