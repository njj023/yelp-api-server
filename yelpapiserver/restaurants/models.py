from django.db import models

class Location(models.Model):
	id = models.IntegerField(primary_key = True)
 	name = models.CharField(max_length = 500)

 	def __unicode__(self):
 		return self.name

class Restaurant(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 500)
	rating = models.DecimalField(decimal_places = 1, max_digits = 2)
	location = models.ForeignKey(Location)

	def __unicode__(self):
 		return self.name
