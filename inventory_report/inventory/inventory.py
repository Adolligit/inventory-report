import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(self, path, type):
        if "csv" in path:
            return Inventory.import_csv_file(path, type)

    @classmethod
    def import_csv_file(path, type):
        with open(path, encoding="utf-8") as file:
            result = list(csv.DictReader(file, delimiter=',', quotechar='"'))
            return Inventory.whats_the_type(type, result)

    @classmethod
    def whats_the_type(type, content):
        return (
            CompleteReport.generate(content)
            if type == 'completo'
            else SimpleReport.generate(content)
        )
