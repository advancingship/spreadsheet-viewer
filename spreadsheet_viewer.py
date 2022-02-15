import csv
import sys
import pandas
from pathlib import Path


escape_character = "\\"


def get_csv_data(path):
    try:
        return pandas.read_csv(path).to_csv(
            quoting=csv.QUOTE_NONE, escapechar=escape_character, index_label=False, index=False
        )
    except pandas.errors.EmptyDataError as error:
        print(str(error))


def get_xls_data(path):
    return pandas.read_excel(path).to_csv(index_label=False, index=False)


def get_xlsx_data(path):
    with open(path, mode='rb') as file:
        return pandas.read_excel(file.read(), engine="openpyxl").to_csv(index_label=False, index=False)


extension_to_getter_map = {'csv': get_csv_data, 'xls': get_xls_data, 'xlsx': get_xlsx_data}


def get_spreadsheet_data(path):
    file_extension = Path(path).suffix.lower()[1:]
    try:
        return extension_to_getter_map[file_extension](path)
    except KeyError:
        print(f'files with .{file_extension} extension are not currently supported')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(get_spreadsheet_data(sys.argv[1]))
    else:
        print("usage: python spreadsheet_viewer.py /path/to/file-name")
