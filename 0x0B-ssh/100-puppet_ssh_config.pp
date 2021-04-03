#!/usr/bin/puppet
#Setting up serv to connect w/o pwd

augeas { 'id file':
  context => '/etc/ssh/ssh_config',
  changes => 'set IdentityFile ~/.ssh/holberton',
}

augeas { 'pwd auth':
  context => '/etc/ssh/ssh_config',
  changes => 'set PasswordAuthentication no',
}

