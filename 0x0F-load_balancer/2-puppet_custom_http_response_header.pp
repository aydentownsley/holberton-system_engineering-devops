# adding custom response header

package { 'nginx':
  ensure => installed,
}

file_line { 'add_header':
  path  => '/etc/nginx/sites-available/default',
  line  => 'add_header X-Served-By $hostname;',
  match => '# SSL configuration',
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
