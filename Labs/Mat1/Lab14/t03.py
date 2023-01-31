max_nominal = 4
wallet = {
    1: 20,
    2: 4,

    4: 3,
}

suma = 0
for i in range(1, max_nominal + 1):
    try:
        suma += i * wallet[i]
    except KeyError:
        pass

# for key, val in wallet.items():
#     suma += key * val

print(f"у гаманці {suma} у.о")
