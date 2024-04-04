#!/usr/bin/env bash
# This  script prepares the web servers for deplpoyement

sudo apt update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo sed -i "s/server_name _;/&\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html;\n\t}\n/" /etc/nginx/sites-enabled/default
sudo service nginx restart
