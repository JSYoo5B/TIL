import Foundation

class Student: Comparable {
    static func < (lhs: Student, rhs: Student) -> Bool {
        if lhs.koreanScore != rhs.koreanScore {
            return lhs.koreanScore > rhs.koreanScore
        }
        else {
            if lhs.englishScore != rhs.englishScore {
                return lhs.englishScore < rhs.englishScore
            }
            else {
                if lhs.mathScore != rhs.mathScore {
                    return lhs.mathScore > rhs.mathScore
                }
                else {
                    return lhs.name < rhs.name
                }
            }
        }
    }

    static func == (lhs: Student, rhs: Student) -> Bool {
        return lhs.name == rhs.name && lhs.koreanScore == rhs.koreanScore && lhs.mathScore == rhs.mathScore && lhs.englishScore == rhs.englishScore
    }

    let name: String
    let koreanScore: Int
    let englishScore: Int
    let mathScore: Int

    init(name: String, koreanScore: Int, englishScore: Int, mathScore: Int) {
        self.name = name
        self.koreanScore = koreanScore
        self.mathScore = mathScore
        self.englishScore = englishScore
    }
}

var numberOfStudents: Int = 0
var students: [Student] = []

func input() {
    if let stringTemp: String = readLine(), let intTemp: Int = Int(stringTemp) {
        numberOfStudents = intTemp
    }

    for _ in 0..<numberOfStudents {
        if let studentInfo: [String] = readLine()?.split(separator: " ").compactMap({ String($0) }) {
            let scores: [Int] = studentInfo[1...].compactMap({ Int($0) })
            students.append(Student(name: studentInfo[0], koreanScore: scores[0], englishScore: scores[1], mathScore: scores[2]))
        }
    }
}

func sortAndPrintStudents() {
    students.sort()

    let output = students.reduce(into: "") { (result: inout String, student: Student)->Void in
        result += student.name + "\n"
    }

    print(output)
}

input()
sortAndPrintStudents()
