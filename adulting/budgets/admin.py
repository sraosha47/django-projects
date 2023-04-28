from django.contrib import admin

from .models import Budget, Category, Entry

# Register your models here.
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Entry)