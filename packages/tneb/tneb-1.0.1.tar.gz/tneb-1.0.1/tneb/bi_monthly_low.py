
# Function to calculate electricity bill for Low usage
def bi_monthly_low(start_reading, end_reading):
    total_units = end_reading - start_reading
    bill_amount = 0

    if total_units >= 1 and total_units <= 100:
        bill_amount = 0
    elif total_units >= 101 and total_units <= 200:
        bill_amount = 100 * 0 + 2.25 * (total_units-100)
    elif total_units >= 201 and total_units <= 400:
        bill_amount = 100 * 0  + 100 * 2.25 + 4.5 * (total_units-200)
    elif total_units >= 401 and total_units <= 500:
        bill_amount = 100 * 0 + 100 * 2.25 + 200 * 4.5 + 6 * (total_units - 400 )

    return bill_amount