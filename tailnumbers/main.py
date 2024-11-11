"""
main.py
"""

import os

from .csv_data import CsvData

class TailNumbers:

    def __init__(self, data_dir):
        self.master_data = CsvData(os.path.join(data_dir, 'MASTER.txt'))
        self.engine_data = CsvData(os.path.join(data_dir, 'ENGINE.txt'))
        self.acftref_data = CsvData(os.path.join(data_dir, 'ACFTREF.txt'))
        self.dealer_data = CsvData(os.path.join(data_dir, 'DEALER.txt'))
        self.dereg_data = CsvData(os.path.join(data_dir, 'DEREG.txt'))
        self.docindex_data = CsvData(os.path.join(data_dir, 'DOCINDEX.txt'))
        self.reserved_data = CsvData(os.path.join(data_dir, 'RESERVED.txt'))

    def get_tailnumber(self, tailnumber):
        if tailnumber[0].upper() == 'N':
            tailnumber = tailnumber[1:]   
        data = self.master_data.get('N-NUMBER', tailnumber)
        data['aircraft_ref'] = self.acftref_data.get('CODE', data['MFR MDL CODE'])
        data['engine'] = self.engine_data.get('CODE',  data['ENG MFR MDL'])
        return data

