from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Expenses


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Expenses
		fields = ['title', 'category', 'amount']
