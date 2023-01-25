import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    importers = {
        "json": JsonImporter,
        "csv": CsvImporter,
        "xml": XmlImporter,
    }

    _, path, type = sys.argv
    extension = path.split(".")
    inventory_refactor = InventoryRefactor(importers[extension[-1]])
    printed_result = inventory_refactor.import_data(path, type)
    sys.stdout.write(printed_result)
