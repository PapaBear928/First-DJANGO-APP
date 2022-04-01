from django.db import models


#class one to one
class Categories(models.Model):

	CHOICES = {
		(1, 'Grocery'),
		(2, 'Unexpected'),
		(3, 'Administrative fees'),
		(4, 'Means of transport'),
		(5, 'Bills'),
		(6, 'Other'),
	}
	categories = models.PositiveSmallIntegerField(default=6, choices=CHOICES)


class Expenses(models.Model):

	title = models.CharField(max_length=64, null=True, blank=False)
	category = models.OneToOneField(Categories, on_delete=models.CASCADE, null=True, blank=True, unique=False)
	amount = models.DecimalField(max_digits=7, decimal_places=2, blank=False, default=0.00)
	description = models.TextField(default="Short description. Maximum 100 signs", max_length=100, null=True)
	date_of_introduction = models.DateField(null=True, blank=True)
	date_of_payment = models.DateTimeField(null=True, blank=True)
	unexpected = models.BooleanField(blank=True, default=None)
	bills_photo = models.ImageField(upload_to="saved bills pics", null=True, blank=True)

	def __str__(self):
		return self.new_title()

	def new_title(self):
		return "Title:{}, Category:{}".format(self.title, self.category)


# Many to one
class Descript(models.Model):
	extra_description = models.TextField(default="Maximum 600 signs", max_length=600, blank=True, null=True)
	expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)


'''# Many to many
class WhereToPaid(models.Model):
	name = models.CharField(max_length=100, default="Where have you paid?")
	payments = models.ManyToManyField(Expenses, related_name="where")'''