def sumEmements(file_name):
    with open(file_name) as f:
        elements = [float(el) for el in f.read().split()]
        return sum(elements)

def countNegEmements(file_name):
    with open(file_name) as f:
        elements = [float(el) for el in f.read().split()]
        counter = 0
        for el in elements:
            if el < 0:
                counter += 1
        return counter


def minEvenEmements(file_name):
    with open(file_name) as f:
        elements = [float(el) for el in f.read().split()]
        minEven = elements[0]
        for el in elements[2::2]:
            if el < minEven:
                minEven = el
        return minEven

def countLesThanAverage(file_name):
    # кількості компонент файла, які менші за середнє арифметичне всіх його компонент.
    with open(file_name) as f:
        elements = [float(el) for el in f.read().split()]
        average = sum(elements) / len(elements)
        # elements.clear()
        print(average)

        # f.seek(0)
        # elements = [float(el) for el in f.read().split()]
        # print("прочитані елементи:", elements)
        counter = 0
        for el in elements:
            if el < average:
                counter += 1

        return counter




# print(sumEmements("input02.txt"))
# print(countNegEmements("input02.txt"))
# print(minEvenEmements("input02.txt"))
print(countLesThanAverage("input02.txt"))

