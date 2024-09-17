from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

bids = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bidding', methods=['GET', 'POST'])
def bidding():
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        initial_price = float(request.form['price'])
        bids[name] = initial_price
        return redirect(url_for('next_bidder'))
    return render_template('bidding.html')

@app.route('/next_bidder', methods=['GET', 'POST'])
def next_bidder():
    if request.method == 'POST':
        next_bidder = request.form['next_bidder'].lower()
        if next_bidder == 'no':
            return redirect(url_for('statistics'))
        else:
            return redirect(url_for('bidding'))
    return render_template('next_bidder.html')

@app.route('/statistics')
def statistics():
    highest_price, middle_price = get_statistics_summary(bids)
    return render_template('statistics.html', highest_price=highest_price, middle_price=middle_price)

@app.route('/adjustment', methods=['GET', 'POST'])
def adjustment():
    if request.method == 'POST':
        name = request.form['name'].strip().lower()
        choice = request.form['choice']
        if choice == '2':
            new_price = float(request.form['new_price'])
            if bids[name] <= new_price <= bids[name] * 1.5:
                bids[name] = new_price
        return redirect(url_for('next_adjustment'))
    return render_template('adjustment.html', bids=bids)

@app.route('/next_adjustment', methods=['GET', 'POST'])
def next_adjustment():
    if request.method == 'POST':
        next_bidder = request.form['next_bidder'].lower()
        if next_bidder == 'no':
            return redirect(url_for('result'))
        else:
            return redirect(url_for('adjustment'))
    return render_template('next_adjustment.html')

@app.route('/result')
def result():
    winner_name, winner_price = get_winner(bids)
    return render_template('result.html', winner_name=winner_name, winner_price=winner_price)

def get_statistics_summary(bids):
    highest_price = max(bids.values())
    middle_price = sum(bids.values()) / len(bids)
    return highest_price, middle_price

def get_winner(bids):
    highest_price = max(bids.values())
    winner_name = max(bids, key=bids.get).title()
    return winner_name, highest_price

if __name__ == '__main__':
    app.run(debug=True)