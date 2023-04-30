from django.contrib import admin

from .models import Budget, Category, Entry

# Register your models here.
class CategoryInLine(admin.TabularInline):
    model = Category
    extra = 3

class EntryInLine(admin.TabularInline):
    model = Entry
    extra = 3

class BudgetAdmin(admin.ModelAdmin):
    list_display = ["budget_text", "owner" ]
    fieldsets = [
        ("Description", {"fields": ["owner", "budget_text"]}),
        ("Funds", {"fields": ["funds"]}),
        ("Timeperiod", {"fields": ["start_date", "end_date"]})
    ]
    inlines = [CategoryInLine]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_text", "budget"]
    fieldsets = [
        (None, {"fields": ["budget", "category_text"]})
    ]
    inlines = [EntryInLine]

admin.site.register(Budget, BudgetAdmin)
admin.site.register(Category, CategoryAdmin)
