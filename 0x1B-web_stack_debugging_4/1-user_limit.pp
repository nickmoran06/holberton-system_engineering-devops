# Changing soft instead hard and viceversa

exec {'soft':
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf',
}

exec {'hard':
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
  before   => Exec['soft'],
}
