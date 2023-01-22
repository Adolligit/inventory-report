from inventory_report.inventory.product import Product


def test_cria_produto():
    pass
    product = Product(
        6,
        'ProdutoTest1',
        'Trybe',
        '06/08/2000',
        '-/-/-',
        '3',
        'Cuida bem do meu nenê.')

    assert product.id == 1
    assert product.nome_do_produto == 'ProdutoTest1'
    assert product.nome_da_empresa == 'Trybe'
    assert product.data_de_fabricacao == '06/08/2000'
    assert product.data_de_validade == '-/-/-'
    assert product.numero_de_serie == '3'
    assert product.instrucoes_de_armazenamento == 'Cuida bem do meu nenê.'
