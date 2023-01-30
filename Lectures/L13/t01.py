v = 10
try:
    # f = open("input.txt")
    res = 1 / v
    print(res)
except IndexError:
    print("IndexError")
except ZeroDivisionError:
    print("Ох ти негідник! Ділити на нуль не можна - йди вчитись в школу!")
except FileNotFoundError:
    print("File is not found!")
else:
    print("Block else")
finally:
    print("Block finally")

pass