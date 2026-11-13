from cart import subtotal, total


def test_subtotal():
    assert subtotal([(2.50, 2), (1.00, 3)]) == 8.00


def test_total_adds_tax():
    assert total([(10.00, 1)]) == 10.70


def test_bulk_discount():
    items = [(1.00, 1)] * 11
    assert total(items, tax_rate=0) == 9.90
