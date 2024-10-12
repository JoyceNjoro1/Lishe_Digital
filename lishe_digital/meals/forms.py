from django import forms
from .models import Meal

class MealPurchaseForm(forms.Form):
    meal = forms.ModelChoiceField(queryset=Meal.objects.all())
