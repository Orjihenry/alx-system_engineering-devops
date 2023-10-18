# Increase the ULIMIT to 4096 to fix bug
exec { 'fix--for-nginx':
  command => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}
