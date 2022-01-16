---
title: Azure
tags: moodle
lang: zh-tw
---

{%hackmd theme-dark %}

# Step
1. Creat a new Azure VM
    1. ![](https://i.imgur.com/p5hsSNV.png)
    2. ![](https://i.imgur.com/s4iQOhu.png)
    3. ![](https://i.imgur.com/04QjQAc.png)
    4. ![](https://i.imgur.com/7JLI1AG.png)
    5. ![](https://i.imgur.com/SYkKYw4.png)
    6. ![](https://i.imgur.com/kaMofjg.png)
    7. ![](https://i.imgur.com/UeIgdDt.png)
    8. ![](https://i.imgur.com/0QRTPds.png)
    9. ![](https://i.imgur.com/asUTKX3.png)
    10. ![](https://i.imgur.com/f9tgzBS.png)
    11. ![](https://i.imgur.com/hRKDMt2.png)
2. Connect using SSH([MobaXterm_Free](https://mobaxterm.mobatek.net/download.html))
    1. ![](https://i.imgur.com/9wZM9IQ.png)
    2. ![](https://i.imgur.com/x97vqUB.png)
3. Creat Moodle
    1. Update system & all package
		```shell
		sudo yum update
		```
    2. Install httpd server
    	```shell
    	sudo yum install httpd
    	```
    3. Start httpd server
    	```shell
    	sudo systemctl start httpd.service
    	```
    4. Install PHP7.3
        ```shell
    	sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    	sudo dnf install -y https://rpms.remirepo.net/enterprise/remi-release-8.rpm
    	sudo dnf module list php
    	sudo dnf module enable php:remi-7.3 -y
    	```
    5. Install PHP extension
        ```shell
    	dnf install -y php-mysqlnd php php-cli php-common php-fpm php-zip php-gd php-intl php-xmlrpc php-soap php-sodium
    	```
    6. Check version
    	```shell
    	php -v
    	```
    7. Install mariadb
		```shell
		sudo yum install mariadb mariadb-server
		```
    8. Start server
    	```shell
    	sudo systemctl start mariadb
    	```
    9. Login(root)
    	```shell
    	sudo mysql -u root -p
    	```
        > Password => Press Enter key
    10. Init mariadb
    	1. Creat database
    	    ```sql
    	    create database YourDataBaseName;
    	    ```
    	2. Creat user
    	    ```sql
    	    CREATE USER 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	3. Add permission
    		```sql
    		GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	4. Reload the grant tables(授權表)
    	    ```sql
    	    FLUSH PRIVILEGES;
    	    ```
        5. Logout mysql
            ```sql
            quit
            ```
    11. Open selinux config
    	```shell
    	sudo vim /etc/selinux/config
    	```
    12. Chang enforcing SELinux to disable
    	```shell
    	SELINUX=enforcing
    	      to
    	SELINUX=disable
    	```
    13. Download
	    - [download.moodle.org](https://download.moodle.org/releases/latest/)
	    1. Install wget
	        ```shell
	        sudo yum install wget
	        ```
	    2. Go to /var/www/html
	        ```shell
	        cd /var/www/html
	        ```
	    3. Download moodle package
	        ```shell
	    	sudo wget https://download.moodle.org/download.php/direct/stable311/moodle-3.11.4.tgz
	        ```
	    4. Install tar command
	        ```shell
	        sudo yum install tar
	        ```
	    5. Decompression 
	        ```shell
	        sudo tar -zxvf moodle-3.11.4.tgz
	        ```
    14. Creat moodledata directory（Can't creat on /var/www/html）
    	```shell
    	sudo mkdir /your_path/moodledata
    	```
	15. Change folder permission
		```shell
		sudo chown -R apache:apache moodledata/
        sudo chown -R apache:apache moodle/
		```
4. Setting moodle
    1. ![](https://i.imgur.com/P3WzxUh.png)
    2. ![](https://i.imgur.com/XLxjgjZ.png)
    3. ![](https://i.imgur.com/pxfgynl.png)
    4. ![](https://i.imgur.com/PuZRAv5.png)
    5. ![](https://i.imgur.com/r94K2jP.png)
    6. ![](https://i.imgur.com/Y39E8LS.png)
    7. ![](https://i.imgur.com/GMf8E0Z.png)
    8. ![](https://i.imgur.com/7BqsE0P.png)
    9. ![](https://i.imgur.com/AwLjDLM.png)
    10. ![](https://i.imgur.com/SHM4e4k.png)
    11. ![](https://i.imgur.com/zUqWK1Q.png)

# Types
### Others
- ifconfig command not found
    ```shell
    sudo yum install net-tools
    ```

### Apache
- [virtualhost_example](https://httpd.apache.org/docs/2.4/vhosts/examples.html)
- Creat Virtualhost
    ```shell
    sudo vim /etc/httpd/conf.d/moodle.conf
    ```
- moodle.conf
    ```apache=
    <VirtualHost *:80>
	DocumentRoot "/var/www/html/"
	ServerName Your_Public_IP
    </VirtualHost>
    ```
- check server status
    ```shell
    sudo systemctl status httpd.service
    ```

### php 7.3
- Verify php-mysqlnd
    ```shell
    php -m | grep -i mysql
    ```
### mariadb
- Reset admin password
    - Login(root)
        ```shell
        sudo mysql -u root -p
        ```
    - Select your database
        ```sql
        use moodle;
        ```
    - Change your user's password
    	```sql
    	UPDATE mdl_user SET password=MD5('admin') WHERE username='admin';
        ```

### moodle
- If you want download moodle-3.11.4.zip
    ```shell
	sudo wget https://download.moodle.org/download.php/direct/stable311/moodle-3.11.4.zip
	```
    - Install unzip command
        ```shell
        sudo yum install unzip
        ```
    - Decompression
        ```shell
        sudo unzip filename.zip
        ```