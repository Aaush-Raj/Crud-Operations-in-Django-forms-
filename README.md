# Crud-Operations-in-Django-forms-
In this Django Project I've created a Form(Employee Register form) with Create,Read,Update,and Delete (CRUD) features. 
You can Add New Details to the Database , Edit saved data, Delete any data from Database and you can view all data on the Front end page.

# DJANGO APP & TEMPLATES :
I've created an APP (Employee Register) within it , I've created 3 Template files for the HTML structure:
          i.base.html - This is the base of all other files, I've done Template inheritance with this. In this all CSS(inline and downloaded) , Javascript with Bootstrap is uploaded. I've created a Jumbotron container in this for all the content.
         ii.employee_form.html - In this file I've created Form Structure and Submit button.
        iii. employee_list.html - In this I've created the structure of the list , which will be shown after you submit the form. This is the list of all other Employees who have registered before you.
  
# FORM :
For this project , I haven't used any ordinary html form ...instead I've used Django's Form feature i.e 'crispy_forms'.
first you have to install 'crispy_forms' into your Django settings before using.
My form Consist of : Name , Mobile , Emp_code & Position.
- Whenever you fill the form and submit it , it will get saved in the DataBase.

# DATABASE :
Although Django provides you default Database of SQL , The database I've used here is PostgreSQL.

for Using Postgresql as your database -
   i. You have to download Postgresql and Create a profile and Password ,then
  ii. You have to make following changes into your Database settings(under settings.py) ->
  ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'postgres',
        'USER':'postgres',
        'PASSWORD': '@rajaayush1234@',
        'HOST':'localhost',
        'PORT':'5432',

    }
}
  ```
--AAUSH RAJ
aayushcontactinfo@gamil.com

                    
  
