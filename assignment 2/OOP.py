# Assignment 2
'''
Summary: Perform the object-oriented analysis process to find 
the objects a given a program is made of. Once the objects are found, 
complete the object-oriented design process to find the classes that 
correspond to the objects found. With the object-oriented design finalized, 
implement the program using Visual Studio Code IDE.
'''
import random

class Product:
    def __init__(self, code, name, sale_price, manuf_cost, stock_lvl, est_units_manufactured):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manuf_cost = manuf_cost
        self.stock_lvl = stock_lvl
        self.est_units_manufactured = est_units_manufactured
        self.monthly_stock = []
        self.unfulfilled_sales = 0

    def simulate_monthly_production_and_sales(self):
        for month in range(1, 13):
            units_manufactured = self.est_units_manufactured
            units_sold = random.randint(units_manufactured - 10, units_manufactured + 10)
            units_sold = min(units_sold, self.stock_lvl)  # Ensure stock doesn't go negative
            self.stock_lvl -= units_sold
            if units_sold < 0:
                self.unfulfilled_sales -= units_sold  # Count unfulfilled sales
                units_sold = 0  # No units sold if stock is insufficient
            net_profit_loss = (units_sold * self.sale_price) - (units_manufactured * self.manuf_cost)
            self.monthly_stock.append(MonthlyStock(month, units_sold, units_manufactured, net_profit_loss))

def generate_predicted_stock_statement(self):
        print("\nPredicted Stock Statement for Product:", self.name)
        for month_stock in self.monthly_stock:
            month_stock.display()
        if self.unfulfilled_sales > 0:
            print("\nDetails of unfulfilled sales:")
            print("Units that could not be sold:", self.unfulfilled_sales)


class MonthlyStock:
    def __init__(self, month, units_sold, units_manufactured, net_profit_loss):
        self.month = month
        self.units_sold = units_sold
        self.units_manufactured = units_manufactured
        self.net_profit_loss = net_profit_loss

    def display(self):
        print("\nMonth:", self.month)
        print("Units Sold:", self.units_sold)
        print("Units Manufactured:", self.units_manufactured)
        print("Net Profit/Loss:", self.net_profit_loss)
        print("-------------------------------")

def get_pos_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 100 <= value <= 1000:
                return value
            else:
                print("Please enter a valid Product Code between 100 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_pos_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive real number.")
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

def main():
    code = get_pos_int_input("Please enter the Product Code (100 to 1000): ")
    name = input("Please enter the Product Name: ")
    sale_price = get_pos_float_input("Please enter the Product Sale Price (greater than zero): ")
    manuf_cost = get_pos_float_input("Please enter the Product Manufacture Cost (greater than zero): ")
    stock_lvl = get_pos_int_input("Please enter the Stock Level (greater than 0): ")
    est_units_manufactured = get_pos_int_input("Please enter the Estimated Monthly Units Manufactured (greater than or equal to 0): ")

    product = Product(code, name, sale_price, manuf_cost, stock_lvl, est_units_manufactured)
    product.simulate_monthly_production_and_sales()
    product.generate_predicted_stock_statement()

if __name__ == "__main__":
    main()