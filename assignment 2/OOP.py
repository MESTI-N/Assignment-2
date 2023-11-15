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
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_units_manufactured = estimated_units_manufactured
        self.monthly_stock = []

    def simulate_monthly_production_and_sales(self):
        for month in range(1, 13):
            units_manufactured = self.estimated_units_manufactured
            units_sold = random.randint(units_manufactured - 10, units_manufactured + 10)
            net_profit_loss = (units_sold * self.sale_price) - (units_manufactured * self.manufacture_cost)
            self.monthly_stock.append(MonthlyStock(month, units_sold, units_manufactured, net_profit_loss))

    def generate_predicted_stock_statement(self):
        print("Predicted Stock Statement for Product:", self.name)
        for month_stock in self.monthly_stock:
            month_stock.display()

class MonthlyStock:
    def __init__(self, month, units_sold, units_manufactured, net_profit_loss):
        self.month = month
        self.units_sold = units_sold
        self.units_manufactured = units_manufactured
        self.net_profit_loss = net_profit_loss

    def display(self):
        print("Month: "+self.month)
        print("Units Sold: "+self.units_sold)
        print("Units Manufactured: "+self.units_manufactured)
        print("Net Profit/Loss: "+self.net_profit_loss)
        print("-------------------------------")

def main():
    product_code = int(input("Please enter the Product Code (100 to 1000): "))
    product_name = input("Please enter the Product Name: ")
    sale_price = float(input("Please enter the Product Sale Price (greater than zero): "))
    manufacture_cost = float(input("Please enter the Product Manufacture Cost (greater than zero): "))
    stock_level = int(input("Please enter the Stock Level (greater than 0): "))
    estimated_units_manufactured = int(input("Please enter the Estimated Monthly Units Manufactured (greater than or equal to 0): "))

    product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_units_manufactured)
    product.simulate_monthly_production_and_sales()
    product.generate_predicted_stock_statement()

if __name__ == "__main__":
    main()
