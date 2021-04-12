# adding custom response header
package { 'nginx':
	ensure => installed
}

nginx::resource::vhost {
add_header=> {
	'X-Served-By' => '',
}

service { 'nginx':
	ensure  => running,
	restart => true,
	require => Package['nginx'],
}
