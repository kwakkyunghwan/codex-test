def apply_conditions(stocks, conditions):
    """Return stocks that satisfy conditions.
    Currently supports a simple minimum price filter.
    """
    min_price = conditions.get('min_price', 0)
    return [s for s in stocks if s.get('price', 0) >= min_price]
