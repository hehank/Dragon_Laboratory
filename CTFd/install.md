---
title: CTFd initialize
tags: tags
lang: en-us
---

{%hackmd theme-dark %}

# Step
1. Creat a new GCP VM
    - same as [install.md](https://github.com/hehank/Moodle/blob/main/GCP/install.md)-Step-1.Creat a new GCP VM
        > Change picture 4. operation system & version

        ![](https://i.imgur.com/0WGo8Pk.png)
2. Connect using SSH([MobaXterm_Free](https://mobaxterm.mobatek.net/download.html))
    - same as [install.md](https://github.com/hehank/Moodle/blob/main/GCP/install.md)-Step-2.Connect using SSH(MobaXterm_Free)
        > Just IP different
3. Creat CTFd
    1. Update && upgrade
        ```shell
        sudo apt update && sudo apt dist-upgrade
        ```
    2. Install some packages that we need
        ```shell
        sudo apt install python3-pip mariadb-server libmariadbclient-dev nginx uwsgi redis-server unzip uwsgi-plugin-python3 docker docker.io
        ```
    3. Install some Python packages that we need
        ```shell
        sudo pip3 install Flask uwsgi
        ```
    4. Download CTFd
        ```shell
        cd ~
        git clone https://github.com/CTFd/CTFd.git
        ```
    5. Edit `prepare.sh`
        ```shell
        sudo vim ~/CTFd/prepare.sh
        ```
        ![](https://i.imgur.com/ryjxJSq.png)
    6. Execute `prepare.sh`
        ```shell
        sudo sh ~/CTFd/prepare.sh
        ```
    7. Edit `redis.conf`
        ```shell
        sudo vim /etc/redis/redis.conf
        ```
        ![](https://i.imgur.com/1MnRhgL.png)
    8. Setting mariadb
        1. Login mariadb by root
        	```shell
        	sudo mysql -u root -p
        	```
        2. Setting character
            ```sql
            SET character_set_server = 'latin1';
			SET character_set_results = 'utf8';
			SET character_set_filesystem = 'binary';
			SET character_set_database = 'latin1';
			SET character_set_connection = 'utf8';
			SET character_set_client = 'utf8';
            ```
        3. Check what you set
            ```sql
            SHOW VARIABLES LIKE 'character\_set\_%';
            ```
            ![](https://i.imgur.com/b5Ck3Za.png)
        4. Creat a new database
    	    ```sql
    	    create database YourDataBaseName;
    	    ```
    	5. Creat user
    	    ```sql
    	    CREATE USER 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	6. Add permission
    		```sql
    		GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' IDENTIFIED BY 'PASSWORD';
    	    ```
    	7. Reload the grant tables(授權表)
    	    ```sql
    	    FLUSH PRIVILEGES;
    	    ```
        8. Logout
            ```sql
            quit
            ```
    9. Change CTFd database linked
        1. Edit `config.py`
        	```shell
        	sudo vim ~/CTFd/CTFd/config.py
        	```
        2. Change DATABASE_URL & REDIS_URL value
            ```python
            DATABASE_URL = 'mysql+pymysql://MariaDB_User:MariaDB_Password@localhost:3306/ctfd'
            REDIS_URL = 'redis://127.0.0.1:6379'
            ```
            ![](https://i.imgur.com/sY4ARmc.png)
    10. Add CTFd path to python sys.path & comment some codes
        1. Edit `wsgi.py`
        	```shell
        	sudo vim ~/CTFd/wsgi.py
        	```
        2. Add content & comment some codes
            ```python
            sys.path.insert(0, '/home/ksu/CTFd')
            ```
            ![](https://i.imgur.com/O4gSbVH.png)
    11. Change uwsgi setting
        1. Edit `uwsgi.ini`
            ```shell
        	sudo vim /etc/uwsgi/apps-available/uwsgi.ini
        	```
        2. Add content
            ```ini=
            [uwsgi]
			# Where you've put CTFD
			#http=127.0.0.1:65535
			chdir = Your_CTFd_Location

			mount = /="CTFd:create_app()"

			plugins-dir = /usr/lib/uwsgi/
			plugin = /usr/lib/uwsgi/plugins/python3_plugin.so
			socket= /tmp/uwsgi.sock
			chmod-socket = 666
			master=true
			processes = 10
			threads = 20
			max-requests = 100
			enable-threads = true
			vacuum = true
			mod-socket = 666
			manage-script-name = true
			wsgi-file = wsgi.py
			callable = app

			limit-as = 6144
			limit-post = 104857600
			reload-on-as = 1024
			reload-on-rss = 1024
			#evil-reload-on-as = 2048
			#evil-reload-on-rss = 1024
			#max-requests = 1000
			#max-worker-lifetime = 600
			#reload-on-rss = 6144
			#worker-reload-mercy = 600

			harakiri = 60

			#die-on-term = true


			#socket=/tmp/uwsgi.sock
			uid = www-data
			gid = www-data
			daemonize=/var/log/uwsgi/ctfd.log
            ```
            ![](https://i.imgur.com/0RUd7wU.png)
    12. Linked uwsgi
        ```shell
        sudo ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/uwsgi.ini
        ```
    13. Change CTFd directory premission
        ```shell
        sudo chown -R www-data:www-data ~/CTFd/
        ```
    14. Change nginx setting
        1. Remove defalt setting
            ```shell
            sudo rm /etc/nginx/sites-available/default
            ```
        2. Creat & edit a new defalt setting
            ```shell
            sudo vim /etc/nginx/sites-available/default
            ```
        3. Add content
            ```nginx=
            server {
			        listen 80 default_server;
			        listen [::]:80 default_server;
				root Your_CTFd_directory; 
				index index.html index.htm index.nginx-debian.html;
			
			        #server_name 120.114.62.218;
			
				location / {
			             #try_files $uri $uri/ =404;
			             root Your_CTFd_directory;
			             include uwsgi_params;
			             uwsgi_pass unix:/tmp/uwsgi.sock;
			             uwsgi_read_timeout 300s;
			        }
				location /static {
			               root Your_CTFd_directory/CTFd/themes/core/static/;
			        }
				client_max_body_size 1000m;
			        }
            ```
            ![](https://i.imgur.com/iPlvi0D.png)

    15. Creat start CTFd script
        - `start.sh`
            ```shell
            sudo uwsgi -d --ini /etc/uwsgi/apps-enabled/uwsgi.ini
            ```
        - `restart.sh`
            ```shell
            sudo pkill uwsgi -9
            sudo uwsgi -d --ini /etc/uwsgi/apps-enabled/uwsgi.ini
            ```
        - `stop.sh`
            ```shell
            sudo pkill uwsgi -9
            ```
    16. Start CTFd
        ```shell
        chmod +x start.sh
        ./start.sh
        ```
    17. restart nginx
        ```shell
        sudo service nginx restart
        ```
4. Setting CTFd
    1. Website
        1. Input CTFd platform name
            ![](https://i.imgur.com/trPuhBc.png)
        2. Choose mode
            ![](https://i.imgur.com/IcPyrtW.png)
        3. Add a new administrator
            ![](https://i.imgur.com/euTmmNr.png)
        4. Setting style
            ![](https://i.imgur.com/rhRzVuO.png)
        5. Setting start / end Date & Time
            ![](https://i.imgur.com/jq8L4GV.png)
        6. Click finish
            ![](https://i.imgur.com/oQmaNUo.png)
    2. Import data
        1. ![](https://i.imgur.com/YV9gehW.png)
        2. ![](https://i.imgur.com/2upZY1f.png)
        3. ![](https://i.imgur.com/sHvjAcF.png)
    3. Install docker questions
        1. Download questions
            ```shell
            sudo wget http://120.114.62.217/MyFirstSecurity_Docker.zip
            ```
        2. Decompress `MyFirstSecurity_Docker.zip`
            ```shell
            sudo unzip MyFirstSecurity_Docker.zip
            ```
        3. Execute `docker.sh`
            ```shell
            sudo sh docker.sh
            ```
        4. Check it is running or not
            ```shell
            sudo docker ps -a
            ```
            ![](https://i.imgur.com/8JKzJIm.png)
        5. Connect to your docker questions bash
            ```shell
            sudo docker exec –ti [CONTAINER ID] bash
            ```
        6. Run `start.sh`(Press Enter to continue)
            ```shell
            sh /bin/start.sh
            ```
            ![](https://i.imgur.com/7u5roYB.png)
        7. Leave your docker questions bash
            ```shell
            exit
            ```
    4. Change questions IP
        1. Login mariaDB(root)
            ```shell
            sudo mysql –u root –p
            ```
        2. Choose database
            ```sql
            USE Your_Database_Name;
            ```
        3. Change IP
            ```sql
            UPDATE `challenges` SET `description` = replace(`description`, 'old', 'new');
            ```
            ![](https://i.imgur.com/TwUwcRf.png)

# Types
### CTFd
- Log file location
    ```shell
    /var/log/uwsgi/ctfd.log
    ```

### MariaDB
- List all database
    ```sql
    SHOW DATABASES;
    ```
    ![](https://i.imgur.com/NUAMxnW.png)