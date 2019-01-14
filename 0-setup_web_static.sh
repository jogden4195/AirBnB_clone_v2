#!/usr/bin/env bash
#Sets up our web servers for the deployment of web_static

#Installing Nginx
sudo apt-get update
sudo apt-get -y install nginx

#Creating folders
sudo mkdir -p data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#Creating test html file
touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t\tHolberton School\n\t</head>\n</html>" | sudo tee /data/web_static/releases/test/index.html

#Creating symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

#Giving ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

#Updating Nginx configuration to serve content of /data/web_static/current/ to hbnb_static
sudo sed -i '41i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#Restarting Nginx
sudo service nginx restart
