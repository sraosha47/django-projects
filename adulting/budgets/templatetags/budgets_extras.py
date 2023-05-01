from django import template
from budgets.models import Budget, Category, Entry

register = template.Library()

@register.filter(name='get_item') 
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag
def get_budget_costs(budget):
    costs = 0
    category_list= Category.objects.filter(budget_id=budget.id)
    for category in category_list:
        entry_list = Entry.objects.filter(category_id=category.id)
        for entry in entry_list:
            costs += entry.costs
    return costs

@register.simple_tag
def get_category_costs(category):
    costs = 0
    entry_list= Entry.objects.filter(category_id=category.id)
    for entry in entry_list:
        costs += entry.costs
    return costs


@register.simple_tag
def get_savings(budget):
    savings = budget.funds
    costs = 0
    category_list= Category.objects.filter(budget_id=budget.id)
    for category in category_list:
        entry_list = Entry.objects.filter(category_id=category.id)
        for entry in entry_list:
            costs += entry.costs
    savings -= costs
    return savings
