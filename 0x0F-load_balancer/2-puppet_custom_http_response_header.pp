# adding custom response header

exec { 'update':
  command => 'apt-get update',
  provider => '/usr/bin/bash',
}
->
package { 'nginx':
  ensure => installed,
}
->
file { 'add_header':
  esnure => present,
  path  => /etc/nginx/sites-available/default,
  after => 'listen 80 default_server',
  line => 'add_header X-Served-By $hostname;',
}
->
service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
