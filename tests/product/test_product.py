from inventory_report.inventory.product import Product


def test_cria_produto():
    pass
    product = Product(
        3,
        'ProdutoTest1',
        'Trybe',
        '06/08/2000',
        '-/-/-',
        '3',
        'Cuida bem do meu nenê.')

    assert product.id == 1
