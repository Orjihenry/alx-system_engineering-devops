# Bug fix on wordpress site running on apache2

exec { 'wordpress bug fix':
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
