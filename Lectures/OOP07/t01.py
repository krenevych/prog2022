if __name__ == '__main__':
    lst = [1, 2, 3]
    d = {1: 1, 5: "111"}

    try:
        # print(d[3])
        print(lst[6])
    except Exception as er:
        print("Error:", er)
        print("Type:", type(er))

