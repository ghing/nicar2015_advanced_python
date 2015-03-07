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


class ResultsClient(object):
    url = "http://example.com/data.csv"

    def __init__(self):
        # TODO: Implement this to compose functionality from ResultsFetcher
        # and ResultsParser

    def parse(self, s):
        """
        Parse a string containing CSV rows into result objects

        Args:
            s (string): String representing rows of data in CSV format
        
        Returns:
            Iterable of Record objects corresponding to rows in CSV format

        """
        # TODO: Delegate to a ResultsParser instance to parse results

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

    def load(self):
        return self.parse(self.fetch())
