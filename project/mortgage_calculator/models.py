from django.db import models

class MortgageCalculator(models.Model):
    loan_amount = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    loan_term_years = models.IntegerField()