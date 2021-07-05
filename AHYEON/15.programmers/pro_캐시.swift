import Foundation

func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    let cities = cities.map{ return $0.uppercased() }
    var caches: [String] = []
    var count = 0

    for city in cities {
        if caches.contains(city) {
            count += 1
            caches.remove(at: caches.firstIndex(of: city)!)
            caches.append(city)
        }
        else {
            count += 5
            caches.append(city)
            if caches.count > cacheSize {
                caches.removeFirst()
            }
        }
    }

    return count
}