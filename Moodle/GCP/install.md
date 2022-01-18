---
title: GCP
tags: moodle
lang: zh-tw
---

{%hackmd theme-dark %}

# Moodle setup on GCP step
1. Creat a new GCP VM
    1. ![](https://i.imgur.com/MerxoUq.png)
    2. ![](https://i.imgur.com/0lHV77A.png)
    3. ![](https://i.imgur.com/682eBwz.png)
    4. ![](https://i.imgur.com/FIvyqnN.png)
    5. ![](https://i.imgur.com/frCSX6O.png)
    6. ![](https://i.imgur.com/4oeb8ne.png)
    7. ![](https://i.imgur.com/F3jweVD.png)
    8. ![](https://i.imgur.com/BQN1cUF.png)
    9. ![](https://i.imgur.com/KwYVW5v.png)
    10. ![](https://i.imgur.com/uyWG4dC.png)
    11. ![](https://i.imgur.com/ygSxFi4.png)
2. Connect using SSH([MobaXterm_Free](https://mobaxterm.mobatek.net/download.html))
    1. ![](https://i.imgur.com/mgCnBA9.png)
    2. ![](https://i.imgur.com/RtYgTBX.png)
    3. ![](https://i.imgur.com/u0BIRQE.png)
    4. ![](https://i.imgur.com/xl6nikf.png)
    5. ![](https://i.imgur.com/JqXzZNT.png)
    6. ![](https://i.imgur.com/0NBtTtO.png)
    7. ![](https://i.imgur.com/7Chi5BH.png)
    8. ![](https://i.imgur.com/dTapXNd.png)

3. Creat Moodle
    1. Update system & all package
		```shell=
		sudo yum update
		```
    2. Install apache server
    	```shell=
    	sudo yum install httpd
    	```
    3. Start httpd server
    	```shell=
    	sudo systemctl start httpd.service
    	```
    4. Install PHP7.3
        ```shell=
    	sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    	sudo dnf install -y https://rpms.remirepo.net/enterprise/remi-release-8.rpm
    	sudo dnf module list php
    	sudo dnf module enable php:remi-7.3 -y
    	```
    5. Install PHP extension
        ```shell=
    	dnf install -y php-mysqlnd php php-cli php-common php-fpm php-zip php-gd php-intl php-xmlrpc php-soap php-sodium
    	```
    6. Check version
    	```shell=
    	php -v
    	```
    7. Install mariadb
		```shell=
		sudo yum install mariadb mariadb-server
		```
    8. Start server
    	```shell=
    	sudo systemctl start mariadb
    	```
    9. Login(root)
    	```shell=
    	sudo mysql -u root -p
    	```
        > Password => Press Enter key
    10. Init mariadb
    	1. Creat database
    	    ```sql=
    	    create database YourDataBaseName;
    	    ```
    	2. Creat user
    	    ```sql=
    	    CREATE USER 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	3. Add permission
    		```sql=
    		GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	4. Reload the grant tables(授權表)
    	    ```sql=
    	    FLUSH PRIVILEGES;
    	    ```
        5. Logout mysql
            ```sql=
            quit
            ```
    11. Open selinux config
    	```shell=
    	sudo vim /etc/selinux/config
    	```
    12. Chang enforcing SELinux to disable
    	```shell=
    	SELINUX=enforcing
    	      to
    	SELINUX=disable
    	```
    13. Download
	    - [download.moodle.org](https://download.moodle.org/releases/latest/)
	    1. Install wget
	        ```shell=
	        sudo yum install wget
	        ```
	    2. Go to /var/www/html
	        ```shell=
	        cd /var/www/html
	        ```
	    3. Download moodle package
	        ```shell=
	    	sudo wget https://download.moodle.org/download.php/direct/stable311/moodle-3.11.4.tgz
	        ```
	    4. Install tar command
	        ```shell=
	        sudo yum install tar
	        ```
	    5. Decompression 
	        ```shell=
	        sudo tar -zxvf moodle-3.11.4.tgz
	        ```
    14. Creat moodledata directory（Can't creat on /var/www/html）
    	```shell=
    	sudo mkdir /your_path/moodledata
    	```
	15. Change folder permission
		```shell=
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
5. Login moodle
    1. Connect to [http://35.236.165.53/moodle/](http://35.236.165.53/moodle/)
    2. ![](https://i.imgur.com/VyPIdzH.png)
    3. ![](https://i.imgur.com/U9UnsQf.png)

# Upload video to Moodle
1. Change post max size
    1. Edit php.ini (Because Moodle is written in PHP)
        ```shell=
        sudo vim /etc/php.ini
        ```
    2. Press `/` key
        ![](https://i.imgur.com/5essm9s.png)
    3. Enter `post_max` and press `Enter` key
        ![](https://i.imgur.com/EAg6NAB.png)
    4. You can see this config and specific a size you want
        ![](https://i.imgur.com/ZSuYlpN.png)
        ```ini=
        post_max_size = [size + unit]
        # KB => K, MB => M, GB => G
        ```
    5. Save your change
        1. Press `:`
        2. Enter `wq`
        3. Press `Enter` key
        ![](https://i.imgur.com/es0Oor9.png)
    6. Reboot your VM
        ```shell=
        sudo reboot
        ```
2. ![](https://i.imgur.com/OTaOCaw.png)
3. ![](https://i.imgur.com/5QHLicy.png)
4. ![](https://i.imgur.com/McZ3UNX.png)
5. ![](https://i.imgur.com/8BMjPbw.png)
6. ![](https://i.imgur.com/SdZJ0Ht.png)
7. ![](https://i.imgur.com/WWFYi1H.png)
8. ![](https://i.imgur.com/pUQKOaV.png)
9. ![](https://i.imgur.com/xjnavhO.png)
10. ![](https://i.imgur.com/GlyiAHx.png)
11. ![](https://i.imgur.com/hbSigjj.png)

# Types
### Others
- ifconfig command not found
    ```shell=
    sudo yum install net-tools
    ```

### Apache
- [virtualhost_example](https://httpd.apache.org/docs/2.4/vhosts/examples.html)
- Creat Virtualhost
    ```shell=
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
    ```shell=
    sudo systemctl status httpd.service
    ```

### php 7.3
- Verify php-mysqlnd
    ```shell=
    php -m | grep -i mysql
    ```
### mariadb
- Reset admin password
    - Login(root)
        ```shell=
        sudo mysql -u root -p
        ```
    - Select your database
        ```sql=
        use moodle;
        ```
    - Change your user's password
    	```sql=
    	UPDATE mdl_user SET password=MD5('admin') WHERE username='admin';
        ```

### moodle
- If you want download moodle-3.11.4.zip
    ```shell=
	sudo wget https://download.moodle.org/download.php/direct/stable311/moodle-3.11.4.zip
	```
    - Install unzip command
        ```shell=
        sudo yum install unzip
        ```
    - Decompression
        ```shell=
        sudo unzip filename.zip
        ```

### CentOS Stream 9
- Install php
    ```shell=
    sudo yum install php
    ```
- Can't install many php extension in one line
    ```shell=
    dnf install -y php-mysqlnd php php-cli php-common php-fpm php-zip php-gd php-intl php-xmlrpc php-soap php-sodium
    ```