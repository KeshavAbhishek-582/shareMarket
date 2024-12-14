from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve form data
        total_shares = request.form.get('total_shares', '').strip()
        average_price = request.form.get('average_price', '').strip()
        current_ltp = request.form.get('current_ltp', '').strip()

        if not total_shares or not average_price or not current_ltp:
            return jsonify({'error': 'Please fill all required fields.'})

        total_shares = float(total_shares)
        average_price = float(average_price)
        current_ltp = float(current_ltp)

        # Calculate total investment and current value
        total_investment = total_shares * average_price
        current_investment_value = total_shares * current_ltp

        # Calculate profit/loss
        profit_or_loss = current_investment_value - total_investment
        profit_or_loss_percentage = (profit_or_loss / total_investment) * 100

        result = {
            'total_investment': f'Total Investment: ₹{total_investment:.2f}',
            'profit_or_loss': f"{'Profit' if profit_or_loss >= 0 else 'Loss'}: ₹{abs(profit_or_loss):.2f}",
            'percentage': f"{'Profit' if profit_or_loss >= 0 else 'Loss'} Percentage: {abs(profit_or_loss_percentage):.2f}%"
        }

        # Calculate new averages for additional shares/prices
        new_averages = []
        for i in range(1, 6):
            new_shares = request.form.get(f'set_{i}_shares', '').strip()
            new_price = request.form.get(f'set_{i}_price', '').strip()

            if new_shares and new_price:
                new_shares = float(new_shares)
                new_price = float(new_price)

                total_shares += new_shares
                total_investment += new_shares * new_price
                new_average_price = total_investment / total_shares
                new_averages.append(f"Set {i}: New Avg Price: ₹{new_average_price:.2f}")

        result['new_averages'] = new_averages
        return jsonify(result)

    except ValueError:
        return jsonify({'error': 'Please enter valid numerical values.'})

if __name__ == '__main__':
    app.run(debug=True)