import pickle

with open("picle.dat", "rb") as f:
    loaded = pickle.load(f)
    print(loaded)
