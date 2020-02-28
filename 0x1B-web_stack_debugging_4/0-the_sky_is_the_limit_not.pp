# Increases the open file limit in default file of nginx

exec {'open_limit':
  command  => 'sudo sed -i 's/15/4096' /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
