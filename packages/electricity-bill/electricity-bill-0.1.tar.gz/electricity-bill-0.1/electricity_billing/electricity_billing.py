class ElectricityBillCalculator:
    def __init__(self):
        pass

    def calculate_electricity_bill(self, start_reading, end_reading):
        total_units = end_reading - start_reading
        bill_amount = 0

        if total_units <= 50:
            bill_amount = total_units * 0
        elif total_units <= 100:
            bill_amount = 50 * 0 + (total_units - 50) * 2.25
        elif total_units <= 200:
            bill_amount = 50 * 0 + 50 * 2.25 + (total_units - 100) * 4.5
        elif total_units <= 250:
            bill_amount = 50 * 0 + 50 * 2.25 + 100 * 4.5 + (total_units - 200) * 6
        elif total_units <= 300:
            bill_amount = 50 * 0 + 50 * 2.25 + 100 * 4.5 + 50 * 6 + (total_units - 250) * 8
        elif total_units <= 400:
            bill_amount = 50 * 0 + 50 * 2.25 + 100 * 4.5 + 50 * 6 + 50 * 8 + (total_units - 300) * 9
        elif total_units <= 500:
            bill_amount = 50 * 0 + 50 * 2.25 + 100 * 4.5 + 50 * 6 + 50 * 8 + 100 * 9 + (total_units - 400) * 10
        else:
            bill_amount = 50 * 0 + 50 * 2.25 + 100 * 4.5 + 50 * 6 + 50 * 8 + 100 * 9 + 100 * 10 + (total_units - 500) * 11

        return bill_amount