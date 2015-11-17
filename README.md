Developing a website to view/share photos with the family.

Technology Stack:
- Other
  - libmysqlclient-dev
  - python-dev
  - libjpeg-dev
- Python 2.7
  - Pillow
  - mysql-python
- Django
- MySQL Server
- Vagrant/Virtual Box

Currently using a 32bit Ubuntu(Trusty) for development. Will need to install vagrant and virtualbox to run VM.

Add VM to local vagrant repository
```
$ vagrant box add trusty32 https://atlas.hashicorp.com/ubuntu/boxes/trusty32/versions/20151105.0.0/providers/virtualbox.box
```

Build / Provision / Start VM
```
$ vagrant up
```

The following are some steps to do for a new build:
```
# Create Database
$ python /vagrant/family_site/manage.py migrate

# Create Admin (Super) User
$ python /vagrant/family_site/manage.py createsuperuser

# Determine IP of new Vagrant VM
$ ifconfig

# Modify the configuration files to match environment
$ ls -1 config/*
config/HOST
config/MEDIA_ROOT
config/PORT

# Start the runserver (IP should match from previous step)
$ python manage.py runserver 10.0.0.11:8000
```



