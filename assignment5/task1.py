from collections import Counter
import re

INPUT_FILE = "text.txt"
OUTPUT_FILE = "analysis.txt"

def normalize_text(text: str) -> list[str]:
    return re.findall(r"\b\w+\b", text.lower())

def main() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)

    all_words: list[str] = []
    for line in lines:
        all_words.extend(normalize_text(line))

    total_words = len(all_words)
    freq = Counter(all_words)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(f"Total lines: {total_lines}\n")
        out.write(f"Total words: {total_words}\n")
        out.write("\nWord frequency:\n")
        for word, count in freq.most_common():
            out.write(f"{word}: {count}\n")

    print(f"Done! Results saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
