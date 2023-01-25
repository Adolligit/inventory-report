from inventory_report.importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path: str, type: str):
        content = self.importer().import_data(path)
        self.data += content
        return self.__whats_the_type(type, content)

    def __whats_the_type(self, type: str, content: list):
        return (
            CompleteReport.generate(content)
            if type == 'completo'
            else SimpleReport.generate(content)
        )
