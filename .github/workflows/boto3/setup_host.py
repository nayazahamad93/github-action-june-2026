import subprocess

import shutil
import os




def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


if shutil.which("nginx"):
    print("nginx is already installed!!")
else:
    command = "sudo apt-get update && sudo apt-get install -y nginx"
    run(command)


# 2. Setup Nginx config for it-defined.com (and remove default site)
run("sudo mv ./it-defined.com.conf /etc/nginx/sites-available/it-defined.com")
run("sudo ln -sf /etc/nginx/sites-available/it-defined.com /etc/nginx/sites-enabled/it-defined.com")
run("sudo rm -f /etc/nginx/sites-enabled/default")

# 3. Copy the code to /var/www/it-defined.com
run("sudo mkdir -p /var/www/it-defined.com")
run("sudo mv ./index.html /var/www/it-defined.com/index.html")

# Reload nginx
run("sudo nginx -t && sudo systemctl reload nginx")