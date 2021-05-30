from app.hist_app import hist
from flask import render_template, request, redirect, url_for
from app.forms import NewPositionForm


@hist.route("/", methods=['POST', 'GET'])
def index():
    form = NewPositionForm()
    if request.method == 'POST':
        date_time = request.form['date_time']
        instrument = request.form['instrument']
        amount = request.form['amount']
        portfolio = request.form['portfolio']
        print(date_time, instrument, amount, portfolio)
        return redirect(url_for('portfolio.add_position'))
    return render_template('index.html', form=form)