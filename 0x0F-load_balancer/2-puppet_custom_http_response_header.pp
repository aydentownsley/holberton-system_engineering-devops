# adding custom response header
package { 'nginx':
  ensure => installed,
}

file_line { 'add_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'http {  add_header X-Served-By $hostname;',
  match => 'http {',
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
