from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'csv' in path:
            with open(path, encoding='utf-8') as file:
                return list(
                    csv.DictReader(file, delimiter=',', quotechar='"')
                )
        else:
            raise ValueError('Arquivo inválido')
