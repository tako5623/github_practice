def CalcPrice(base_price):

    discount_rate = 0.2
    consumption_tax = 0.08
    price = base_price

    price *= (1.0 + consumption_tax)
    price *= (1.0 - discount_rate)

    return price


print(CalcPrice(1000))
