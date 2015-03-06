import unittest

from pycar_advanced.functional import Result, generate_results, candidate_first_names

class FunctionalTestCase(unittest.TestCase):
    def test_generate_results(self):
        result_attrs = [
            {
                'candidate_name': 'Rahm Emanuel',
                'candidate_id': '18957',
                'total_votes': 211597,
            },
            {
                'candidate_name': 'Jesus "Chuy" Garcia',
                'candidate_id': '21600',
                'total_votes': 157526,
            },
            {
                'candidate_name': 'Willie Wilson',
                'candidate_id': '21598',
                'total_votes': 49612,
            },
        ]

        result_iter = generate_results(result_attrs)

        for i in range(len(result_attrs)):
            result = next(result_iter)
            self.assertEqual(isinstance(result, Result), True)
            self.assertEqual(result.candidate_name,
                             result_attrs[i]['candidate_name'])
            self.assertEqual(result.candidate_id,
                             result_attrs[i]['candidate_id'])
            self.assertEqual(result.total_votes,
                             result_attrs[i]['total_votes'])

        self.assertRaises(StopIteration, result_iter.next)

    def test_candidate_first_names(self):
        result_attrs = [
            {
                'candidate_name': 'Rahm Emanuel',
                'candidate_id': '18957',
                'total_votes': 211597,
            },
            {
                'candidate_name': 'Jesus "Chuy" Garcia',
                'candidate_id': '21600',
                'total_votes': 157526,
            },
            {
                'candidate_name': 'Willie Wilson',
                'candidate_id': '21598',
                'total_votes': 49612,
            },
        ]

        result_iter = generate_results(result_attrs)
        first_names = candidate_first_names(result_iter)
        self.assertEqual(first_names[0], "Rahm")
        self.assertEqual(first_names[1], "Jesus")
        self.assertEqual(first_names[2], "Willie")
