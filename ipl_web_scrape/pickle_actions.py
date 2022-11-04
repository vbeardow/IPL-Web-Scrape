import pickle


def pickle_dump(list, pick_path):

    with open(pick_path, "wb") as pick:
        pickle.dump(list, pick)

    print(f"{len(list)} items pickled to {pick_path}")


def pickle_load(pick_path):

    with open(pick_path, "rb") as pick:
        out = pickle.load(pick)

    print(f"{len(out)} items loaded from {pick_path}")

    return out
