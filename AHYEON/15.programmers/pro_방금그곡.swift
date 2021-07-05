func solution(_ m:String, _ musicinfos:[String]) -> String {

    let musicinfos = musicinfos.map {$0.components(separatedBy: ",")}

    let m = change(m)
    var res = [(String,Int)]()

    for info in musicinfos {

        let playtime = diff(info[0],info[1])
        let music = change(info[3])
        let title = info[2]

        let repeatcnt = playtime / music.count
        let sheet = repeatcnt == 0 ? music : String(repeating: music, count: repeatcnt + 1)

        if String(sheet.prefix(playtime)).contains(m) {
            res.append((title,playtime))
        }
    }


    return res.max {$0.1 < $1.1}?.0 ?? "(None)"
}


func diff(_ s: String, _ e: String) -> Int {
    var s = s.components(separatedBy: ":").map {Int($0)!}
    var e = e.components(separatedBy: ":").map {Int($0)!}

    return (e[0] * 60 + e[1]) - (s[0] * 60  + s[1])
}


func change(_ s: String) -> String{
    let s = s
    return s.replacingOccurrences(of:"C#", with:"c")
        .replacingOccurrences(of: "D#", with: "d")
        .replacingOccurrences(of: "F#", with: "f")
        .replacingOccurrences(of: "G#", with: "g")
        .replacingOccurrences(of: "A#", with: "a")
}

