from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Expenses, Categories, Descript
from .forms import ExpensesForm, CategoriesForm, DescriptForm
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializers import ExpenseSerializer


class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ExpenseView(viewsets.ModelViewSet):
	queryset = Expenses.objects.all()
	serializer_class = ExpenseSerializer


def all_expenses(request):
	all_exp = Expenses.objects.all()
	return render(request, 'Expenses.html', {'expenses': all_exp})


@login_required
def new_expense(request):
	Exp_form = ExpensesForm(request.POST or None, request.FILES or None)
	Cat_form = CategoriesForm(request.POST or None)

	if all((Exp_form.is_valid(), Cat_form.is_valid())):
		expenses = Exp_form.save(commit=False)
		cat = Cat_form.save()
		expenses.category = cat
		expenses.save()
		return redirect(all_expenses)

	return render(request, 'expense_form.html', {'form': Exp_form, 'xtraform': None, 'xtra': None,
	                                             'catform': Cat_form, 'new': True})


@login_required
def edit_your_expenses(request, id):
	expense = get_object_or_404(Expenses, pk=id)
	xtra = Descript.objects.filter(expense=expense)

	try:
		categories = Categories.objects.get(expenses=expense.id)
	except Categories.DoesNotExist:
		categories = None

	Exp_form = ExpensesForm(request.POST or None, request.FILES or None, instance=expense)
	Cat_form = CategoriesForm(request.POST or None, instance=categories)
	Xtra_form = DescriptForm(request.POST or None)

	if request.method == 'POST':
		if 'extra_descript' in request.POST:
			xtra = Xtra_form.save(commit=False)
			xtra.Descript = Descript
			xtra.save()

	if all((Exp_form.is_valid(), Cat_form.is_valid())):
		expenses = Exp_form.save(commit=False)
		cat = Cat_form.save()
		expenses.category = cat
		expenses.save()
		return redirect(all_expenses)

	return render(request, 'expense_form.html', {'form': Exp_form, 'catform': Cat_form,
	                                             'xtraform': Xtra_form, 'xtra': xtra, 'new': False})


@login_required
def delete_your_expenses(request, id):
	expense = get_object_or_404(Expenses, pk=id)

	if request.method == "POST":
		expense.delete()
		return redirect(all_expenses)

	return render(request, 'confirm.html', {'expense': expense})