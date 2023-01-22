from datetime import datetime
from collections import Counter


class SimpleReport:
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
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {min(oldest_manufacture)}\n"
            f"Data de validade mais próxima: {min(close_to_expiration)}\n"
            f"Empresa com mais produtos: {enterprise}"
        )

# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com mais produtos: NOME DA EMPRESA
