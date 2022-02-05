

def order_tally(orders_by_type_file):
    tallies = {"Musk": 0,
               "Hybrid": 0,
               "Watermelon": 0,
               "Winter": 0}

    orders = open(orders_by_type_file)

    for order in orders:
        data = order.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        tallies[melon_type] = tallies[melon_type] + melon_count

    orders.close()

    return tallies

def total_revenue(tallies):
    MELON_PRICES = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    print("TOTAL_REVENUE")

    for melon_type in tallies:
        price = MELON_PRICES[melon_type]
        melon_revenue = price * tallies[melon_type]
        total_revenue = total_revenue + melon_revenue
        print(f"We sold {tallies[melon_type]:,} {melon_type} melons at ${price:.2f} each for a total of ${melon_revenue:.2f}")

    return total_revenue


def sales_comparison(orders_with_sales_file):

    orders = open(orders_with_sales_file)
    online_revenue = 0
    salespeople_revenue = 0

    for order in orders:
        data = order.split("|")
        if data[2] == "ONLINE":
            online_revenue = online_revenue + float(data[3])
        else: 
            salespeople_revenue = salespeople_revenue + float(data[3])

    print("SALES DATA")
    print(f"Salespeople generated ${salespeople_revenue:,.2f} in revenue.")
    print(f"Internet sales generated ${online_revenue:,.2f} in revenue.")

    if salespeople_revenue > online_revenue:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")
    
    orders.close()

melon_tallies = order_tally("orders-by-type.txt")

total_revenue(melon_tallies)

print()

sales_comparison("orders-with-sales.txt")
	


