from django.contrib import admin
from .models import Project

admin.site.register(Project)
#in admin we first import our project from models and then simply pass that to database with a simple method
# admin.site.register(your project name) this will passs your database tabale details to django database
