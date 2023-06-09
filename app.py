from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        pincode = request.form['pincode']
        address = request.form['address']
        message = request.form['message']

        # Perform further processing with the form data
        # ...

        return f"Booking successful!<br>Name: {name}<br>Mobile: {mobile}<br>Pincode: {pincode}<br>Address: {address}<br>Message: {message}"

    return render_template('book.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#/home/Thanisia/mysite/flask_app.py