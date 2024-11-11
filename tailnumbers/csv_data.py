"""
csv_data.py
"""

import os
import csv

class CsvData:

    def __init__(self, fpath):
        self.fpath = os.path.expandvars(fpath)
        self.data = []
        with open(self.fpath, 'r') as fp:
            dict_reader = csv.DictReader(fp)
            for row in dict_reader:
                self.data.append(row)
        self._clean()

    def _clean(self):
        # remove whitespace arround values
        for row in self.data:
            for key in row.keys():
                try:
                    row[key] = row[key].strip()
                except AttributeError:
                    pass

        for row in self.data:
            keys_list = list(row.keys())
            for key in keys_list:
                if key and '\ufeff' in key:
                    new_key = key.replace('\ufeff', '')
                    row[new_key] = row.pop(key)

    def get(self, key, val):
        for row in self.data:
            if row[key] == val:
                return row

    def data(self):
        return self.data
