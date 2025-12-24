#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_k = None
    best_v = None
    for k, v in a_dictionary.items():
        if best_v is None or v > best_v:
            best_v = v
            best_k = k
    return best_k
