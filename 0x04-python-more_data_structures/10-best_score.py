#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    valBest = 0
    keyBest = None

    for key, val in a_dictionary.items():
        if val > valBest:
            valBest = val
            keyBest = key

    return keyBest
