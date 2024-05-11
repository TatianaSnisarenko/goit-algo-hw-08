import unittest
from task1 import Cabel, merge_cabels_in_pairs, merge_cabels_into_one


class TestCabelMethods(unittest.TestCase):

    def test_merge_cabels_in_pairs(self):
        cable_input = [('A', 12), ('B', 11), ('C', 13),
                       ('D', 5), ('E', 6), ('F', 7), ('G', 8), ('H', 33)]
        cabels = [Cabel(cabel[0], cabel[1]) for cabel in cable_input]

        expected_result = (
            [('D', 'E'), ('F', 'G'), ('B', 'A'), ('C', 'H')], sum([x[1] for x in cable_input]))
        result = merge_cabels_in_pairs(cabels)
        self.assertEqual(result, expected_result)

    

    def test_merge_cabels_into_one(self):
        cable_input = [('A', 12), ('B', 11), ('C', 13),
                       ('D', 5), ('E', 6), ('F', 7), ('G', 8), ('H', 33)]
        cabels = [Cabel(cabel[0], cabel[1]) for cabel in cable_input]

        expected_result = (
            [('D', 'E'), ('F', 'G'), ('DE', 'B'), ('A', 'C'), ('FG', 'DEB'),
             ('AC', 'H'), ('FGDEB', 'ACH')], sum([x[1] for x in cable_input]))
        result = merge_cabels_into_one(cabels)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
