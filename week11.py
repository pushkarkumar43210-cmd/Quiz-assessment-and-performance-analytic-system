# =========================================
# WEEK 11: Exception Handling + Validation
# =========================================

import csv

# -------- Custom Exceptions --------
class InvalidInputError(Exception):
    pass

class DuplicateAttemptError(Exception):
    pass


# -------- Validators (validators.py logic) --------
class Validators:

    @staticmethod
    def validate_name(name):
        if not name.isalpha():
            raise InvalidInputError("Name must contain only letters")

    @staticmethod
    def validate_score(score, total):
        if score < 0 or score > total:
            raise InvalidInputError("Invalid score value")

    @staticmethod
    def check_duplicate(sid, attempted_ids):
        if sid in attempted_ids:
            raise DuplicateAttemptError("Student already attempted quiz")


# -------- Student --------
class Student:
    def __init__(self, sid, name, dept):
        Validators.validate_name(name)
        self.sid = sid
        self.name = name
        self.dept = dept

    def display(self):
        print(f"ID: {self.sid}, Name: {self.name}, Dept: {self.dept}")


# -------- Quiz --------
class Quiz:
    def __init__(self, qid, subject):
        self.qid = qid
        self.subject = subject
        self.questions = []

    def add_question(self, text, options, correct):
        self.questions.append({
            "text": text,
            "options": options,
            "correct": correct
        })


# -------- Result --------
class Result:
    def __init__(self, sid, score, total):
        Validators.validate_score(score, total)
        self.sid = sid
        self.score = score
        self.total = total
        self.percentage = (score / total) * 100
        self.status = "Pass" if self.percentage >= 40 else "Fail"

    def display(self):
        print(f"\nScore: {self.score}/{self.total}")
        print(f"Percentage: {self.percentage}%")
        print(f"Status: {self.status}")


# -------- CSV Loader (Error Handling) --------
def load_students_from_csv(filename):
    students = []
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                sid, name, dept = row
                students.append(Student(sid, name, dept))
    except FileNotFoundError:
        print("Error: CSV file not found")
    except ValueError:
        print("Error: Incorrect data format in CSV")
    return students


# =========================================
# 🔥 MAIN PROGRAM
# =========================================

attempted_students = set()

try:
    # Create student
    s1 = Student("S001", "Pushkar", "CSE")
    Validators.check_duplicate(s1.sid, attempted_students)
    attempted_students.add(s1.sid)

    s1.display()

    # Create quiz
    quiz = Quiz("Q1", "Python")
    quiz.add_question("2+2?", ["3", "4", "5"], "4")

    # Result
    result = Result("S001", 2, 2)
    result.display()

except InvalidInputError as e:
    print("Validation Error:", e)

except DuplicateAttemptError as e:
    print("Duplicate Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
