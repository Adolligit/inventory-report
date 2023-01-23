from datetime import datetime
from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list_product: list) -> str:
        oldest_manufacture = [
            key["data_de_fabricacao"]
            for key in list_product
        ]

        close_to_expiration = [
            key["data_de_validade"]
            for key in list_product
            if key["data_de_validade"] > datetime.now().strftime("%Y-%m-%d")
        ]

        enterprise = Counter(
            key["nome_da_empresa"]
            for key in list_product
        ).most_common()

        stocked_products = ''

        for company, qnt in enterprise:
            stocked_products += (f"- {company}: {qnt}\n")

        return (
            f"Data de fabricação mais antiga: {min(oldest_manufacture)}\n"
            f"Data de validade mais próxima: {min(close_to_expiration)}\n"
            f"Empresa com mais produtos: {enterprise[0][0]}\n"
            f"Produtos estocados por empresa:\n{stocked_products}"
        )
