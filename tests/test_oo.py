import unittest

import responses

from pycar_advanced.oo import ResultsParser, ResultsFetcher, ResultsClient 


class ResultsTestMixin(object):
    results_csv = """candidate_name,candidate_id,total_votes
Rahm Emanuel,18957,211597
Jesus "Chuy" Garcia,21600,157526
Willie Wilson,21598,49612
"""

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

    csv_url = 'http://example.com/data.csv'

    def _test_results(self, results):
        self.assertEqual(len(results), len(self.result_attrs))

        for i, result in enumerate(results):
            self.assertEqual(result.candidate_name,
                self.result_attrs[i]['candidate_name'])
            self.assertEqual(result.candidate_id,
                self.result_attrs[i]['candidate_id'])
            self.assertEqual(result.total_votes,
                self.result_attrs[i]['total_votes'])


# TODO: Use the ResultsTestMixin to DRY up these three test cases 

class ResultParserTestCase(unittest.TestCase):
    def test_parse(self):
        parser = ResultsParser()
        results = parser.parse(self.results_csv)
        self._test_results(results)


class ResultFetcherTestCase(unittest.TestCase):
    @responses.activate
    def test_fetch(self):
        responses.add(responses.GET, self.csv_url, 
            body=self.results_csv, status=200, content_type='text/csv')
                                                       
        fetcher = ResultsFetcher()
        csv_s = fetcher.fetch('http://example.com/data.csv')
        self.assertEqual(csv_s.strip(), self.results_csv.strip())


class ResultClientTestCase(ResultsTestMixin, unittest.TestCase):
    @responses.activate
    def test_load(self):
        # TODO: Implement this
        self.fail()
