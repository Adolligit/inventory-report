from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        6,
        "PS7",
        "Sony",
        "20-08-2030",
        "20-08-2060",
        "SCJLTDAPS7200830",
        "Lugar mais seguro da sua casa...um cofre talvez?",
    )

    assert repr(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
