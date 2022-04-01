from django.contrib import admin
from django.urls import path
from RedPandaExpenses.views import all_expenses, new_expense, edit_your_expenses, delete_your_expenses


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('all_expenses/', all_expenses, name= "all"),
    path('new_expense/', new_expense, name= "new"),
    path('edit_your_expense/<int:id>/', edit_your_expenses, name= "edit"),
    path('delete_your_expense/<int:id>/', delete_your_expenses, name= "delete"),


]
