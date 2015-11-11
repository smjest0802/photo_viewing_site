#/usr/bin/env bash

apt-get update

# Set default password once and use everywhere
default_password="changeme"

# Install PIP
#sudo apt-get install -y python-pip

# Install mySQL Server
#sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password ${default_password}'
echo mysql-server mysql-server/root_password password ${default_password} | sudo debconf-set-selections
#sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password ${default_password}'
echo mysql-server mysql-server/root_password_again password ${default_password} | sudo debconf-set-selections
sudo apt-get install -y mysql-server
#mysql_secure_installation

# Python Configuration
#easy_install django
#sudo apt-get install libmysqlclient-dev
#sudo apt-get install python-dev
#pip install mysql-python

#Configure
#useradd -m -p $default_password -s /bin/bash family
