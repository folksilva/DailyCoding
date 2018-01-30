"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original 
sentence in a list. If there is more than one possible reconstruction, return any of them. If there 
is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string 
"thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""
import itertools
import unittest

def problem22(dictionary, word):
    all_combinations = []
    sentences = []
    for i in range(2, len(dictionary)+1):
        all_combinations += itertools.permutations(dictionary, i)
    for c in all_combinations:
        if ''.join(c) == word:
            sentences.append(list(c))
    return sentences


class TestProblem22(unittest.TestCase):

    def test_a(self):
        dictionary = ['quick', 'brown', 'the', 'fox']
        word = 'thequickbrownfox'
        result = [['the','quick','brown','fox']]
        self.assertCountEqual(problem22(dictionary, word), result)


    def test_b(self):
        dictionary = ['bed','bath','bedbath','and','beyond']
        word = 'bedbathandbeyond'
        result = [['bed','bath','and','beyond'],['bedbath','and','beyond']]
        self.assertCountEqual(problem22(dictionary, word), result)
