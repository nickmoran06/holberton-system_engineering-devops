# Using puppet, edit the ssh_config file:
# Must be configured to use the private key ~/.ssh/holberton
# Must be configured to refuse to authenticate using a password

exec { 'echo':
  command  => 'echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config'
  provider => 'shell'
}