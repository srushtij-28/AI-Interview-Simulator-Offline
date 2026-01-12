questions = {
    "What is Python?": "programming",
    "What is machine learning?": "data",
    "What is a function?": "code",
    "What is AI?": "intelligence",
    "What is a loop?": "repeat"
}

print("🧠 AI Interview Simulator \n")

score = 0

for q, keyword in questions.items():
    print("Q:", q)
    ans = input("Your answer: ").lower()

    if keyword in ans:
        print("✅ Correct\n")
        score += 1
    else:
        print("❌ Not quite\n")

print("📊 Interview Result")
print("Score:", score, "/", len(questions))

if score >= 4:
    print("🎉 Excellent! You are interview ready.")
elif score >= 2:
    print("🙂 Good, but practice more.")
else:
    print("⚠️ Needs improvement.")
