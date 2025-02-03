import json

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, name, age, grade):
        student = {"name": name, "age": age, "grade": grade}
        self.students.append(student)
        self.save_students()
        print(f"Student {name} added successfully!")

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for index, student in enumerate(self.students, start=1):
                print(f"{index}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

    def search_student(self, name):
        results = [s for s in self.students if s["name"].lower() == name.lower()]
        if results:
            for student in results:
                print(f"Found - Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        else:
            print("Student not found.")

    def update_student(self, name, new_age=None, new_grade=None):
        for student in self.students:
            if student["name"].lower() == name.lower():
                if new_age:
                    student["age"] = new_age
                if new_grade:
                    student["grade"] = new_grade
                self.save_students()
                print(f"Student {name} updated successfully!")
                return
        print("Student not found.")

    def delete_student(self, name):
        self.students = [s for s in self.students if s["name"].lower() != name.lower()]
        self.save_students()
        print(f"Student {name} deleted successfully!")

if __name__ == "__main__":
    system = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            system.add_student(name, age, grade)
        elif choice == "2":
            system.display_students()
        elif choice == "3":
            name = input("Enter name to search: ")
            system.search_student(name)
        elif choice == "4":
            name = input("Enter name to update: ")
            new_age = input("Enter new age (leave blank to keep current): ") or None
            new_grade = input("Enter new grade (leave blank to keep current): ") or None
            system.update_student(name, new_age, new_grade)
        elif choice == "5":
            name = input("Enter name to delete: ")
            system.delete_student(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
