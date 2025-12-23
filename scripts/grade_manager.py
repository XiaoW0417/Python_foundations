from pathlib import Path
import json

file_path = Path("../data/students.json")
file_path.parent.mkdir(parents=True, exist_ok=True)

def find_top_students(students, top_n=3):
        results = sorted(students, key=lambda x: (x.get("score"), x.get("name")), reverse=True)
        return results[:top_n]

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    top_n = 3
    top_students = find_top_students(data, top_n)

    print(f"Top {top_n} Students:")
    for i, student in enumerate(top_students):
        print(f"Rank {i}: [{student.get("id")}] {student.get("name")} - Score: {student.get("score")}")

except Exception as e:
    print(f"Error: {e}")