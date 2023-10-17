def calculate_net_income(gross_income):
    if gross_income > 1500:
        tax_rate = 0.23
    elif 1300 <= gross_income <= 1500:
        tax_rate = 0.13
    elif gross_income < 0:
        print(f"Wage is not correct")
        return None
    else:
        tax_rate = 0

    tax_amount = gross_income * tax_rate

    net_income = gross_income - tax_amount

    return net_income



gross_income = -1500
net_income = calculate_net_income(gross_income)
print(f"Net Income: {net_income}")
