import random
import datetime

# ---------------- USER PERSONALITY TYPES ----------------
PERSONALITY_TYPES = {
    "1": "Consistent Learner",
    "2": "Last-Minute Crammer",
    "3": "Balanced Learner",
    "4": "Distracted Learner"
}

# ---------------- USER CLASS ----------------
class User:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.study_log = []

    def add_study_session(self, subject, hours):
        today = datetime.date.today()
        self.study_log.append({
            "date": today,
            "subject": subject,
            "hours": hours
        })

    def total_hours(self):
        return sum(entry["hours"] for entry in self.study_log)

    def show_progress(self):
        print("\n📊 Study Progress:")
        for entry in self.study_log:
            print(f"{entry['date']} - {entry['subject']} - {entry['hours']} hrs")

# ---------------- AI ANALYSIS ----------------
class AIAnalyzer:
    def __init__(self, user):
        self.user = user

    def analyze(self):
        total = self.user.total_hours()
        days = len(self.user.study_log)

        if days == 0:
            return "Start studying first!"

        avg = total / days

        # Personality-based AI suggestions
        if self.user.personality == "Consistent Learner":
            if avg >= 2:
                return "Great consistency! Keep it up 🚀"
            else:
                return "Try to increase daily study time slightly."

        elif self.user.personality == "Last-Minute Crammer":
            if avg < 2:
                return "Avoid cramming! Study daily in small chunks."
            else:
                return "Good improvement! Maintain consistency."

        elif self.user.personality == "Balanced Learner":
            return "Nice balance! Keep steady progress."

        elif self.user.personality == "Distracted Learner":
            return "Reduce distractions. Try Pomodoro technique ⏱️"

        return "Keep learning!"

    def predict_performance(self):
        total = self.user.total_hours()

        if total > 20:
            return "Predicted Performance: Excellent 🌟"
        elif total > 10:
            return "Predicted Performance: Good 👍"
        else:
            return "Predicted Performance: Needs Improvement ⚠️"

# ---------------- MAIN PROGRAM ----------------
def main():
    print("📚 AI Study Habit Tracker\n")

    name = input("Enter your name: ")

    print("\nSelect your personality type:")
    for key, value in PERSONALITY_TYPES.items():
        print(f"{key}. {value}")

    choice = input("Enter choice: ")
    personality = PERSONALITY_TYPES.get(choice, "Balanced Learner")

    user = User(name, personality)
    ai = AIAnalyzer(user)

    while True:
        print("\nMenu:")
        print("1. Add Study Session")
        print("2. View Progress")
        print("3. AI Suggestion")
        print("4. Predict Performance")
        print("5. Exit")

        option = input("Enter option: ")

        if option == "1":
            subject = input("Enter subject: ")
            hours = float(input("Enter hours studied: "))
            user.add_study_session(subject, hours)
            print("✅ Session added!")

        elif option == "2":
            user.show_progress()

        elif option == "3":
            print("🤖 AI Suggestion:", ai.analyze())

        elif option == "4":
            print("📈", ai.predict_performance())

        elif option == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
