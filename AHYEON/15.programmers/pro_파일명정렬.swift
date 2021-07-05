func solution(_ files:[String]) -> [String] {
    var fileList = [File]()
    for file in files {
        fileList.append(File(text: file))
    }
    fileList.sort { (f1, f2) -> Bool in
        if f1.head == f2.head {
            let n1 = Int(f1.number)!
            let n2 = Int(f2.number)!
            return n1 == n2 ? false : n1 < n2
        } else {
            return f1.head < f2.head
        }
    }
    return fileList.map { $0.text }
}

struct File {
    var text: String
    var head: String = ""
    var number: String = ""
    var tail: String = ""

    init(text: String) {
        self.text = text
        self.parseFile(text)
    }

    mutating func parseFile(_ file: String) {
        // 0: head, 1: number, 2: tail
        var current = 0

        for char in file.lowercased() {
            if current == 0 {
                if let _ = Int(String(char)) {
                    number.append(char)
                    current += 1
                } else {
                    head.append(char)
                }
            } else if current == 1 {
                if let _ = Int(String(char)) {
                    number.append(char)
                } else {
                    tail.append(char)
                    current += 1
                }
            } else {
                tail.append(char)
            }
        }
    }
}


extension String{
    var numeric: ClosedRange<Character> { return "0"..."9" }
    var head: String{
        return self.prefix { numeric.contains($0) == false }.uppercased()
    }
    var number: Int {
        return Int( self.drop   { numeric.contains($0) == false}
                        .prefix { numeric.contains($0) == true })!
    }
}

func solution2(_ files:[String]) -> [String] {

    return files.enumerated().sorted { (lhs, rhs) in
        let l = lhs.element
        let r = rhs.element
        if l.head != r.head { return l.head < r.head}
        if l.number != r.number { return l.number < r.number}
        return lhs.offset < rhs.offset

    }.map{ $0.element }
}
