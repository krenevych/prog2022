class InputPositiveIntException(ValueError):
    def __init__(self, message, err_code, original_value, converted_value):
        pass


def InputPositiveInt(*arg, **kwargs):
    x = input(*arg, **kwargs)
    return int(x)


if __name__ == '__main__':
    x = InputPositiveInt("Введіть ціле невід'ємне число")

    print(x)
