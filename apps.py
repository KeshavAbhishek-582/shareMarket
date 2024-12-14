import tkinter as tk

def calculate_profit_loss():
    try:
        # Get basic user inputs
        total_shares = entry_shares.get().strip()
        average_price = entry_average_price.get().strip()
        current_ltp = entry_ltp.get().strip()

        # Validate inputs
        if not total_shares or not average_price or not current_ltp:
            result_label.config(text="Please fill all required fields.")
            return

        total_shares = float(total_shares)
        average_price = float(average_price)
        current_ltp = float(current_ltp)

        # Calculate total investment and current value
        total_investment = total_shares * average_price
        current_investment_value = total_shares * current_ltp

        # Calculate profit/loss
        profit_or_loss = current_investment_value - total_investment
        profit_or_loss_percentage = (profit_or_loss / total_investment) * 100

        # Display profit/loss results
        if profit_or_loss >= 0:
            result_label.config(text=f"Profit: ₹{profit_or_loss:.2f} | Profit Percentage: {profit_or_loss_percentage:.2f}%")
        else:
            result_label.config(text=f"Loss: ₹{-profit_or_loss:.2f} | Loss Percentage: {-profit_or_loss_percentage:.2f}%")

        total_investment_label.config(text=f"Total Investment: ₹{total_investment:.2f}")

        # Automatically proceed to calculate new averages
        calculate_new_average_prices(total_shares, average_price)

    except ValueError:
        result_label.config(text="Please enter valid numerical values.")

def calculate_new_average_prices(current_shares, current_average_price):
    try:
        # Collect additional inputs for new shares and prices
        results = []
        for i in range(5):
            new_shares = additional_shares[i].get().strip()
            new_price = additional_prices[i].get().strip()

            # Skip empty inputs
            if not new_shares or not new_price:
                continue

            new_shares = float(new_shares)
            new_price = float(new_price)

            # Calculate new average price
            total_shares = current_shares + new_shares
            total_investment = (current_shares * current_average_price) + (new_shares * new_price)
            new_average_price = total_investment / total_shares
            results.append(f"Set {i+1}: New Avg Price: ₹{new_average_price:.2f}")

        # Display results
        if results:
            new_avg_price_label.config(text="\n".join(results))
        else:
            new_avg_price_label.config(text="No additional inputs provided for new shares and prices.")

    except ValueError:
        new_avg_price_label.config(text="Please enter valid numerical values for additional shares and prices.")

# Create the GUI
root = tk.Tk()
root.title("Investment Calculator")

# Input fields for current shares, average price, and LTP
tk.Label(root, text="Total Shares:").grid(row=0, column=0, padx=10, pady=5)
entry_shares = tk.Entry(root)
entry_shares.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Average Price:").grid(row=1, column=0, padx=10, pady=5)
entry_average_price = tk.Entry(root)
entry_average_price.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Current LTP:").grid(row=2, column=0, padx=10, pady=5)
entry_ltp = tk.Entry(root)
entry_ltp.grid(row=2, column=1, padx=10, pady=5)

# Input fields for additional shares and prices
tk.Label(root, text="Add New Shares and Prices:").grid(row=3, column=0, columnspan=2, pady=10)
additional_shares = []
additional_prices = []

for i in range(5):
    tk.Label(root, text=f"Set {i+1} - Shares:").grid(row=4+i, column=0, padx=10, pady=5)
    share_entry = tk.Entry(root)
    share_entry.grid(row=4+i, column=1, padx=10, pady=5)
    additional_shares.append(share_entry)

    tk.Label(root, text=f"Set {i+1} - Price:").grid(row=4+i, column=2, padx=10, pady=5)
    price_entry = tk.Entry(root)
    price_entry.grid(row=4+i, column=3, padx=10, pady=5)
    additional_prices.append(price_entry)

# Buttons
tk.Button(root, text="Calculate", command=calculate_profit_loss).grid(row=9, column=0, columnspan=2, pady=20)

# Labels to display results
total_investment_label = tk.Label(root, text="")
total_investment_label.grid(row=10, column=0, columnspan=4, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=4, pady=5)

new_avg_price_label = tk.Label(root, text="")
new_avg_price_label.grid(row=12, column=0, columnspan=4, pady=5)

# Start the GUI event loop
root.mainloop()