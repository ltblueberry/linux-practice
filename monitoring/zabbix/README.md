# zabbix

## Install nginx

Add nginx repository
```
sudo yum install epel-release
```

Install nginx
```
sudo yum install nginx
```

Start service
```
sudo systemctl start nginx
sudo systemctl enable nginx
```

## Install MariaDB

```
sudo yum install mariadb-server mariadb
```

Start service
```
sudo systemctl start mariadb
sudo systemctl enable mariadb
```
 
Run security script (Leave it blank, if you've just installed MariaDB)
```
sudo mysql_secure_installation
```

## Install PHP-FPM

Add popular repository with php up-to-date php releases
```
sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
```

Enable remi package with php
```
yum --disablerepo="*" --enablerepo="remi-safe" list php[7-9][0-9].x86_64

sudo yum-config-manager --enable remi-php74
```

Install php
```
sudo yum install php php-mysqlnd php-fpm
```

Change php-fpm configuration
```
$ sudo vim /etc/php-fpm.d/www.conf

# User group
user = nginx
group = nginx

# Listen on socket file
listen = /var/run/php-fpm/php-fpm.sock;

listen.owner = nginx
listen.group = nginx
listen.mode = 0660
```

Start service
```
sudo systemctl start php-fpm
sudo systemctl enable php-fpm
```