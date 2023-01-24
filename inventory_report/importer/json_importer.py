import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if 'json' in file_path:
            with open(file_path, encoding='utf-8') as file:
                return json.load(file)
        else:
            raise ValueError('Arquivo inválido')
