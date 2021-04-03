#!/usr/bin/puppet
#Setting up serv to connect w/o pwd

class { '::ssh::server':
  options => {
    'IdentityFile'           => '~/.ssh/holberton',
    'PasswordAuthentication' => 'no',
  },
}
