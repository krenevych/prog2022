def sumInFile(file_name):
    suma = 0
    with open(file_name) as f:
        for line in f:
            # print(line.split())
            suma += sum([float(el) for el in line.split()])
    return suma


def numberOfNegativeComponents(fileName):
    number_of_negative_components = 0
    with open(fileName) as f:
        for line in f:
            numbers_str = line.split()
            for number in numbers_str:
                if float(number) < 0:
                    number_of_negative_components += 1
    return number_of_negative_components


def findLesThanAvarage(fileName):
    #     кількості компонент файла, які менші за середнє арифметичне всіх його компонент.
    suma = 0
    count = 0
    with open(fileName) as f:
        for line in f:
            elems = [float(el) for el in line.split()]
            suma += sum(elems)
            count += len(elems)
        average = suma / count # середнє арифметичне

        f.seek(0)

        count_less_than_av = 0
        for line in f:
            # print(line)
            elems = [float(el) for el in line.split()]
            for el in elems:
                if el < average:
                    count_less_than_av += 1

        return count_less_than_av


if __name__ == '__main__':
    print(findLesThanAvarage("input02.txt"))
