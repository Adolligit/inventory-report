import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if "csv" in path:
            return Inventory.import_csv_file(path, type)

    @staticmethod
    def import_csv_file(path: str, type: str):
        with open(path, encoding="utf-8") as file:
            result = list(csv.DictReader(file, delimiter=',', quotechar='"'))
            return Inventory.whats_the_type(type, result)

    @staticmethod
    def whats_the_type(type: str, content: list):
        return (
            CompleteReport.generate(content)
            if type == 'completo'
            else SimpleReport.generate(content)
        )
