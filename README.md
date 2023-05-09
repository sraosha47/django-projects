# django-projects

## A brave new world

I started this repository for a school project. I basically have to create a three tier application. 
I asked some friends who are actual developers which languages and frameworks I should use. I ignored them all and chose Django. 
Mainly because I prefer Python to JavaScript or any derivatives of it.

I like it so far and have learned a lot. So I might continue creating new apps for my first project 'Adultung', 
or I might even start with some new Django projects. Who knows.

## Projects

### [Adulting](https://github.com/sraosha47/django-projects/tree/main/adulting)

A project offering apps that help with all the tedious, boring stuff that comes with adulthood. You know...responsibilities.
So far it conains following apps:


#### [Users](https://github.com/sraosha47/django-projects/tree/main/adulting/users)

This app handles the creation of new users, logging in, logging out, and viewing and edditing ones own account. 
It also allows superusers to see and edit other accounts and create new superusers.


#### [Budgets](https://github.com/sraosha47/django-projects/tree/main/adulting/budgets)
An app allowing the creation of budgets with categories and entries. Each budget cointains a description/name, initial funds, and start and end date.
They're linked to freely creatable categories which are linked to entries, which are accompanied with costs.

So far it is view only though. It shows manually created budgets with categories and entries and also shows the costs and current savings. The views handling the creation of new, and the editing of existing budgets aren't implemented yet.
