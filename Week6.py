class Student:
    def __init__(self, sid, name, dept):
        self.sid = sid
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.sid}: {self.name} ({self.dept})"


class Quiz:
    def __init__(self, qid, subject):
        self.qid = qid
        self.subject = subject
        self.questions = []

    def add_question(self, qtext, options, correct):
        self.questions.append({
            "text": qtext,
            "options": options,
            "correct": correct
        })


class Result:
    def __init__(self, sid, qid, score, percentage, status):
        self.sid = sid
        self.qid = qid
        self.score = score
        self.percentage = percentage
        self.status = status


# 🔥 MAIN EXECUTION CODE
# Create student
s1 = Student(101, "Pushkar", "CSE")
print("Student:", s1)

# Create quiz
quiz = Quiz(1, "Python")

# Add questions
quiz.add_question("What is Python?", ["Language", "Snake", "Car"], "Language")
quiz.add_question("2 + 2 = ?", ["3", "4", "5"], "4")

print("\nQuiz Questions:")
for q in quiz.questions:
    print(q["text"], "->", q["options"])

# Create result
result = Result(101, 1, 2, 100, "Pass")

print("\nResult:")
print("Score:", result.score)
print("Percentage:", result.percentage)
print("Status:", result.status)
