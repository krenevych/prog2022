# 1 2 3
# 4 5
# 1 9 8


def readMatrix(inputFile):
    M = []
    try:
        num_elems_in_row = None
        with open(inputFile) as f:
            for line in f:
                row = [float(el) for el in line.split()]
                if num_elems_in_row is None:
                    num_elems_in_row = len(row)

                assert len(row) == num_elems_in_row, "кількість елементів у рядках не однакова"


                M.append(row)
    except OSError as fnf_err:
        print(f"Файл {fnf_err.filename} не знайдено")
        return None
    except ValueError:
        print("Файл містить некоректні дані")
        return None
    except AssertionError as as_err:
        print(as_err)
        return None

    return M


def sumMatrix(A, B):

    try:
        assert (
                len(A) == len(B) and
                len(A[0]) == len(B[0])
                ), "розмірності матриць різні"
    except AssertionError:
        return None


    return [  # Stub
        [1, 2],
        [3, 4]
    ]

if __name__ == '__main__':
    M = readMatrix("input05.txt")
    B = readMatrix("input05_2.txt")
    print("M = ", M)
    print("B = ", B)
    C = sumMatrix(M, B)
    print(C)
