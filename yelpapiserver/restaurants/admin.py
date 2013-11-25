from django.contrib import admin
from yelpapiserver.restaurants import models

# Register our models with the admin interface
admin.site.register(models.Location)
admin.site.register(models.Restaurant)