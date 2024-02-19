# Mortgage Repayment Calculator

This is a simple mortgage repayment calculator built using Django, a Python web framework. It allows users to calculate their monthly mortgage payments based on the loan amount, interest rate, and loan term.

## Features

- Calculate monthly mortgage payments.
- Django form validation to ensure input data integrity.
- Easy-to-use interface.

## Installation

Firstly ensure that you have Python installed. Then follow the instructions below starting with cloning the repository:

```cmd
$ git clone https://github.com/RDrohan/mortgage-calculator-app.git
$ cd mortgage-calculator-app
```

Create a virtual environment to install dependencies in and activate it:

```cmd
$ py -m venv .venv
$ .venv/Scripts/activate
```

Then install the dependencies:

```cmd
(.venv)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```cmd
(.venv)$ cd project
(.venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
