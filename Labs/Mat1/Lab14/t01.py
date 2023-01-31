# Знайти площу трикутника за трьома сторонами a,b,c.
# Оформити перевірку вхідних даних
# (що трикутник з такими сторонами a,b,c існує) за допомогою оператора assert.


a, b, c = [float(a) for a in input().split()]
try:
    assert a + b > c and a + c > b and b + c > a, "Такого трикутника не існує"

    p = (a + b + c) / 2.0
    s = p * (p - a) * (p - b) * (p - c)
    s = s ** 0.5
    print(f"Площа трикутника зі сторонами {a}, {b}, {c} = {s}")

except AssertionError as as_err:
    print(as_err)

