#print("STUDENT MANAGEMENT HERE =>")

class Student:
    def __init__(self, name, age, level, roll_no):
        self.name = name
        self.age = age
        self.level = level
        self.roll_no = roll_no
        self.marks = {}
        self.grade = ""
        self.total_score = 0
        self.average_score = 0
        self.gpa = 0.0

    def add_marks(self):
        subjects = ["english", "hindi", "kannada", "maths", "science", "ss"]
        for subject in subjects:
            while True:
                try:
                    mark = int(input(f"Enter the student's marks in {subject.title()}: "))
                    if 0 <= mark <= 100:
                        self.marks[subject] = mark
                        break
                    else:
                        print("Invalid input. Marks should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        return self.marks

    def get_total_marks(self):
        self.total_score = sum(self.marks.values())
        return self.total_score

    def get_average_score(self):
        self.average_score = self.get_total_marks() / len(self.marks)
        return self.average_score

    def get_grade(self):
        percentage = self.get_total_marks() / 600 * 100
        
        if percentage >= 90:
            self.grade = 'A+'
            self.gpa = 4.0
        elif percentage >= 80:
            self.grade = 'A'
            self.gpa = 3.7
        elif percentage >= 75:
            self.grade = 'B+'
            self.gpa = 3.3
        elif percentage >= 70:
            self.grade = 'B'
            self.gpa = 3.0
        elif percentage >= 65:
            self.grade = 'C+'
            self.gpa = 2.7
        elif percentage >= 60:
            self.grade = 'C'
            self.gpa = 2.3
        elif percentage >= 55:
            self.grade = 'D+'
            self.gpa = 2.0
        elif percentage >= 50:
            self.grade = 'D'
            self.gpa = 1.7
        else:
            self.grade = 'F'
            self.gpa = 0.0

        return self.grade

    def get_gpa(self):
        if self.grade == "":
            self.get_grade()
        return self.gpa
