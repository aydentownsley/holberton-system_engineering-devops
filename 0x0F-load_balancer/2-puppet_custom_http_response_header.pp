#!/usr/bin/puppet
# adding custom response header
package { 'nginx':
  ensure => installed
}

exec { 'addheader':
  command => "sed -i 's\http {\http {\\n\\tadd_header X-Served-By \$hostname;\\n\' /etc/nginx/nginx.conf",
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
