class MySet(set):

    def update(self, *s) -> None:

        for el in s:
            for inner in el:

                if type(inner) != int:
                    raise RuntimeError("AAAAAA")

                super().add(inner)


if __name__ == '__main__':
    s = MySet()
    s.update((1, 3, 4), (999, 23))

    print(s)
