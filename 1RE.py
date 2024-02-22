#Regular Expression
import re

def main():
    text = "The quick brown fox jumps over the lazy dog"

    pattern = r'\b(fox|dog)\b'
    match = re.search(pattern, text)
    if match:
        print("Found:", match.group())
    else:
        print("Pattern not found")
    matches = re.findall(pattern, text)
    if matches:
        print("Found:", matches)
    else:
        print("Pattern not found")
    for match in re.finditer(pattern, text):
        print("Found:", match.group(), "at position:", match.start())
    replaced_text = re.sub(pattern, "animal", text)
    print("Replaced text:", replaced_text)

if __name__ == "__main__":
    main()
