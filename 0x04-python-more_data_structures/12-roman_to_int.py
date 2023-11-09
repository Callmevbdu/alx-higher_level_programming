#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    sum_ = 0
    classicNum = 0
    romanNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for rev in reversed(roman_string):
        classicNum = romanNum[rev]
        sum_ += classicNum if sum_ < classicNum * 5 else -classicNum

    return sum_
