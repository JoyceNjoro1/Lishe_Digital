from django.shortcuts import render, get_object_or_404
from .models import Student, Transaction
from .forms import MealPurchaseForm
from .models import Student

def purchase_meal(request, qr_code):
    student = get_object_or_404(Student, qr_code=qr_code)
    if request.method == 'POST':
        form = MealPurchaseForm(request.POST)
        if form.is_valid():
            meal = form.cleaned_data['meal']
            if student.balance >= meal.price:
                # Deduct meal price from student's balance
                student.balance -= meal.price
                student.save()

                # Log the transaction
                Transaction.objects.create(student=student, meal=meal)

                return render(request, 'success.html', {'student': student, 'meal': meal})
            else:
                return render(request, 'insufficient_balance.html', {'student': student})
    else:
        form = MealPurchaseForm()
    return render(request, 'purchase_meal.html', {'form': form, 'student': student})

def students_list(request):
    students = Student.objects.all()  # Replace with the correct queryset
    return render(request, 'students_list.html', {'students': students})
