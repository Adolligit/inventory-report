from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import SimpleReport

PRODUCT = {
        "id": "3",
        "nome_do_produto": "Xbox Three XXX",
        "nome_da_empresa": "Microsoft",
        "data_de_fabricacao": "2030-03-18",
        "data_de_validade": "2060-03-18",
        "numero_de_serie": "MCEUAXTXXX300318",
        "instrucoes_de_armazenamento": "Se deixar no lixo, serve também",
    }


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)
    colored_print = colored_report.generate([PRODUCT])

    manufature_date = "Data de fabricação mais antiga:"
    expiration_date = "Data de validade mais próxima:"
    enterprise = "Empresa com mais produtos:"

    expected = (
        f"\033[32m{manufature_date}\033[0m \033[36m2021-02-18\033[0m\n"
        f"\033[32m{expiration_date}\033[0m \033[36m2023-09-17\033[0m\n"
        f"\033[32m{enterprise}\033[0m \033[31mTarget Corporation\033[0m"
    )

    assert colored_print == expected
