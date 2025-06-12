# django-projects

## A brave new world

I started this repository for a school project. I basically have to create a three tier application. 
I asked some friends who are actual developers which languages and frameworks I should use. I ignored them all and chose Django. 
Mainly because I prefer Python to JavaScript or any derivatives of it.

I like it so far and have learned a lot. So I might continue creating new apps for my first project 'Adulting', 
or I might even start with some new Django projects. Who knows.

## Projects

### [Adulting](https://github.com/sraosha47/django-projects/tree/main/adulting)

A project offering apps that help with all the tedious, boring stuff that comes with adulthood. You know...responsibilities.
So far it contains following apps:


#### [Users](https://github.com/sraosha47/django-projects/tree/main/adulting/users)

This app handles the creation of new users, logging in, logging out, and viewing and edditing ones own account. 
It also allows superusers to see and edit other accounts and create new superusers.

It contains following views:
* Index - Leads to the main page one sees, after logging in. Otherwise it leads back to the login page.
* Login - handles authentication, logs the user in and then redirects to the index.
* Logout - logs out and redirects to the login.
* register - leads to a page that let's someone create a new account.
* newuser - leads to a page letting admins create a new account.
* create - creates new account and redirects back to the register page.
* change - handles changes made on the account page and redirects to the index.
* account - shows information about the users account. Also allows superusers to see all accounts and edit them. Should be changed, so only the password can be reset.



#### [Budgets](https://github.com/sraosha47/django-projects/tree/main/adulting/budgets)
An app allowing the creation of budgets with categories and entries. Each budget cointains a description/name, initial funds, and start and end date.
They're linked to freely creatable categories which are linked to entries, which are accompanied with costs.

So far it is view only though. It shows manually created budgets with categories and entries and also shows the costs and current savings. The views handling the creation of new, and the editing of existing budgets aren't implemented yet. The calculations of costs and savings needed some additional Django tags which can be found under [budgets_extras.py](https://github.com/sraosha47/django-projects/blob/main/adulting/budgets/templatetags/budgets_extras.py).

It contains following views:
* Index - Shows a list of the users budgets
* Categories - Detail view of a budgets categories
* Entries - Detail view of a categories entries
