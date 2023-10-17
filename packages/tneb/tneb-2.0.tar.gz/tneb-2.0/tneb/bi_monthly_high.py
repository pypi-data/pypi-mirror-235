# Function to calculate electricity bill for High Usage
def bi_monthly_high(start_reading, end_reading):
    total_units = end_reading - start_reading
    bill_amount = 0

    if total_units >= 1 and total_units <= 100:
        bill_amount = 0
    elif total_units >= 101 and total_units <= 400:
        bill_amount = 4.5 * (total_units - 100)
    elif total_units >= 401 and total_units <= 500:
        bill_amount = 4.5 * 300 + 6 * (total_units - 400)
    elif total_units >= 501 and total_units <= 600:
        bill_amount = 4.5 * 300 + 6 * 100 + 8 * (total_units - 500)
    elif total_units >= 601 and total_units<=800:
        bill_amount = 4.5 * 300 + 6 * 100 + 8 * 100 + 9 * (total_units - 600)
    elif total_units >=801 and  total_units<=1000:
         bill_amount = 4.5 * 300 + 6 * 100 + 8 * 100 + 9 * 200 + 10 *(total_units - 800)
    elif total_units>=1001:
        bill_amount = 4.5 * 300 + 6 * 100 + 8 * 100 + 9 * 200 + 10 * 200 + 11 * (total_units-1000)

    return bill_amount
