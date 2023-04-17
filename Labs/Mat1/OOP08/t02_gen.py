def s(k):
    sn = 1
    print(f"віддав значення {sn} назовні")
    yield sn
    print("повернувся у функцію")
    for k in range(2, k + 1):
        sn = sn + 1 / k
        print(f"віддав значення {sn} назовні")
        yield sn
        print("повернувся у функцію")
    print("закінчив роботу!!!")


if __name__ == '__main__':
    for el in s(10):
        print(f"отримав значення {el} з генератора")
