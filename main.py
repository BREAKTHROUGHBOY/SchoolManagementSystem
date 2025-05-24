from school_manager import School

school_team = School()


def join_student():
    print("\n=== ADDING NEW STUDENT ===")
    name = input("ENTER STUDENT NAME: ").strip()

    while True:
        try:
            age = int(input("ENTER STUDENT AGE: "))
            if 5 <= age <= 100:
                break
            else:
                print("⚠️ AGE MUST BE BETWEEN 5 AND 100.")
        except ValueError:
            print("⚠️ INVALID INPUT. PLEASE ENTER A NUMBER.")

    level = input("ENTER STUDY LEVEL (e.g. Grade 10, Class B): ").strip()
    roll_no = input("ENTER STUDENT ROLL NUMBER / ID: ").strip()

    school_team.add_student(name, age, level, roll_no)


def main():
    print('---------------------------------------')
    print("🎓 SMART STUDENT MANAGEMENT SYSTEM")
    print("🔍 RANKING + PERFORMANCE ANALYSIS ENGINE")
    print('---------------------------------------')

    while True:
        print("\n____________________________________")
        print("1. ADD STUDENT")
        print("2. REMOVE STUDENT")
        print("3. UPDATE STUDENT MARKS")
        print("4. VIEW STUDENT RANKINGS")
        print("5. GENERATE REPORT CARD")
        print("6. CLASS ANALYSIS")
        print("7. SPECIFIC STUDENT DATA")
        print("8. QUIT")
        print("____________________________________")

        choice = input("📌 ENTER YOUR CHOICE (1-8): ").strip()

        if choice == '1':
            join_student()

        elif choice == '2':
            name = input("ENTER STUDENT NAME TO REMOVE: ").strip()
            school_team.remove_student(name)

        elif choice == '3':
            name = input("ENTER STUDENT NAME TO UPDATE MARKS: ").strip()
            school_team.upd_marks(name)

        elif choice == '4':
            school_team.rank_students()

        elif choice == '5':
            name = input("ENTER STUDENT NAME FOR REPORT CARD: ").strip()
            school_team.generate_report_card(name)

        elif choice == '6':
            school_team.generate_class_analysis()

        elif choice == '7':
            school_team.allow_access()

        elif choice == '8':
            print("\n👋 EXITING... THANK YOU FOR USING THE SYSTEM!")
            break

        else:
            print("❌ INVALID CHOICE. PLEASE SELECT A VALID OPTION.")


if __name__ == '__main__':
    main()
