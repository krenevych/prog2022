def s():
    sn = 1
    k = 1
    print(f"віддав значення {sn} назовні")
    yield sn
    print("повернувся у генератор")
    while True:
        k += 1
        sn = sn + 1 / k
        print(f"віддав значення {sn} назовні")
        yield sn
        print("повернувся у генератор")
    print("закінчив роботу!!!")


if __name__ == '__main__':
    for el in s():
        if el > 4:
            break
        print(f"отримав значення {el} з генератора")

    # el_gen = s()
    # print(el_gen)
    # while True:
    #     el = next(el_gen)
    #     print(el)
    #     if el > 4: break