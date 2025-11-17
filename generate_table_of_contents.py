import os
import re
from urllib.parse import quote

README = "README.md"
START = "<!-- PROBLEMS-TABLE:START -->"
END = "<!-- PROBLEMS-TABLE:END -->"


def generate_table():
    pattern = re.compile(r"Problem (\d+): (.+)\.py")
    rows = []

    for root, _, files in os.walk("."):
        for f in files:
            m = pattern.match(f)
            if m:
                num, name = m.groups()
                rel_path = os.path.join(root, f).replace("\\", "/").lstrip("./")
                url = f"https://github.com/pranavagrawal321/Project-Euler/blob/master/{quote(rel_path)}"
                rows.append((int(num), name, f"{url}"))

    rows.sort(key=lambda t: t[0])

    table = [
        "| Problem | File | Link |",
        "|---------|------|------|",
    ]

    for num, name, url in rows:
        table.append(f"| {num} | {name} | [Link]({url}) |")

    return "\n".join(table)


def update_readme():
    with open(README, "r") as f:
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
        with open(README, "w") as f:
            f.write(new_content)
        print("README.md updated.")
        return 1  # cause pre-commit to fail so user commits updated file
    else:
        print("README.md already up to date.")
        return 0


if __name__ == "__main__":
    exit(update_readme())
