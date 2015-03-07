import csv
import requests
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from pycar_advanced.results import Result

class ResultsFetcher(object):
    def fetch(self, url):
        """
        Fetch a results CSV file from a URL

        Args:
            url (string): String containing the location of the CSV file

        Returns:
            A string containing the contents of the CSV file

        """
        # TODO: Implement this
        r = requests.get(url)
        return r.text


class ResultsParser(object):
    def parse(self, s):
        """
        Parse a string containing CSV rows into result objects

        Args:
            s (string): String representing rows of data in CSV format
        
        Returns:
            Iterable of Record objects corresponding to rows in CSV format

        """
        # TODO: Implement this
        f = StringIO(s)
        reader = csv.DictReader(f)
        results = []
        for row in reader:
            results.append(Result(
                candidate_name=row['candidate_name'],
                candidate_id=row['candidate_id'],
                total_votes=int(row['total_votes'])
            ))
   
        return results


class ResultsClient(object):
    url = "http://example.com/data.csv"

    def __init__(self):
        # TODO: Implement this to compose functionality from ResultsFetcher
        # and ResultsParser
        self._fetcher = ResultsFetcher() 
        self._parser = ResultsParser()

    def parse(self, s):
        """
        Parse a string containing CSV rows into result objects

        Args:
            s (string): String representing rows of data in CSV format
        
        Returns:
            Iterable of Record objects corresponding to rows in CSV format

        """
        # TODO: Delegate to a ResultsParser instance to parse results
        return self._parser.parse(s)

    def fetch(self, url=None):
        """
        Fetch a results CSV file from a URL

        Args:
            url (string): String containing the location of the CSV file

        Returns:
            A string containing the contents of the CSV file

        """
        if url is None:
            url = self.url

        # TODO: Delegate to a ResultsFetcher instance to fetch results
        # and return a string
        return self._fetcher.fetch(url)

    def load(self):
        return self.parse(self.fetch())
