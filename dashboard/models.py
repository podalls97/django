from django.db import models

class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    date = models.DateField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"
