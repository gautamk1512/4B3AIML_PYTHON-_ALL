# Question:
# A program that simulates a school management system, with classes for the students, the teachers, and the courses.

# Explanation:
# - `Student` class: Stores student name and ID.
# - `Teacher` class: Stores teacher name and subject.
# - `Course` class: Links a teacher and a list of students to a subject.

# Code Breakdown:
# 1. Define `Student` class to hold student info.
# 2. Define `Teacher` class to hold teacher info.
# 3. Define `Course` class.
#    - `__init__`: Sets course name, assigns a teacher, initializes empty student list.
#    - `add_student`: Appends a Student object to the list.
#    - `show_details`: Prints course name, teacher name, and list of enrolled students.
# 4. Create objects for Teacher (`t1`) and Students (`s1`, `s2`).
# 5. Create a Course object (`math_course`) assigned to `t1`.
# 6. Add students to the course.
# 7. Display course details.

class Student:
    # 1. Student Info
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Teacher:
    # 2. Teacher Info
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Course:
    # 3. Course Management
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.course_name}.")

    def show_details(self):
        print(f"Course: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")
        # List comprehension to get names from student objects
        print("Students:", ", ".join([s.name for s in self.students]))

# 4. Create People
t1 = Teacher("Mr. Smith", "Math")
s1 = Student("Alice", "S01")
s2 = Student("Bob", "S02")

# 5. Create Course
math_course = Course("Mathematics 101", t1)

# 6. Add Students
math_course.add_student(s1)
math_course.add_student(s2)

# 7. Show Info
math_course.show_details()
