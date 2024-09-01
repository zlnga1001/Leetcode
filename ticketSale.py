# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

# Hint: Looping over dictionary; dict.keys(), dict.items(), dict.values()

def total_sales(ticket_sales):
    total = 0
    for i in ticket_sales.values():
        total += i
    return total




ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))