import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if 'xml' in file_path:
            with open(file_path, encoding='utf-8') as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        else:
            raise ValueError('Arquivo inválido')
