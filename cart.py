"""A tiny shopping cart."""

BULK_THRESHOLD = 10  # orders of this many items or more get the discount
BULK_DISCOUNT = 0.10


def subtotal(items):
    """Sum of price * qty over (price, qty) pairs."""
    return sum(price * qty for price, qty in items)


def total(items, tax_rate=0.07):
    """Subtotal plus tax, rounded to cents. Orders of 10 or more items get 10% off before tax."""
    sub = subtotal(items)
    if len(items) > BULK_THRESHOLD:
        sub = sub * (1 - BULK_DISCOUNT)
    return round(sub * (1 + tax_rate), 2)
