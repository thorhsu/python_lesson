class student:    
    x = 0
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []

    def add(self, grade):
        self.grades.append(grade)

    def avg(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return None
    def fcount(self):
        notQualifiedNum = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                if grade < 60:
                    notQualifiedNum += 1

            return notQualifiedNum
        else:
            return None
        
    
def top(students):
    highestScore = 0
    bestStudent = None
    for student in students:
        avg_score = student.avg()
        if avg_score > highestScore:
            highestScore = avg_score
            bestStudent = student

    return bestStudent

tom = student("Tom", "male")
tom.add(50)
tom.add(70)
tom.add(90)
print("avg is %*.2f"%(tom.avg()))
print(tom.fcount())
        
mary = student("Mary", "female")
mary.add(59)
mary.add(90)
mary.add(100)
print(mary.avg())
print(mary.fcount())

jessica = student("Jessica", "female")
jessica.add(30)
jessica.add(40)
jessica.add(60)
print(jessica.avg())
print(jessica.fcount())

students = [tom, mary, jessica]
top_student = top(students)
print("Best student is", top_student.name, " average score is", top_student.avg())
