import os
import re
import subprocess
from urllib.parse import quote

README = "README.md"
START = "<!-- PROBLEMS-TABLE:START -->"
END = "<!-- PROBLEMS-TABLE:END -->"


def generate_table():
    # Match ONLY valid problem files
    pattern = re.compile(r"^Problem (\d+): (.+)\.py$")
    rows = []

    # Get only files tracked by Git (respects .gitignore automatically)
    result = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    )
    tracked_files = result.stdout.splitlines()

    for rel_path in tracked_files:
        filename = os.path.basename(rel_path)
        m = pattern.match(filename)
        if m:
            num, name = m.groups()
            url = (
                "https://github.com/pranavagrawal321/Project-Euler/blob/master/"
                f"{quote(rel_path)}"
            )
            rows.append((int(num), name, url))

    rows.sort(key=lambda t: t[0])

    table = [
        "| Problem | File | Link |",
        "|---------|------|------|",
    ]

    for num, name, url in rows:
        table.append(f"| {num} | {name} | [Link]({url}) |")

    return "\n".join(table)


def update_readme():
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    start_i = content.find(START)
    end_i = content.find(END)

    if start_i == -1 or end_i == -1:
        raise SystemExit("README.md does not contain the required markers.")

    table = generate_table()

    new_content = (
        content[: start_i + len(START)] + "\n" + table + "\n" + content[end_i:]
    )

    if new_content != content:
        with open(README, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated.")
        return 1
    else:
        print("README.md already up to date.")
        return 0


if __name__ == "__main__":
    raise SystemExit(update_readme())
