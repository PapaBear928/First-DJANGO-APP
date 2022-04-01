from django.forms import ModelForm
from .models import Expenses, Categories, Descript


class ExpensesForm(ModelForm):
	class Meta:
		model = Expenses
		fields = ['title',  'amount', 'description', 'date_of_introduction', 'date_of_payment', 'unexpected', 'bills_photo']


class CategoriesForm(ModelForm):
	class Meta:
		model = Categories
		fields = ['categories']


class DescriptForm(ModelForm):
	class Meta:
		model = Descript
		fields = ['extra_description']


'''class WhereToPaidForm(ModelForm):
	class Meta:
		model = WhereToPaid
		fields = ['where']'''
