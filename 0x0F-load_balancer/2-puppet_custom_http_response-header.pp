#!/usr/bin/env bash
#Install nginx and http header  

exec {'Install nginx':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "15i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
  provider => shell,
}
