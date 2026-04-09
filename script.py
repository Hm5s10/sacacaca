import sys
sys.stdout.reconfigure(encoding='utf-8')

MAX_LEN = 2000
SEPARATOR = "\n" * 10

def split_markdown(text, max_len=MAX_LEN):
    blocks = []
    i = 0
    n = len(text)

    while i < n:
        current = ""
        byte_len = 0
        start_i = i

        # 🔹 ajouter des caractères tant qu'on ne dépasse pas max_len
        while i < n:
            c = text[i]
            c_bytes = len(c.encode('utf-8'))
            if byte_len + c_bytes > max_len:
                break
            current += c
            byte_len += c_bytes
            i += 1

        # 🔹 essayer de couper proprement sur double saut de ligne
        cut_pos = current.rfind("\n\n")
        if cut_pos != -1 and cut_pos != len(current) - 1:
            cut_pos += 2  # inclure le \n\n
        else:
            cut_pos = current.rfind("\n")
            if cut_pos != -1 and cut_pos != len(current) - 1:
                cut_pos += 1  # inclure le \n

        if cut_pos != -1 and cut_pos != len(current):
            # remettre le surplus dans le flux
            i = start_i + cut_pos
            current = current[:cut_pos]

        blocks.append(current)

        # 🔹 sécurité : si aucun caractère ajouté, avancer d'1
        if len(current) == 0:
            blocks.append(text[i])
            i += 1

    return blocks

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py fichier.md")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    blocks = split_markdown(content)

    for idx, block in enumerate(blocks):
        print(f"--- BLOC n°{idx+1} ---\n")
        print(block)
        print("\n")
        if idx != len(blocks) - 1:
            print(SEPARATOR)

if __name__ == "__main__":
    main()