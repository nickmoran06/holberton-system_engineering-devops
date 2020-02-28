# Changing soft instead hard and viceversa

exec {'soft_hard_feature':
  command => "/usr/bin/sed -i 's/holberton hard nofile 5/holberton hard nofile 50' /etc/security/limits.conf;\
  /usr/bin/sed -i 's/holberton soft nofile 4/holberton soft nofile 40' /etc/security/limits.conf"
}
