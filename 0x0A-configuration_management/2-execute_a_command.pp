# killing process
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin/:/root',
}
