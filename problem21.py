"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find 
the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""
import itertools

def problem21(lectures):
    input_data = [' '.join(str(j) for j in i) for i in lectures]
    combinations = set()
    rooms = 0
    for c in itertools.combinations(input_data, 2):
        a = set(range(*(int(n) for n in c[0].split())))
        b = set(range(*(int(i) for i in c[1].split())))
        if not a.intersection(b) == set():
            rooms += 1
    return rooms if rooms > 0 else 1


def test_problem21():
    input = [(30, 75), (0, 50), (60, 150)]
    output = 2
    assert problem21(input) == output

