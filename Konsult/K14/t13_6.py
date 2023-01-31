def write(in_file_name, out_file_name):
    in_f = open(in_file_name, encoding="utf-8")
    lines = in_f.readlines()
    in_f.close()
    lines = [line.strip() for line in lines]
    text = "".join(lines)

    f = open(out_file_name, "wt", encoding="utf-8")
    lst = [text[x:x + 40] for x in range(0, len(text), 40)]
    for el in lst:
        print(el, file=f)
    f.close()


write("input.txt", "text.txt")
