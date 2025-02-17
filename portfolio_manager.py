class StockPortfolioManager:
    def __init__(self):
        """
        Constructor initializes:
        1. A dictionary (self.portfolios) to hold multiple portfolios.
        2. An available balance set to $10,000.
        """
        self.portfolios = {}  # {portfolio_name: {stock_symbol: shares_owned}}
        self.balance = 10000.0

    def add_portfolio(self, portfolio_name):
        """
        Adds a new portfolio to the collection.
        If the portfolio already exists, it will not overwrite it.
        """
        if portfolio_name in self.portfolios:
            print(f"Portfolio '{portfolio_name}' already exists.")
        else:
            self.portfolios[portfolio_name] = {}
            print(f"New portfolio '{portfolio_name}' created successfully.")

    def add_stock(self, portfolio_name, stock_symbol, initial_shares=0):
        """
        Adds a new stock to the specified portfolio with an initial number of shares.
        If the portfolio or stock already exists, it handles those cases appropriately.
        """
        if portfolio_name not in self.portfolios:
            print(f"Portfolio '{portfolio_name}' does not exist.")
            return

        if stock_symbol in self.portfolios[portfolio_name]:
            print(f"Stock '{stock_symbol}' already in portfolio '{portfolio_name}'.")
        else:
            self.portfolios[portfolio_name][stock_symbol] = initial_shares
            print(f"Stock '{stock_symbol}' added to portfolio '{portfolio_name}' with {initial_shares} shares.")

    def buy_shares(self, portfolio_name, stock_symbol, shares_to_buy, price_per_share):
        """
        Buys a specified number of shares for an existing stock in a portfolio.
        Ensures sufficient funds are available before completing the purchase.
        """
        if portfolio_name not in self.portfolios:
            print(f"Portfolio '{portfolio_name}' does not exist.")
            return

        if stock_symbol not in self.portfolios[portfolio_name]:
            print(f"Stock '{stock_symbol}' does not exist in portfolio '{portfolio_name}'.")
            return

        total_cost = shares_to_buy * price_per_share

        # Check for sufficient funds
        if total_cost > self.balance:
            print("Error: Insufficient funds to buy shares.")
            return

        # Deduct from balance and update shares
        self.balance -= total_cost
        self.portfolios[portfolio_name][stock_symbol] += shares_to_buy
        print(f"Successfully bought {shares_to_buy} shares of '{stock_symbol}' in portfolio '{portfolio_name}'.")
        print(f"Total cost: ${total_cost:.2f}, Remaining balance: ${self.balance:.2f}")

    def sell_shares(self, portfolio_name, stock_symbol, shares_to_sell, price_per_share):
        """
        Sells a specified number of shares from an existing stock in a portfolio.
        Ensures enough shares are owned to complete the transaction.
        """
        if portfolio_name not in self.portfolios:
            print(f"Portfolio '{portfolio_name}' does not exist.")
            return

        if stock_symbol not in self.portfolios[portfolio_name]:
            print(f"Stock '{stock_symbol}' does not exist in portfolio '{portfolio_name}'.")
            return

        current_shares = self.portfolios[portfolio_name][stock_symbol]

        if shares_to_sell > current_shares:
            print("Error: Insufficient shares to sell.")
            return

        # Calculate revenue
        total_revenue = shares_to_sell * price_per_share
        self.portfolios[portfolio_name][stock_symbol] -= shares_to_sell
        self.balance += total_revenue
        print(f"Successfully sold {shares_to_sell} shares of '{stock_symbol}' in portfolio '{portfolio_name}'.")
        print(f"Total revenue: ${total_revenue:.2f}, New balance: ${self.balance:.2f}")

    def deposit_money(self, amount):
        """
        Adds funds to the current balance.
        """
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw_money(self, amount):
        """
        Deducts funds from the current balance, ensuring the user does not overdraw.
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Error: Insufficient funds to withdraw.")
            return
        self.balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

    def display_balance(self):
        """
        Displays the current available balance.
        """
        print(f"Current available balance: ${self.balance:.2f}")

    def display_all_portfolios(self):
        """
        Lists all existing portfolios.
        """
        if not self.portfolios:
            print("No portfolios have been created yet.")
            return

        print("Existing portfolios:")
        for portfolio_name in self.portfolios:
            print(f"- {portfolio_name}")

    def display_portfolio(self, portfolio_name):
        """
        Shows the details (stocks and number of shares) of a specified portfolio.
        """
        if portfolio_name not in self.portfolios:
            print(f"Portfolio '{portfolio_name}' does not exist.")
            return
        
        print(f"Portfolio '{portfolio_name}' details:")
        stock_data = self.portfolios[portfolio_name]
        if not stock_data:
            print("  (This portfolio has no stocks yet.)")
        else:
            for stock_symbol, shares_owned in stock_data.items():
                print(f"  - Stock: {stock_symbol}, Shares Owned: {shares_owned}")


def main():
    manager = StockPortfolioManager()

    while True:
        print("\n--- Stock Portfolio Manager ---")
        print("1. Add new portfolio")
        print("2. Add stock to portfolio")
        print("3. Buy shares")
        print("4. Sell shares")
        print("5. Deposit money")
        print("6. Withdraw money")
        print("7. Display available balance")
        print("8. Display all portfolios")
        print("9. Display a specific portfolio")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            portfolio_name = input("Enter new portfolio name: ")
            manager.add_portfolio(portfolio_name)
        elif choice == '2':
            portfolio_name = input("Enter portfolio name: ")
            stock_symbol = input("Enter stock symbol: ")
            try:
                initial_shares = int(input("Enter initial number of shares: "))
            except ValueError:
                print("Error: Please enter a valid integer for shares.")
                continue
            manager.add_stock(portfolio_name, stock_symbol, initial_shares)
        elif choice == '3':
            portfolio_name = input("Enter portfolio name: ")
            stock_symbol = input("Enter stock symbol: ")
            try:
                shares_to_buy = int(input("Enter number of shares to buy: "))
                price_per_share = float(input("Enter price per share: "))
            except ValueError:
                print("Error: Please enter valid numbers for shares and price.")
                continue
            manager.buy_shares(portfolio_name, stock_symbol, shares_to_buy, price_per_share)
        elif choice == '4':
            portfolio_name = input("Enter portfolio name: ")
            stock_symbol = input("Enter stock symbol: ")
            try:
                shares_to_sell = int(input("Enter number of shares to sell: "))
                price_per_share = float(input("Enter price per share: "))
            except ValueError:
                print("Error: Please enter valid numbers for shares and price.")
                continue
            manager.sell_shares(portfolio_name, stock_symbol, shares_to_sell, price_per_share)
        elif choice == '5':
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Error: Please enter a valid number for the amount.")
                continue
            manager.deposit_money(amount)
        elif choice == '6':
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Error: Please enter a valid number for the amount.")
                continue
            manager.withdraw_money(amount)
        elif choice == '7':
            manager.display_balance()
        elif choice == '8':
            manager.display_all_portfolios()
        elif choice == '9':
            portfolio_name = input("Enter portfolio name: ")
            manager.display_portfolio(portfolio_name)
        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")


# This line makes the script automatically run the main function if executed directly.
if __name__ == "__main__":
    main()
