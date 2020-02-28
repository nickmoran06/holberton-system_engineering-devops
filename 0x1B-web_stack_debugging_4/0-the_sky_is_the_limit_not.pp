# Increases the open file limit in default file of nginx
  command  => "sudo sed -i 's/15/1000' /etc/default/nginx && sudo service nginx restart",
  provider => shell,
}
