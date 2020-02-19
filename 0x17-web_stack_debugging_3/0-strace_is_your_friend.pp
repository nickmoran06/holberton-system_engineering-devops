# typo 500 error, to fix it is changing php instead phpp
exec { 'php_instead_phpp':
path     => '/bin/',
command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}
