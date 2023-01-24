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

    print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")

    expected = (
        "\033[32mData de fabricação mais antiga:\033[0m \033[36m2021-02-18\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m \033[36m2023-09-17\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m \033[31mTarget Corporation\033[0m"
    )

    assert colored_print == expected
