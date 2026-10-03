def caulte_discount(price):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if price > 1000:
        raise ValueError("Price cannot exceed 1000")
    
    discount = price * 0.1
    return price - discount

try:
    price = float(input("Enter the price: "))
    discounted_price = caulte_discount(price)
    print(f"Discounted price: {discounted_price:.2f}")
except ValueError as e:
    print(f"Error Type:", type(e).__name__)
    print(f"Error message: {e}")