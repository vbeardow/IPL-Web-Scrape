import pickle
from typing import List, Any


def pickle_dump(list: List[Any], pick_path: str) -> None:
    """Dump list items to file at specified file path

    Args:
        list (List): List of objects to be pickled
        pick_path (str): Path for file where items are pickled
    """

    with open(pick_path, "wb") as pick:
        pickle.dump(list, pick)

    print(f"{len(list)} items pickled to {pick_path}")


def pickle_load(pick_path: str) -> List[Any]:
    """Load items from pickle file

    Args:
        pick_path (str): Path to pickle file to load from

    Returns:
        List[Any]: Returns items from pickled file as list
    """

    with open(pick_path, "rb") as pick:
        out = pickle.load(pick)

    print(f"{len(out)} items loaded from {pick_path}")

    return out
