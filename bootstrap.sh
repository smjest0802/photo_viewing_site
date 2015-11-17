#/usr/bin/env bash

apt-get update

# Set default password once and use everywhere
default_password="changeme"

# Install generic tools
echo "Installing initial tools"
sudo apt-get install -y python-pip

# Install mySQL Server
echo "Installing mySQL Server"
echo mysql-server mysql-server/root_password password ${default_password} | sudo debconf-set-selections
echo mysql-server mysql-server/root_password_again password ${default_password} | sudo debconf-set-selections
sudo apt-get install -y mysql-server

# Harden mySQL (Pieces from mysql_secure_installation)
echo "Hardening mySQL Install"
mysql -u root -p"${default_password}" -e "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1')"
mysql -u root -p"${default_password}" -e "DELETE FROM mysql.user WHERE User=''"
mysql -u root -p"${default_password}" -e "DELETE FROM mysql.db WHERE Db='test' OR Db='test\_%'"
mysql -u root -p"${default_password}" -e "FLUSH PRIVILEGES"

# Python Configuration
echo "Installing Django pieces"
sudo easy_install django
sudo apt-get install -y libmysqlclient-dev
sudo apt-get install -y python-dev
sudo pip install mysql-python
sudo apt-get install -y libjpeg-dev # Needed to install Pillow on Ubuntu
sudo pip install pillow # Needed for Django image fields

# MySQL setup for project
echo "MySQL setup for project"
mysql -u root -p"${default_password}" -e "CREATE DATABASE family CHARACTER SET utf8"
mysql -u root -p"${default_password}" -e "create user 'family'@'localhost'"
mysql -u root -p"${default_password}" -e "set password for 'family'@'localhost' = PASSWORD('${default_password}')"
mysql -u root -p"${default_password}" -e "grant all on family.* to 'family'"

# Add '.my.cnf' to vagrant home directory
echo "Creating '.my.cnf' for user family"
cnf_file="/home/vagrant/.my.cnf"
sudo touch $cnf_file

# File created by root, change to be owned by vagrant
sudo chown vagrant:vagrant $cnf_file

echo "[client]" >> $cnf_file
echo "database=family" >> $cnf_file
echo "user=family" >> $cnf_file
echo "password=\"${default_password}\"" >> $cnf_file
echo "host=localhost" >> $cnf_file
echo "default-character-set = utf8" >> $cnf_file
echo "" >> $cnf_file
echo "[mysql]" >> $cnf_file
echo "database=family" >> $cnf_file
echo "user=family" >> $cnf_file
echo "password=\"${default_password}\"" >> $cnf_file
echo "host=localhost" >> $cnf_file
echo "default-character-set = utf8" >> $cnf_file
echo "" >> $cnf_file
echo "[mysqladmin]" >> $cnf_file
echo "database=family" >> $cnf_file
echo "user=family" >> $cnf_file
echo "password=\"${default_password}\"" >> $cnf_file
echo "host=localhost" >> $cnf_file
echo "default-character-set = utf8" >> $cnf_file

# Create Media directories
echo "Creating media directories"
sudo mkdir -p /share/pictures_for_site/media
sudo chown -R vagrant:vagrant /share
