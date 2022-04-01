from django.contrib import admin
from .models import Expenses, Categories, Descript



@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
	# fields = ['title']
	list_display = ['title', 'category', 'amount', 'date_of_payment']
	list_filter = ('title', 'category', 'amount', 'date_of_payment')
	search_fields = ('title', 'amount')


admin.site.register(Categories)
admin.site.register(Descript)
'''admin.site.register(WhereToPaid)'''