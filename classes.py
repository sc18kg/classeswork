class Student:

    def __init__(self, name, age, bclass):
        self.name = name
        self.age = age
        self.bclass = bclass

farn = Student("Farnaaz", 20 , "Student")


def final_grade(gradea, gradeb, gradec):
    average_gradea = (gradea / 25) * 100
    average_gradeb = (gradeb / 50) * 100
    average_gradec = (gradec / 100) * 100

    return ((average_gradea * 0.25) +  (average_gradeb * 0.5) +  average_gradec) / 1.75

gradea = int(input("Please enter your Homework Grade: "))
gradeb = int(input("Please enter your Assesment Grade: "))
gradec = int(input("Please enter your Final Exam Grade: "))

average_grade = str(final_grade(gradea, gradeb, gradec))

print(f"{farn.name},{farn.age} has an average score of {average_grade}")