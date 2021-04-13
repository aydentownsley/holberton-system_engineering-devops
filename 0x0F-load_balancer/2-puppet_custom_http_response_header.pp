# adding custom response header
package { 'nginx':
	ensure => installed
}

file_line {
	command => 'sed -i "s/http {/http {\n\tadd_header X-Served-By \$hostname;\n/"' /etc/nginx/nginx.conf
}

service { 'nginx':
	ensure  => running,
	restart => true,
	require => Package['nginx'],
}
