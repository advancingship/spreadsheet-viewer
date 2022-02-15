from unittest import TestCase

import spreadsheet_viewer


class Test(TestCase):
    CITIES_CSV_PATH = "sample-spreadsheets/cities.csv"

    cities_csv_output = open('cities_csv_output.txt')
    CITIES_CSV_OUTPUT = cities_csv_output.read()
    cities_csv_output.close()

    CITIES_XLS_PATH = "sample-spreadsheets/cities.xls"

    CITIES_XLSX_PATH = "sample-spreadsheets/cities.xlsx"

    cities_xls_output = open('cities_xls_output.txt')
    CITIES_XLS_OUTPUT = cities_xls_output.read()
    cities_xls_output.close()

    def test_get_csv_data(self):
        self.maxDiff = None
        self.assertEqual(spreadsheet_viewer.get_csv_data(self.CITIES_CSV_PATH), self.CITIES_CSV_OUTPUT)

    def test_get_xls_data(self):
        self.assertEqual(spreadsheet_viewer.get_xls_data(self.CITIES_XLS_PATH), self.CITIES_XLS_OUTPUT)

    def test_get_xlsx_data(self):
        self.assertEqual(spreadsheet_viewer.get_xlsx_data(self.CITIES_XLSX_PATH), self.CITIES_XLS_OUTPUT)
