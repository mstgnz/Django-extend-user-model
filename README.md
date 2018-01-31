# Expand User Model

> Django user model is expanded and the only difference in the original 
> version is that you are in the right place to login with extra fields and e-mail.

* First we create an application called 'account'. You can give it a different name. the terminal;

`python3 manage.py startapp account`

* You can copy the contents of the admin.py and models.py files of the 'account' application you created above.
* We are making settings for the 'account' application in the settings.py file.
* We are writing the application we created in the INSTALLED_APPS section.

`INSTALLED_APPS = [
    ....
    'account',
]`
* In the Settings.py file we need to identify our User model. To do this, paste the code below at where you want.

`AUTH_USER_MODEL = 'account.User'`
* From the terminal screen, we can no longer pass the application. Respectively;

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

`email : blablabla@blabla.com`

`password : 123456`

`python3 manage.py runserver`

> When you log in to the Admin panel, you will see that the only 
> difference from the original django user model is the extra 
> space you have entered and the login with the email system.
