from Flask import Flask, render_template, request

app = Flask(__name__)

customers = [
    {
        "id": 1,
        "name": "John Doe",
        "balance": 5000
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "balance": 10000
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/customers')
def view_customers():
    return render_template('customers.html', customers=customers)

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        sender_id = int(request.form['sender'])
        recipient_id = int(request.form['recipient'])
        amount = int(request.form['amount'])
        
        sender = next((c for c in customers if c['id'] == sender_id), None)
        recipient = next((c for c in customers if c['id'] == recipient_id), None)
        
        if sender and recipient and sender['balance'] >= amount:
            sender['balance'] -= amount
            recipient['balance'] += amount
            return render_template('transfer.html', success=True)
        
        return render_template('transfer.html', error=True)
    
    return render_template('transfer.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
