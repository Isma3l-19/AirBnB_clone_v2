#!/usr/bin/env bash
# set up web server for deployment

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install -y nginx
fi
    sudo mkdir -p /data/web_static/releases/test/
    sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>This is a test page for Nginx configuration</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# create symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current
# set ownership
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the
# content of /data/web_static/current/

location_header="location \/hbnb\_static\/ {"
location_content="alias \/data\/web\_static\/current\/;"
new_location="\n\t$location_header\n\t\t$location_content\n\t}\n"
sudo sed -i "37s/$/$new_location/" /etc/nginx/sites-available/default

sudo service nginx restart
