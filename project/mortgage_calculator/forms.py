from django import forms
from .models import MortgageCalculator

class MortgageCalculatorForm(forms.ModelForm):
  class Meta:
    model = MortgageCalculator
    fields = ['loan_amount', 'interest_rate', 'loan_term_years']
    
  def clean_loan_amount(self, *args, **kwargs):
    loan_amount = self.cleaned_data.get('loan_amount')
    if loan_amount is None:
      raise forms.ValidationError("You must enter a loan amount")
    return loan_amount
    
  def clean_interest_rate(self, *args, **kwargs):
    interest_rate = self.cleaned_data.get('interest_rate')
    if interest_rate is None:
      raise forms.ValidationError("You must enter an interest_rate")
    return interest_rate
    
  def clean_loan_term_years(self, *args, **kwargs):
    loan_term_years = self.cleaned_data.get('loan_term_years')
    if loan_term_years is None:
      raise forms.ValidationError("You must enter a loan term")
    if loan_term_years < 10 or loan_term_years > 40:
      raise forms.ValidationError("You must enter a loan term between 10 and 40 years")
    return loan_term_years