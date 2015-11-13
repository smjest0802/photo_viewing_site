# photo_viewing_site
Django developed photo viewing site


Setup Instructions after build:
Create Database:
    $ python /vagrant/family_site/manage.py migrate

Create Admin (Super) User:
    $ python /vagrant/family_site/manage.py createsuperuser

Determine IP of vagrant VM:
    $ ifconfig

Change the settings file to match the IPAddress/Host

Start runserver with IP:
    $ python manage.py runserver 10.0.0.11:8000



