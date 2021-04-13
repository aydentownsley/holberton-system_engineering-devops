# adding custom response header

package { 'nginx':
  ensure => installed,
}

file { 'add_header':
  esnure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
