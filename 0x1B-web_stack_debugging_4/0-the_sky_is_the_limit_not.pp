# Increases the open file limit in default file of nginx

exec {'fx-limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/i" /etc/default/nginx'; sudo service nginx restart,
  before   => Exec['res'],
}
