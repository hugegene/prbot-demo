"""A tiny shopping cart."""


def subtotal(items):
    """Sum of price * qty over (price, qty) pairs."""
    return sum(price * qty for price, qty in items)


def total(items, tax_rate=0.07):
    """Subtotal plus tax, rounded to cents."""
    return round(subtotal(items) * (1 + tax_rate), 2)
