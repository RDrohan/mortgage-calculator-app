from django.shortcuts import render
from .forms import MortgageCalculatorForm

def calculate_monthly_payment(loan_amount, interest_rate, loan_term_years):
    monthly_interest_rate = interest_rate / 12 / 100
    total_payments = loan_term_years * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    return round(monthly_payment, 2)

def mortgage_calculator_view(request):
    if request.method == 'POST':
        form = MortgageCalculatorForm(request.POST or None)
        if form.is_valid():
            loan_amount = form.cleaned_data['loan_amount']
            interest_rate = form.cleaned_data['interest_rate']
            loan_term_years = form.cleaned_data['loan_term_years']
            
            monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term_years)
            # Render result
            return render(request, 'mortgage_calculator/result.html', {
                'monthly_payment': monthly_payment,
                'loan_amount':  loan_amount,
                'interest_rate': interest_rate,
                'loan_term_years': loan_term_years
            })
    else:
        form = MortgageCalculatorForm()
    
    return render(request, 'mortgage_calculator/form.html', {'form': form})