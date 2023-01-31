def readFile(fileName):
    try:
        with open(fileName, encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except OSError as fnf_err:
        print(f"Файл {fnf_err.filename} не знайдено")

readFile("input04_.txt")