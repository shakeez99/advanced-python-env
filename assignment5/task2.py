import json
from typing import Any

INPUT_FILE = "students.json"
OUTPUT_FILE = "students_with_avg.json"

def average(grades: list[float]) -> float:
    return round(sum(grades) / len(grades), 2) if grades else 0.0

def main() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        students: list[dict[str, Any]] = json.load(f)

    updated = []
    for s in students:
        grades = s.get("grades", [])
        s2 = dict(s) 
        s2["average_grade"] = average(grades)
        updated.append(s2)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(updated, f, ensure_ascii=False, indent=2)

    print(f"Done! Updated data saved to '{OUTPUT_FILE}' (original kept as '{INPUT_FILE}')")

if __name__ == "__main__":
    main()
