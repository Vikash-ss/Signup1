

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def create_account():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup():
    account_type = request.form.get('account_type')
    first_name = request.form.get('first_name')
    middle_name = request.form.get('middle_name')
    last_name = request.form.get('last_name')
    dob_month = request.form.get('dob_month')
    dob_year = request.form.get('dob_year')
    gender = request.form.get('gender')
    profile_name = request.form.get('profile_name')
    password = request.form.get('password')
    phone_number = request.form.get('phone_number')

    # Process the data, e.g., store it in a database or perform validation

    return "Sign up successful!"


if __name__ == '__main__':
    app.run(debug=True)


