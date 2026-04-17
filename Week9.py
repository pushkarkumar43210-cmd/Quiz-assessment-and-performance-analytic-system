# ================================
# WEEK 9: Multi-Module (Single File Version)
# ================================

# -------- Student Module --------
class Student:
    def __init__(self, sid, name, dept):
        self.sid = sid
        self.name = name
        self.dept = dept

    def display(self):
        print(f"ID: {self.sid}, Name: {self.name}, Dept: {self.dept}")


# -------- Quiz Module --------
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

    def display(self):
        print("\n--- Quiz ---")
        for i, q in enumerate(self.questions, 1):
            print(f"\nQ{i}: {q['text']}")
            for opt in q["options"]:
                print("-", opt)


# -------- Result Module --------
class Result:
    def __init__(self, sid, score, total):
        self.sid = sid
        self.score = score
        self.total = total
        self.percentage = (score / total) * 100
        self.status = "Pass" if self.percentage >= 40 else "Fail"

    def display(self):
        print("\n--- Result ---")
        print(f"Score: {self.score}/{self.total}")
        print(f"Percentage: {self.percentage}%")
        print(f"Status: {self.status}")


# -------- Analytics Module --------
class Analytics:
    def __init__(self, results):
        self.results = results

    def average_score(self):
        total = sum(r.score for r in self.results)
        return total / len(self.results)

    def pass_count(self):
        return sum(1 for r in self.results if r.status == "Pass")

    def show_report(self):
        print("\n--- Analytics Report ---")
        print("Average Score:", self.average_score())
        print("Students Passed:", self.pass_count())


# ================================
# 🔥 MAIN PROGRAM
# ================================

# Create student
s1 = Student("S001", "Pushkar", "CSE")
s1.display()

# Create quiz
quiz = Quiz("Q1", "Python")

quiz.add_question("Python is?", ["Language", "Snake", "Car"], "Language")
quiz.add_question("2 + 2?", ["3", "4", "5"], "4")

quiz.display()

# Create results
r1 = Result("S001", 2, 2)
r2 = Result("S002", 1, 2)

r1.display()
r2.display()

# Analytics
analysis = Analytics([r1, r2])
analysis.show_report()
