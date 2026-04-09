import sys

MAX_LEN = 2000
SEPARATOR = "\n" * 10


def split_markdown(text, max_len=MAX_LEN):
    blocks = []
    current = ""

    i = 0
    while i < len(text):
        remaining = max_len - len(current)

        if remaining <= 0:
            blocks.append(current)
            current = ""
            continue

        # On cherche le dernier \n AVANT la limite
        slice_end = i + remaining
        chunk = text[i:slice_end]

        last_newline = chunk.rfind("\n")

        if last_newline != -1 and i + last_newline + 1 < len(text):
            # coupe propre sur \n
            current += chunk[:last_newline + 1]
            i += last_newline + 1
        else:
            # pas de \n → on coupe brutalement
            current += chunk
            i += len(chunk)

        if len(current) >= max_len:
            blocks.append(current)
            current = ""

    if current:
        blocks.append(current)

    return blocks


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py fichier.md")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    blocks = split_markdown(content)

    for i, block in enumerate(blocks):
        print(f"--- BLOC {i+1} ---\n")
        print("```md")
        print(block)
        print("```")

        if i != len(blocks) - 1:
            print(SEPARATOR)


if __name__ == "__main__":
    main()
