#!/usr/bin/env bash
# This shell  script prepares the web servers for deployement
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html><body><h1>Hello, Souka</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo rm -f /data/web_static/current
#if [ ! -e /etc/nginx/sites-enabled/hbnb_static ]; then
#            sudo ln -s /data/web_static/releases/test/ /data/web_static/current
#fi'''
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

echo "server {
    listen 80;
    server_name easypath.tech;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        try_files \$uri \$uri/ =404;
    }
}" | sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null

sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo systemctl restart nginx

