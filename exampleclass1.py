class Student:

    def __init__(self, name, age, class_="Student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_score(self, testscores):
        return sum(testscores) / len(testscores)

jill = Student("Jill", 42)
print(jill.name, (jill.average_score([43,70,50])))