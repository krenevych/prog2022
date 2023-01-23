import pickle

with open("picle.dat", "wb") as f:
    d = [1, 3, 4, 5, 6, 8, "hello world"]
    pickle.dump(d, f)
