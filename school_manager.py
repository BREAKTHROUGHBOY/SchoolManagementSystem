from student_manager import Student


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, level, roll_no):
        new_student = Student(name, age, level, roll_no)
        self.students.append(new_student)
        print(f"\nSTUDENT {name} ADDED TO SCHOOL SUCCESSFULLY!\n")

        new_student.add_marks()
        print(" > MARKS ADDED!")

        new_student.get_grade()
        print(" > GRADES CALCULATED")

        new_student.get_average_score()
        print(" > AVERAGE SCORE CALCULATED")

        new_student.get_gpa()
        print(" > GPA CALCULATED")

        print("ADMISSION COMPLETED WITH QUALIFICATIONS!\n")

    def remove_student(self, name):
        if not self.students:
            print(f"\nTHERE ARE NO STUDENTS IN THE SCHOOL!")
            return

        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"\nSTUDENT {name} REMOVED SUCCESSFULLY!\n")
                return

        print(f"\nNO STUDENT NAMED {name} FOUND!\n")

    def upd_marks(self, name):
        if not self.students:
            print("\nTHERE ARE NO STUDENTS TO UPDATE!")
            return

        for student in self.students:
            if student.name == name:
                student.marks = student.add_marks()
                print("MARKS UPDATED SUCCESSFULLY!\n")
                return

        print(f"\nNO STUDENT NAMED {name} FOUND!\n")

    def rank_students(self):
        if not self.students:
            print("NO STUDENTS TO RANK!\n")
            return

        sorted_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
        print("\n=== STUDENT RANKINGS BY TOTAL SCORE ===")
        for i, student in enumerate(sorted_students, start=1):
            print(f"{i}. {student.name} - {student.total_score} marks")
        print()

    def generate_report_card(self, name):
        if not self.students:
            print("\nNO STUDENTS AVAILABLE!")
            return

        for student in self.students:
            if student.name == name:
                print(f"""
-------------------------------------------------------------
                REPORT CARD OF {name}
-------------------------------------------------------------
Name           : {student.name}
Age            : {student.age}
Class Level    : {student.level}
Roll No        : {student.roll_no}
Grade          : {student.get_grade()}
Total Score    : {student.get_total_marks()}
Average Score  : {student.get_average_score()}
GPA            : {student.get_gpa()}
-------------------------------------------------------------
                """)
                return

        print(f"\nNO STUDENT NAMED {name} FOUND!\n")

    def generate_class_analysis(self):
        if not self.students:
            print("\nNO STUDENTS AVAILABLE!")
            return

        while True:
            class_level = input("\nENTER THE CLASS LEVEL FOR ANALYSIS (q to quit): ").strip()
            if class_level.lower() == 'q':
                print("EXITING CLASS ANALYSIS...\n")
                break

            same_class = [s for s in self.students if s.level == class_level]
            if same_class:
                print(f"\n=== ANALYSIS FOR CLASS {class_level} ===")
                for student in same_class:
                    print(f"{student.name} - Total Score: {student.total_score}")
                print()
            else:
                print(f"\nNO STUDENTS FOUND IN CLASS {class_level}. TRY AGAIN!\n")

    def specific_programs(self, program, name):
        target_student = next((s for s in self.students if s.name == name), None)
        if not target_student:
            print(f"SORRY, NO STUDENT NAMED {name} FOUND!\n")
            return

        program = program.lower()
        if program == "total_score":
            print(f"{name}'s TOTAL SCORE: {target_student.get_total_marks()}")
        elif program == "average_score":
            print(f"{name}'s AVERAGE SCORE: {target_student.get_average_score()}")
        elif program == "grade":
            print(f"{name}'s GRADE: {target_student.get_grade()}")
        elif program == "gpa":
            print(f"{name}'s GPA: {target_student.get_gpa()}")
        else:
            print(f"SORRY, NO PROGRAM NAMED '{program}' FOUND!")

    def allow_access(self):
        print("\n=== ACCESS SPECIFIC PROGRAMS ===")
        print("1. Get Total Score")
        print("2. Get Grade")
        print("3. Get Average Score")
        print("4. Get GPA")

        name = input("\nENTER STUDENT NAME: ").strip()
        choice = input("ENTER YOUR CHOICE (1/2/3/4): ").strip()

        options = {
            '1': "total_score",
            '2': "grade",
            '3': "average_score",
            '4': "gpa"
        }

        program = options.get(choice)
        if program:
            self.specific_programs(program, name)
        else:
            print("INVALID CHOICE!\n")
