# Quasion 10
shares_bought = 1000
price_per_share_bought = 32.87
commission_rate = 0.02

amount_paid = shares_bought * price_per_share_bought
commission_paid_buying = amount_paid * commission_rate

shares_sold = 1000
price_per_share_sold = 33.92

amount_received = shares_sold * price_per_share_sold
commission_paid_selling = amount_received * commission_rate

profit_or_loss = amount_received - amount_paid - commission_paid_buying - commission_paid_selling

print(f"The amount of money Joe paid for the stock is: {amount_paid}")
print(f"The amount of commission Joe paid his broker when he bought the stock is: {commission_paid_buying}")
print(f"The amount that Joe sold the stock for is: {amount_received}")
print(f"The amount of commission Joe paid his broker when he sold the stock is: {commission_paid_selling}")
print(f"The amount of money that Joe had left when he sold the stock and paid his broker (both times) is: {profit_or_loss}")
